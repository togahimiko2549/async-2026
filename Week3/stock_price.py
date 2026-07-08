import asyncio
import time
import random

# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)


async def fetch_stock_price(server_name: str, delay: float) -> str:
	"""Simulate fetching stock price from a server after a delay."""
	await asyncio.sleep(delay)
	# produce a slightly varying price to look realistic
	price = 150.0 + random.uniform(-1.5, 1.5)
	return f"[{server_name}] Price: {price:.1f} USD"


async def main():
	# create three tasks with specified delays
	tasks = {
		asyncio.create_task(fetch_stock_price("Alpha", 3.0)),
		asyncio.create_task(fetch_stock_price("Beta", 0.8)),
		asyncio.create_task(fetch_stock_price("Gamma", 1.5)),
	}

	# wait until the first task completes
	done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

	# get and print the result of the fastest server with timestamp
	for d in done:
		try:
			result = d.result()
		except Exception as e:
			result = f"Error: {e}"
		ts = time.asctime(time.localtime())
		print(f"{ts} Winner Result: {result}")

	# cancel remaining pending tasks to avoid memory leak
	pending_count = len(pending)
	for p in pending:
		p.cancel()
	# optionally await cancellation to suppress warnings
	if pending:
		await asyncio.gather(*pending, return_exceptions=True)
		ts = time.asctime(time.localtime())
		print(f"{ts} Cleaning up {pending_count} pending tasks...")


if __name__ == "__main__":
	asyncio.run(main())

