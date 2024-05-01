import websocket
import json
import time

result = []


def on_open(ws):
    print("--- opened ---")


def on_message(ws, message):
    msg = json.loads(message)
    print(msg)
    if 'action' in msg and msg['action'] == 'insert':
        result.append(msg)
        ws.close()


def on_error(error):
    print(error)


def on_close(ws):
    print("--- closed ---")
    print(result)

ws = websocket.WebSocketApp("wss://www.bitmex.com/realtime?subscribe=trade:XBTUSD",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.run_forever()
