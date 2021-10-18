import socket
import threading
import time
from tqdm import tqdm

# mylist = range(1, 21)

# for i in tqdm(mylist):
#     time.sleep(0.1)
start_time = time.time()

p_lock = threading.Lock()  # Потокобезопасность
N = 5000
port = 1500
part = N//20
k = 1


def scan(N):
    global part
    global k
    global port

    while int(port) != N:
        port += 1
        try:
            sock = socket.socket()
            sock.settimeout(0.01)
            sock.connect(('127.0.0.1', port))
            print("\n"+"\033[32mПорт", str(port), "открыт\033")
        except ConnectionRefusedError:
            pass
            # print("\n"+"\033[31mПорт", str(port), "закрыт")
            # sock.close()
        finally:
            sock.close()
    with p_lock:
        if int(port) == k*part:
            k += 1


t = [threading.Thread(target=scan, args=[N]) for i in range(20)]  # Создаем потоки

[t1.start() for t1 in t]  # Запускаем каждый поток

[t1.join() for t1 in t]  # Позволяет выполнить все потоки, а после продолжить выполнение программы в главном потоке

print("All is ok in the end")
print("--- %s seconds ---" % (time.time() - start_time))