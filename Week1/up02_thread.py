from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):
    print(f"[{ctime()}] LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"[{ctime()}] LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"[{ctime()}] Making coffee for {customer_name}...")
    sleep(1)
    print(f"[{ctime()}] Coffee ready for {customer_name}!")

def main():
    queue = ['A', 'B', 'C']
    start_time = time()

    print(f"[{ctime()}] === Multi-threading Coffee Machine ===")

    threads = []
    for customer in queue:
        # สร้าง thread ที่ทำทั้งสองงานต่อเนื่องกัน
        t = threading.Thread(target=lambda name=customer: (
            make_coffee(name),
            update_cup_number(name)
        ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    print(f"[{ctime()}] Total time: {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
