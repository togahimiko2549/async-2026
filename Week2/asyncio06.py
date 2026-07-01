# Program 6: Creating a Concurrent Task
# Concept: Wrapping a coroutine inside asyncio.create_task() to schedule it to run in the background.
import asyncio
from time import time, ctime

async def cook_spaghetti(customer_name):
    print(f"[{ctime()}] Starting Cooking spaghetti for customer {customer_name}...")
    await asyncio.sleep(1)  # Simulate a delay for cooking spaghetti
    print(f"[{ctime()}] Finished Cooking spaghetti for customer {customer_name}!")

async def main():
    start = time()
    # Create a task for cooking spaghetti
    task_a = asyncio.create_task(cook_spaghetti("A"))

    # Do other work while the spaghetti is cooking
    print(f"[{ctime()}] Doing other work while spaghetti is cooking...")

    # Wait for the spaghetti to be ready
    await task_a


    print(f"Total Operation time: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())