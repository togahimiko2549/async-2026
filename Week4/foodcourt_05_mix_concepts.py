import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301045"
    print(f"{ctime()} | --- [Task 5] Advanced Practice: Mixing concepts together ---")

    # 1. Create a regular task for the noodle order.
    noodle_task = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "noodle", "Egg Noodles")
    )

    # 2. Create a task for chicken rice wrapped inside a wait_for timeout.
    chicken_task = asyncio.create_task(
        asyncio.wait_for(
            send_order_to_kitchen(MY_STUDENT_ID, "hainanese_chicken", "Chicken Rice Special"),
            timeout=1.0,
        )
    )

    # 3. Combine both tasks and resolve them concurrently using asyncio.gather.
    try:
        results = await asyncio.gather(noodle_task, chicken_task)
        print(f"{ctime()} | Success: All food served on time! Received {len(results)} dishes.")
        for result in results:
            print(f"{ctime()} | Served: {result['shop']} | Menu: {result['menu']}")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Error: An unexpected timeout occurred during gather processing.")
        
    print(f"{ctime()} | Totoal elapsed time: {time() - start_time:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())
