# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello for the Event Loop!")


if __name__ == "__main__":
    coro_objiect = greet()  # This creates a coroutine object but does not execute it yet.


    asyncio.run(coro_objiect)  # This runs the coroutine object using the event loop, executing it.
