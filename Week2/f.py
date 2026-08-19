import asyncio
import time
#async def task_a():
#    print("1")
#    await asyncio.sleep(0.1)
#    print("2")
#async def task_b():
#    print("3")
#    print("4")
#async def main():
#    b1 = asyncio.create_task(task_a())
#    b2 = asyncio.create_task(task_b())
#    await b1
#    await b2
#asyncio.run(main())
#########################
#async def worker(n):
#    await asyncio.sleep(0.5)
#    return n*10
#async def main():
#    tasks = [asyncio.create_task(worker(i)) for i in range(1, 4)]
#    for t in tasks:
#        res = await t
#        print (res, end="")
######################3
#async def fail_task():
#    await asyncio.sleep(0.1)
#    raise ValueError("Error")
#async def pass_task():
#    await asyncio.sleep(0.2)
#    return "ok"
#async def main():
#    try:
#        res = await asyncio.gather(fail_task(), pass_task())
#        print(res)
 #   except ValueError as e:
  #      print(f"Caught:{e}")
##############################
#    try:
#    except asyncio.CancelledError:
#        print("cancelleds")
#        raise
#async def main():
#    task = asyncio.create_task(job())
#    await asyncio.sleep(1)
#    task.cancel()
#    try:
 #       await task
#    except asyncio.CancelledError:
#        print("cancelled")
#######################################
#async def task1():
#    await asyncio.sleep(0.2)
#    return "t1"
#async def task2():
#    await asyncio.sleep(0.1)
#    return "t2"
#async def main():
#    done, pending = await asyncio.wait(
#        [asyncio.create_task(task1()), asyncio.create_task(task2())],
#        return_when=asyncio.ALL_COMPLETED
#    )
#    print(f"done count: {len(done)}, pending count: {len(pending)}")
###################################
#async def worker(n):
#    await asyncio.sleep(n)
#    if n == 2:
#        raise ValueError("failed on 2")
#    return n
#async def main():
 #   tasks = [asyncio.create_task(worker(i)) for i in [1,2,3]]
#    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
#    print(f"done : {len(done)}, pending : {len(pending)}")
######################
#async def worker(n):
#    return n*2
#async def main():
#    coros = [worker(1), worker(2), worker(3)]
#    res = await asyncio.gather(*coros)
#    print(res)
###################################
#async def worker(delay):
#    await asyncio.sleep(delay)
#    return delay
#async def main():
#    start = time.time()
#    res = await asyncio.gather(worker(1), worker(2), worker(3))
#    print(f"time: {round(time.time()-start)}, result: {res}")
#############################
#async def slow_job():
#    try:
#        await asyncio.sleep(10)
#        return "done"
#    except asyncio.CancelledError:
#        print("slow_job cancelled")
#        raise
#async def main():
#    try:
#        await asyncio.wait_for(slow_job(), timeout=2.0)
#    except asyncio.TimeoutError:
 #       print("timeout")
###################################
#async def my_coro():
#    print("a")
#    await asyncio.sleep(0)
#    print("b")
#
#async def main():
#    task = asyncio.create_task(my_coro())
#    print("c")
#    await task
####################################
#async def worker(n):
#    await asyncio.sleep(n)
#    return n
#async def main():
#    tasks = [asyncio.create_task(worker(i)) for i in [3, 2, 1]]
#    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
#    print([t.result() for t in done])
##################################
#async def count():
#    print("One")
#    await asyncio.sleep(1)
#    print("Two")
#async def main():
 #   await asyncio.gather(count(), count(), count())
#########################
#async def compute(x):
#    return x * 2
#async def main():
#    t1 = asyncio.create_task(compute(5))
#    t2 = asyncio.create_task(compute(10))
#    res2 = await t2
#    res1 = await t1

#    print(f"{res1}, {res2}")
###################################
#async def compute(val):
#    return val * 2
#async def main():
#    coro = compute(10)
#    res= coro()
#    print(res)
################################


asyncio.run(main())
