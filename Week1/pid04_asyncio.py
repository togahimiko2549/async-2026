from time import ctime, time
import asyncio
import os
import threading

# ฟังก์ชันจำลองการทำกาแฟแบบ Asynchronous
async def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id

    current_task = asyncio.current_task()
    task_name = current_task.get_name() 

    task_id = id(current_task)

    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Task ID: {task_id}, Task Name: {task_name} - Making coffee for {customer_name}...")
    await asyncio.sleep(5)  # จำลองเวลาที่ใช้ในการทำกาแฟ
    print(f"[{ctime()}] Process ID: {pid}, Thread ID: {thread_id}, Task ID: {task_id}, Task Name: {task_name} - Finished making coffee for {customer_name}.")


async def main():
    queue = ['a', 'b', 'c']  # รายชื่อลูกค้าที่รอทำกาแฟ
    main_pid = os.getpid()
    main_thread_id = threading.current_thread().native_id

    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} - Starting coffee making process...")
    start_time = time()

    tasks = []
    for customer in queue:

        coro = make_coffee(customer)
        task = asyncio.create_task(coro, name=f"Task-{customer}")
        tasks.append(task)

    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"[{ctime()}] Main Process ID: {main_pid}, Main Thread ID: {main_thread_id} - Finished all coffee making in {duration:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())