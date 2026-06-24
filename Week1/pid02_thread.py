from time import sleep, ctime, time
import threading
import os

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} กำลังชงกาแฟให้ ลูกค้า {customer_name}...")
    sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Thread Name: {thread_name} ชงกาแฟเสร็จสำหรับ ลูกค้า {customer_name}.")
def main():
    queue = ['a', 'b', 'c']  # รายชื่อลูกค้าที่รอทำกาแฟ
    main_pid = os.getpid()
    main_thread_id = threading.current_thread().native_id

    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} - Starting coffee making process...")
    start_time = time()

    threads = []
    for customer in queue:
        thread = threading.Thread(target=make_coffee, args=(customer,), name=f"Thread-{customer}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    duration = time() - start_time
    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} ใช้เวลา {duration:.2f} วินาที.")

if __name__ == "__main__":
    main()