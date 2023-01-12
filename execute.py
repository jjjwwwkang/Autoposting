import NaverDataLab as ND
import coupang as cp
import posting as post
import time
import kakaogpt as kgpt
#일단 키워드를 모으자.
#keywords = ND.get_keywords()

#print(keywords)
#모은 키워드로 쿠팡에서 데이터프레임을 만들자
#df = cp.get_coupang(keywords)

#print(df)

#구글블로거 포스팅
import sys
import os
import pickle
from oauth2client import client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

BLOG_ID = "8038814675849111994" #구글블로거아이디
SCOPES = ['https://www.googleapis.com/auth/blogger']
def get_blogger_service_obj() :
    creds = None
    if os.path.exists('auto_token.pickle') :
        with open('auto_token.pickle','rb') as token :
            creds = pickle.load(token)
    if not creds or not creds.valid :
        if creds and creds.expired and creds.refresh_token :
            creds.refresh(Request())
        else :
            # 다운받은 json이 있는 주소를 적어주기
            flow = InstalledAppFlow.from_client_secrets_file(
                'C:/users/Lenovo/PycharmProjects/autoposting/client_secret.json', SCOPES)
            creds = flow.run_local_server(port = 0)
        with open('auto_token.pickle','wb') as token :
            pickle.dump(creds, token)
    blog_service = build('blogger','v3', credentials = creds)
    drive_service = build('drive','v3',credentials = creds)
    return drive_service, blog_service

def posting(content, title, keyword) : #내용, 상품명, 태그
    data = data = {
    'content': content,
    'title' : title,
    'labels' : keyword,
    'blog' : {
        'id' : BLOG_ID,
    },}
    drive_handler, blog_handler = get_blogger_service_obj()
    posts = blog_handler.posts()
    res = posts.insert(blogId = BLOG_ID, body = data, isDraft = False, fetchImages = True).execute()
    return print('{}완료'.format(title))

#실제 포스팅코드 : 주의!!! 실행 누르면 키워드 생성부터 다시시작함

today = ND.get_today()
while True:
    if today == '1' or today == '11' or today == '21':
        keywords = ND.get_keywords()
        df = cp.get_coupang(keywords)
        for i in range(len(df)):

            word = df.iloc[i]['names']+'사용후기 장단점'
            res4 = kgpt.kogpt_api(prompt = word, max_tokens = 200, temperature =1.0,top_p = 1.0, n = 1 )
            ment = res4['generations'][0]['text']
        #포스팅
            posting('<p><b>'+df.iloc[i]['names']+'</b></p>'
                    '<br/><br/>'+'<p>최저가:'+'<b>'+df.iloc[i]['prices']+'<b></p>'
                    '<br/><br/><br/>'
                    '<img src="//'+df.iloc[i]['images']+'">'
                   '<br/><br/><br/>'
                    '<a href='+df.iloc[i]['urls']+'>'+'최저가로 사러가기</a>'
                    '<br/><br/><br/>'+
                   '<p>'+ment+'</p>',
                  df.iloc[i]['names']+' 솔직리뷰 최저가', df.iloc[i]['keyword'])
            time.sleep(3600*4)



