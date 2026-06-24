from time import sleep, ctime, time
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คนแบบซิงโครนัส
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} - Making coffee for {customer_name}...")
    sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} - Finished making coffee for {customer_name}.")

def main():
    queue = ['a', 'b', 'c']  # รายชื่อลูกค้าที่รอทำกาแฟ
    main_pid = os.getpid()
    main_thread_id = threading.current_thread().native_id

    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} - Starting coffee making process...")
    start_time = time()

    for customer in queue:
        make_coffee(customer)

    duration = time() - start_time
    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} - Finished all coffee making in {duration:.2f} seconds.")
if __name__ == "__main__":
    main()
    