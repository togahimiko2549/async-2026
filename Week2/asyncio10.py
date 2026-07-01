# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.
import asyncio
from time import ctime

async def calulate_bill(customer, base_price):
   print(f"[{ctime()}] Calculating bill for customer {customer}...")
   await asyncio.sleep(1)  # Simulate a delay for bill calculation
   final_price = base_price * 1.07  # Adding a 20% service charge
   return final_price

async def main():
   
   task_a = asyncio.create_task(calulate_bill("A", 100))
   task_b = asyncio.create_task(calulate_bill("B", 200))

   result_a = await task_a
   result_b = await task_b


   print(f"\nFinal Bill A: ${result_a:.2f}")
   print(f"Final Bill B: ${result_b:.2f}")
   print(f"Combined total revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())

