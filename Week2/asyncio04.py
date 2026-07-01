# Program 4: The await Keyword
# Concept: Pausing a coroutine to let another operation finish using await.
import asyncio
from time import ctime

async def main():
    print(f"{ctime()}---->Task Started")

    #await tell the event loop 

    await asyncio.sleep(1)  # Pauses the coroutine for 1 second, allowing other operations to run.

    print(f"{ctime()}---->Task Ended")

if __name__ == "__main__":
    asyncio.run(main())  # This runs the main coroutine, executing it and handling the await.

