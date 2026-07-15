import asyncio
from time import ctime
from food_utils import send_order_to_kitchen

async def main():
    MY_STUDENT_ID = "6710301045"
    print(f"{ctime()} | --- [Task 4] Practice using wait_for to handle timeouts ---")
    print(f"{ctime()} | [System] Order sent. Monitoring 2.0s timeout limit...")

    steak_task = asyncio.create_task(
        send_order_to_kitchen(MY_STUDENT_ID, "steak", "Sizzling Steak")
    )

    try:
        steak_result = await asyncio.wait_for(steak_task, timeout=2.0)
        print(f"{ctime()} | [Success] Steak served on time! Menu: {steak_result['menu']}")
    except asyncio.TimeoutError:
        print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now.")
        steak_task.cancel()
        try:
            await steak_task
        except asyncio.CancelledError:
            print(f"{ctime()} | [Cleanup] Steak order has been canceled.")
    finally:
        print(f"{ctime()} | Task 4 completed.")


if __name__ == "__main__":
    asyncio.run(main())
