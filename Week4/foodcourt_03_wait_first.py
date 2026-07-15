# foodcourt_03_wait_first.py
import asyncio
from time import ctime, time  
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301045"
    print(f"{ctime()} | --- [Task 3] Practice using wait with return_when=FIRST_COMPLETED ---")
    
    
    # Create three tasks for different food orders
    order = {
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "steak", "Beef Steak")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "noodle", " Clear Soup Noodles")),
        asyncio.create_task(send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice thigh"))
    }
    # Wait until the first task completes
    done, pending = await asyncio.wait(order, return_when=asyncio.FIRST_COMPLETED)
    

    fastest_dish = list(done)[0].result()
    print(f"{ctime()} | Winnerserved dish shop: {fastest_dish['shop']} | Menu: {fastest_dish['menu']}")
    # Get and print the result of the fastest order with timestamp
    
    print(f"{ctime()} | Cleaning up: Canceling {len(pending)} remaining pending orders...")
    for p in pending:
        t.cancel()


        print(f"{ctime()} | Totol waiting time for the frist dish: {time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    asyncio.run(main())