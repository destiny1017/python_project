import requests
import threading

def send_request(url):
    response = requests.get(url)
    print(response.text)

def main():
    url = 'http://localhost:8080/multi-request'  # 서버 URL

    threads = []
    for i in range(20):  # 10개의 클라이언트 요청을 보냄
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
