import requests
import json

#내 어플리케이션 > 앱키 > 에서 확인한 API키값 입력
#https://developers.kakao.com/console/app/843374
REST_API_KEY = '0286a9a54958d690b1990ae525adbc67'

def kogpt_api(prompt, max_tokens = 1 , temperature = 1.0, top_p=1.0, n=1) :
    r= requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
        'prompt' : prompt,
        'max_tokens' : max_tokens,
        'temperature' : temperature,
        'top_p' : top_p,
        'n' : n},
        headers = {'Authorization' : 'KakaoAK' + REST_API_KEY,
                             'Content-Type' : 'application/json'}
    , verify= False)
    #응답 json형식으로 변환
    response = json.loads(r.content)
    return response

#KoGPT에게 전달할 명령어 구성
#prompt =  ['테슬라 주가전망','미국주식환전법','남성패딩추천']
k ='한경희생활과학 촉촉한가습기 EHMN-B170(화이트)'
prompt =  [k+' 사용후기 장단점']
'''
contents = []
for i in prompt :
    print(i)
    res4 = kogpt_api(prompt = i,
    max_tokens = 150,
    temperature = 1.0,
    top_p = 1.0,
    n = 1)
    contents.append(res4['generations'][0]['text'].replace('\u200b','\n'))

print(contents)
'''