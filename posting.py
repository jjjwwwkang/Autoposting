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


#keyword = '자동포스팅' #태그
#blogger_title = '오 감동적이다' #블로그제목
#content = '이야 이게 되네?' #내용
'''
data = {
    'content':content,
    'title' : blogger_title,
    'labels' : keyword,
    'blog' : {
        'id' : BLOG_ID,
    },}

#실행하는데 필요한 파라미터들
#drive_handler, blog_handler = get_blogger_service_obj()
#posts = blog_handler.posts()
#res = posts.insert(blogId = BLOG_ID, body = data, isDraft = False, fetchImages = True).execute()
#res #결과물
'''

