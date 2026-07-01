# Program 9: Dynamically Tracking Tasks in a List
# Concept: Managing multiple generated tasks dynamically by appending them into a standard Python list.
import asyncio
from time import time, ctime

async def serve_customer(customer_name):
    print(f"[{ctime()}] Starting service for customer {customer_name}...")
    await asyncio.sleep(1)  # Simulate a delay for serving the customer
    print(f"[{ctime()}] Finished service for customer {customer_name}!")

async def main():
    start = time()
    customers = ["A", "B", "C", "D"]
    tasks_list = []

    for name in customers:
        t = asyncio.create_task(serve_customer(name))
        tasks_list.append(t)

    for t in tasks_list:
        await t
    
    print(f"Served all {len(customers)} customers in {time() - start:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())