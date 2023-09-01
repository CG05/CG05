import asyncio
import websockets
import requests

# 카카오톡 API 토큰과 채팅방 ID 설정
KAKAO_API_TOKEN = 'YOUR_KAKAO_API_TOKEN'
CHAT_ROOM_ID = 'YOUR_CHAT_ROOM_ID'
MY_USER_ID = 'YOUR_USER_ID'  # 자신의 카카오톡 사용자 ID

# 카카오톡 메시지 가져오는 함수
def get_kakao_messages():
    headers = {
        'Authorization': f'Bearer {KAKAO_API_TOKEN}'
    }
    response = requests.get(f'https://kapi.kakao.com/v1/chats/{CHAT_ROOM_ID}/messages', headers=headers)
    return response.json()

# 카카오톡 메시지 보내는 함수
def send_kakao_message(text):
    headers = {
        'Authorization': f'Bearer {KAKAO_API_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {
        'chatId': CHAT_ROOM_ID,
        'type': 'text',
        'text': text,
    }
    response = requests.post('https://kapi.kakao.com/v1/messages', headers=headers, json=data)
    return response.json()

# WebSocket 서버 설정
async def server(websocket, path):
    while True:
        await websocket.send("Listening for new messages...")

        async for message in websocket:
            if message == 'get_messages':
                messages = get_kakao_messages()
                await websocket.send(messages)  # 메시지를 클라이언트에게 보내거나 처리
            elif message.startswith('send_message:'):
                _, text = message.split(':')
                send_kakao_message(text)
                await websocket.send(f"Sent message: {text}")

# WebSocket 서버 실행
start_server = websockets.serve(server, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
