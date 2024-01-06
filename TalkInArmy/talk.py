import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = '5f0353187a6b977140fccbaa373ad026'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'oWls0w9wvhNiBIkaYsX-mH7OVbP1HKMO234O7J3Liw1KRMgb-mzPrXQrAlIKPXSYAAABjN8vp9Gi-KZYUq23DA'
#https://kauth.kakao.com/oauth/authorize?client_id=5f0353187a6b977140fccbaa373ad026&redirect_uri=https://example.com/oauth&response_type=code

def f_auth():
    data = {
    'grant_type': 'authorization_code',
        'client_id': rest_api_key,
        'redirect_uri': redirect_uri,
        'code': authorize_code,
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    r_token = ts["refresh_token"]
    return r_token


def f_auth_refresh(r_token):
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    data = {
        "grant_type": "refresh_token",
        "client_id": rest_api_key,
        "refresh_token": r_token
    }
    response = requests.post(url, data=data)
    tokens = response.json()

    with open(r"kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    with open("kakao_code.json", "r") as fp:
        ts = json.load(fp)
    token = ts["access_token"]
    return token


def f_send_talk(token, text):
    header = {'Authorization': 'Bearer ' + token}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'  
    post = {
        'object_type': 'text',
        'text': text,
        'link': {
        'web_url': 'https://developers.kakao.com',
            'mobile_web_url': 'https://developers.kakao.com'
        },
        'button_title': '키워드'
    }
    data = {'template_object': json.dumps(post)}
    return requests.post(url, headers=header, data=data)


r_token = f_auth()


while True:
    token = f_auth_refresh(r_token)  
    f_send_talk (token, '보낼 메시지')
    time.sleep(1800)
