# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).
import asyncio
from time import time, ctime

async def serve_customer(customer_name):
    print(f"[{ctime()}] Serving customer {customer_name}...")
    await asyncio.sleep(1)  # Simulate a delay for serving the customer
    print(f"[{ctime()}] Finished serving customer {customer_name}.")

async def main():
    start = time()
    #if you await them one by one they still run sequentially
    await serve_customer("A")
    await serve_customer("B")

    print(f"[{ctime()}] Total time taken: {time() - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
    