import asyncio
import httpx

SERVER_IP = "172.20.56.253"
PORT = "8080"
SERVER_URL = f"http://{SERVER_IP}:{PORT}"

MY_STUDENT_ID = "6710301045"

async def hunt_coupons():
    async with httpx.AsyncClient() as client:
        print(f"[{MY_STUDENT_ID}] Hunting for coupons...")


        for attempt in range (1,6):
            try:
                res = await client.post(
                    f"{SERVER_URL}/claim",
                    json={"student_id": MY_STUDENT_ID},
                    timeout=5.0
                )
                data = res.json()
                status = data.get("status")

                print(f"--time{attempt}:[{status}]->{data.get('message',data.get('claimed_coupon'))}")

                if status in ["limit_reached","out_of_stock"]:
                    break

            except Exception as e:
                print(f"connection error: {e}")

            await asyncio.sleep(0.02)

        print("\nกำลังดึงสรุปคูปองของตัวเอง...")
        try:
            res = await client.get(f"{SERVER_URL}/my-coupons/{MY_STUDENT_ID}")
            if res.status_code == 200:
                summary = res.json()
                total = summary.get("total_claimed_coupons", 0)
                coupons = summary.get("claimed_coupons", [])
                print(f" สรุปผล [{MY_STUDENT_ID}] ได้คูปองทั้งหมด {total} ใบ:->{coupons}")
            else:
                print(f"ดึงข้อมูลไม่สำเร็จ status code: {res.status_code}")

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลส่วนตัว: {e}")


        print("\nกำลังดึงสรุปภาพรวมคูปองทั้งหมดจาก server (/summary)...")
        try:
            res = await client.get(f"{SERVER_URL}/summary")
            if res.status_code == 200:
               summary_all = res.json()
               rem_stock= summary_all.get("remaing_stock", "N/A")
               clamis = summary_all.get("student_claims", [])                    

               print(f"จำนวนคูปองที่เหลือในเซิฟเวอร์: {rem_stock} ใบ")
               print("สรุปผลการ claim ของนักเรียนทั้งหมด:")

               for sid, coupons in clamis.items():
                   print(f"  - {sid} ได้คูปอง: {len(coupons)} ใบ -> {coupons}")

            else:
                print(f"ดึงข้อมูลภาพรวมไม่สำเร็จ status code: {res.status_code}")
        
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการดึงข้อมูลสรุปภาพรวม: {e}")

if __name__ == "__main__":
    asyncio.run(hunt_coupons())
        