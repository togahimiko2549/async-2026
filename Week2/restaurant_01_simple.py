import asyncio
from time import ctime, time, sleep

async def greet_diners(customer):
    print(f"{ctime()} greeting for customer {customer}...")
    sleep(1)
    print(f"{ctime()} greeting for customer {customer}...Done!")

def take_order(customer):
    print(f"{ctime()} taking order for customer {customer}...")
    sleep(1)
    print(f"{ctime()} taking order for customer {customer}...Done!")

def do_cooking(customer):
    print(f"{ctime()} cooking for customer {customer}...")
    sleep(1)
    print(f"{ctime()} cooking for customer {customer}...Done!")

def mini_bar(customer):
    print(f"{ctime()} mini bar for customer {customer}...")
    sleep(1)
    print(f"{ctime()} mini bar for customer {customer}...Done!")

if __name__ == "__main__":
    customers = ['A', 'B', 'C']
    start_time = time()
    for customer in customers:
        greet_diners(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)

    duration = time() - start_time
    print(f"{ctime()} Finished Cooking in {duration:.2f} seconds")
    