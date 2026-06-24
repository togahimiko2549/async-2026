import asyncio
import httpx

#ฟังชั่นที่ตั้งชื่อผู้ใช้แบบ asyncio ผ่าน httpx
async def fetch_username(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()["name"]
    
async def main():
    #รันแบบ asynchronous ขนาบกัน (ยิงพร้อมกัน 2 request)
    name1, name2 = await asyncio.gather(fetch_username(1), fetch_username(2))
    print(f"User 1: {name1}, User 2: {name2}")

if __name__ == "__main__":
    asyncio.run(main())
