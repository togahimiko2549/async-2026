from multiprocessing import Process
from time import sleep, ctime, time

def update_cup_number(customer_name):
    print(f"[{ctime()}] LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"[{ctime()}] LCD: Done for customer {customer_name}.")

def make_coffee(customer_name):
    print(f"[{ctime()}] Making coffee for {customer_name}...")
    sleep(1)
    print(f"[{ctime()}] Coffee ready for {customer_name}!")

# ✅ ย้ายออกมาเป็นฟังก์ชัน global
def process_customer(customer_name):
    make_coffee(customer_name)
    update_cup_number(customer_name)

def main():
    queue = ['A', 'B', 'C']
    start_time = time()

    print(f"[{ctime()}] === Multi-processing Coffee Machine ===")

    processes = []
    for customer in queue:
        p = Process(target=process_customer, args=(customer,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    duration = time() - start_time
    print(f"[{ctime()}] Total time: {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
