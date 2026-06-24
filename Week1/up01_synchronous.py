from time import sleep, ctime, time

def make_coffee(customer_name):
    print(f"[{ctime()}] Making coffee for {customer_name}...")
    sleep(1)  # Simulate time taken to make coffee
    print(f"[{ctime()}] coffee ready for {customer_name}.")

def update_cup_number(customer_name):
    print(f"[{ctime()}] LCD: processing for customer {customer_name}...")
    sleep(1)  # Simulate time taken to update cup number
    print(f"[{ctime()}] LCD: Done for customer {customer_name}.")


def main():
    queue = ['a', 'b', 'c']  # List of customers waiting for coffee
    start_time = time()

    print(f"[{ctime()}]  ===Synchronous coffee machine===")

    for customer in queue:
        make_coffee(customer)
        update_cup_number(customer)

    duration = time() - start_time
    print(f"[{ctime()}] Total time : {duration:.2f} seconds.")

if __name__ == "__main__":
    main()