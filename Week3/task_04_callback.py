# Objective: Attach a plain synchronous function that automatically triggers the moment a task finishes.
import asyncio
from time import ctime

def alert_manager(finished_task):
    # callback functions automatically accept the completed task object as the first argument
    print(f"{ctime()} Callback Triggered! Task output fetched: {finished_task.result()}")

async def download_file():
    print(f"{ctime()} Downloading packet...")
    await asyncio.sleep(1.0)
    return "Data_Payload.zip"

async def main():
    task = asyncio.create_task(download_file())
    # register the callback function (Do not add parenthesis '()' to avoid immediate execution)
    task.add_done_callback(alert_manager)
    
    await task # 

asyncio.run(main())