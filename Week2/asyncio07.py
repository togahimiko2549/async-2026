# Program 7: Dual Tasks Concurrency
# Concept: Scheduling two distinct tasks concurrently and awaiting them individually without gather.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer_name):
    print(f"[{ctime()}] Starting Cooking spaghetti for customer {customer_name}...")
    await asyncio.sleep(1)  # Simulate a delay for cooking spaghetti
    print(f"[{ctime()}] Finished Cooking spaghetti for customer {customer_name}!")

async def main ():
    start = time()
    # Create two tasks for cooking spaghetti for different customers
    task_a = asyncio.create_task(cook_spaghetti("A"))
    task_b = asyncio.create_task(cook_spaghetti("B"))

    # Await each task individually
    await task_a
    await task_b

    print(f"Total Operation time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())