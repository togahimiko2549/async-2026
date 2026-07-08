# stock_price_httpx.py (เวอร์ชันสำหรับแจกเป็นโจทย์หรือแนวทางให้นักเรียนเขียน)
import asyncio
import httpx
from time import ctime

async def fetch_stock_price(server_name: str):
    url = f"http://127.0.0.1:8088/price/{server_name}"

    # ใช้ httpx.AsyncClient() ดึงข้อมูลแบบไม่บล็อก Event Loop
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return f"[{data['server']}] Price: {data['price_usd']} USD"
    except httpx.HTTPError as exc:
        return f"[{server_name}] Error: {exc}"

async def main():
    # สร้างกลุ่ม Task เพื่อดึงข้อมูลจากเซิร์ฟเวอร์ทั้ง 3 ตัวพร้อมกัน
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha"), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta"), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma"), name="Gamma")
    }

    # รอเซิร์ฟเวอร์ที่ตอบกลับเร็วที่สุดตัวแรก
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    # รอรับผลลัพธ์จาก Task ที่เสร็จแล้ว เพื่อหลีกเลี่ยง warning ของ exception ที่ไม่ถูกดึง
    done_results = await asyncio.gather(*done, return_exceptions=True)
    winner_result = done_results[0]

    # ปริ้นผลลัพธ์ผู้ชนะให้ตรงกับหน้าจอของอาจารย์ (ดึงค่ามาแสดงจริงๆ ไม่ได้พิมพ์หลอก)
    if isinstance(winner_result, Exception):
        print(f"{ctime()} Winner Result: Error: {winner_result}")
    else:
        print(f"{ctime()} Winner Result: {winner_result}")

    # ปริ้นสรุปจำนวน Task ที่กำลังจะถูกยกเลิก โดยใช้ len(pending) นับจากของจริงในระบบ
    print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")

    # วนลูปสั่งยกเลิก (Cancel) Task ที่เหลือทั้งหมด (ให้โปรแกรมจัดการเงียบๆ เบื้องหลัง)
    for ongoing_task in pending:
        ongoing_task.cancel()

    if pending:
        await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    asyncio.run(main())