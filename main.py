from websocket import create_connection  # pip install websocket-client


if __name__ == '__main__':
    print('req')

    ws = create_connection("wss://ws.postman-echo.com/raw", timeout=3)  # timeout 3 second
    ws.send("AI?")

    result = ws.recv()
    print(result)
    ws.close()

    print('done')
