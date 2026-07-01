# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.
import asyncio

async def greet():
    print("Hello, World!")


coro_objiect = greet()  # This creates a coroutine object but does not execute it yet.


print(type(coro_objiect))  # <class 'coroutine'>


coro_objiect.close()  # This closes the coroutine object without executing it.
