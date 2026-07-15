# foodcourt_02_gather.py

import asyncio
from time import time, ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301045"
    print(f"{ctime()} | --- [Task 2] Practice using gather to wait for all group orders ---")
    
    # Create three tasks for different food orders


t1 = asyncio.create_task(send_order_to_kitchen("6710301045", "hainanese_chicken", "Chicken Rice "))
t2 = asyncio.create_task(send_order_to_kitchen("6710301045", "noodle", "wonton Noodles"))
t3 = asyncio.create_task(send_order_to_kitchen("6710301045", "steak", " Sizzling Steak"))


if __name__ == "__main__":
    asyncio.run(main())
