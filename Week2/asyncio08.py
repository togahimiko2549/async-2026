# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.
import asyncio
from time import ctime

async def kittchen_crew():
    print(f"{ctime()}->[Chef] put noodle in boiling water...")
    await asyncio.sleep(1)  # Simulate a delay for cooking noodles
    print(f"{ctime()}->[Chef] strains the noodle!")

async def bar_crew():
    print(f"{ctime()}->[Bartender] put ice in the glass...")
    await asyncio.sleep(1)  # Simulate a delay for preparing the drink
    print(f"{ctime()}->[Bartender] pours the drink!")

async def main():
    # Create tasks for both workflows
    task_kitchen = asyncio.create_task(kittchen_crew())
    task_bar = asyncio.create_task(bar_crew())

    # Wait for both tasks to complete
    await task_kitchen
    await task_bar

if __name__ == "__main__":
    asyncio.run(main())