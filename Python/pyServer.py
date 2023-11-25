import socket

# 서버 설정
HOST = 'localhost'  # 호스트 (여기서는 로컬호스트)
PORT = 12345        # 포트 번호

# 소켓 생성 및 바인딩
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

# 클라이언트 대기 및 연결 수락
server_socket.listen()
print(f"서버가 {PORT} 포트에서 대기 중...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"클라이언트 {client_address}가 연결되었습니다.")

    # 클라이언트로부터 데이터 받기
    data = client_socket.recv(1024)
    if not data:
        break

    # 받은 데이터를 클라이언트에게 에코
    print(f"클라이언트로부터 받은 메시지: {data.decode('utf-8')}")
    client_socket.send(data)

# 연결 종료
client_socket.close()
server_socket.close()
