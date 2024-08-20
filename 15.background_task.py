import threading
import time
import queue

result = queue.Queue()
print("Before background task")
def background_task(first, second):
    print("Starting background task...")
    time.sleep(5)
    print(f"Inside background task after 5 seconds...{first}")
    time.sleep(10)
    print(f"Inside background task after 10 seconds...{second}")
    result.put({"value": 44})

bg_thread = threading.Thread(target=background_task, args=("WWW", "YYY"))
bg_thread.start()
time.sleep(7)
print("Outside background task")
bg_thread.join()
print("Background task finished")
print(result.get())




