# Objective: Label task objects explicitly to simplify logging and production tracking.
import asyncio
from time import ctime

async def background_worker():
    await asyncio.sleep(0.1)

async def main():
    task = asyncio.create_task(background_worker())
    
    # default auto-generated name assigned by python framework
    print(f"{ctime()} Initial Name: {task.get_name()}") # 
    
    # override name with custom domain specific tag
    task.set_name("Payment-Gateway-Validator")
    print(f"{ctime()} Updated Name: {task.get_name()}") # 

asyncio.run(main())