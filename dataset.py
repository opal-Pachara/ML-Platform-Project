import pandas as pd
import random

# สร้างข้อมูลรายเดือนในช่วงปี 2000-2024
years = list(range(2000, 2025))
months = list(range(1, 13))
data = []

# ค่าเริ่มต้นสมมติสำหรับเดือนแรกของปี 2000
base_waste = 150  # ล้านขวดต่อเดือน
base_recycle_rate = 30  # ล้านขวดต่อเดือน
base_population = 62  # ล้านคน (ประชากรไทยในปี 2000)

# ระดับนโยบายรีไซเคิล (0 = ไม่มี, 1 = เริ่มต้น, 2 = ปานกลาง, 3 = เข้มข้น)
policy_levels = {2000: 0, 2005: 1, 2010: 1, 2015: 2, 2020: 3}

for year in years:
    # กำหนดระดับนโยบายตามช่วงปี
    policy = 0
    for policy_year in sorted(policy_levels.keys()):
        if year >= policy_year:
            policy = policy_levels[policy_year]
    
    for month in months:
        # อัตราการสร้างขยะขวดพลาสติก (เพิ่มขึ้น 2-5% ต่อปี + ความผันผวน)
        waste_growth = random.uniform(0.02, 0.05) / 12
        plastic_waste = base_waste * (1 + waste_growth) ** ((year - 2000) * 12 + month - 1) + random.uniform(-20, 20)
        plastic_waste = max(0, plastic_waste) if random.random() > 0.1 else None  # 10% โอกาสเป็น None
        
        # อัตราการรีไซเคิล (เพิ่มขึ้น 1-3% ต่อปี + ผลจากนโยบาย + ความผันผวน)
        recycle_increase = (random.uniform(0.01, 0.03) + policy * 0.005) / 12
        recycle_rate = base_recycle_rate * (1 + recycle_increase) ** ((year - 2000) * 12 + month - 1) + random.uniform(-10, 10)
        recycle_rate = max(0, recycle_rate) if random.random() > 0.15 else None  # 15% โอกาสเป็น None
        
        # เปอร์เซ็นต์การรีไซเคิล (คำนวณถ้ามีข้อมูลครบ)
        recycling_percentage = (recycle_rate / plastic_waste * 100) if (plastic_waste is not None and recycle_rate is not None and plastic_waste > 0) else None
        
        # แนวโน้มการรีไซเคิล (เพิ่มขึ้นตามเวลาและนโยบายแต่ไม่เกิน 100)
        recycling_trend = min(100, 20 + ((year - 2000) * 12 + month - 1) * random.uniform(0.1, 0.3) + policy * 5 + random.uniform(-5, 5))
        recycling_trend = recycling_trend if random.random() > 0.1 else None  # 10% โอกาสเป็น None
        
        # จำนวนประชากร (เพิ่มขึ้น 0.1-0.3% ต่อปี)
        pop_growth = random.uniform(0.001, 0.003) / 12
        population = base_population * (1 + pop_growth) ** ((year - 2000) * 12 + month - 1)
        population = population if random.random() > 0.05 else None  # 5% โอกาสเป็น None
        
        # นโยบายไม่ให้ขาดหาย (สมมติว่านโยบายต้องมีครบ)
        policy_value = policy
        
        data.append([f"{year}-{month:02d}", plastic_waste, recycle_rate, recycling_percentage, recycling_trend, population, policy_value])

# สร้าง DataFrame
df = pd.DataFrame(data, columns=[
    "Date", 
    "Plastic Bottle Waste Generated (Million Bottles)", 
    "Recycling Rate (Million Bottles)", 
    "Recycling Percentage (%)", 
    "Recycling Trend (0-100)",
    "Population (Million)",
    "Recycling Policy Level (0-3)"
])

# บันทึกเป็น CSV
df.to_csv("thai_plastic_bottle_waste_monthly_dataset_with_missing.csv", index=False)

# แสดงตัวอย่างข้อมูล 5 แถวแรก
print(df.head())

# แสดงจำนวนข้อมูลที่หายไปในแต่ละคอลัมน์
print("\nMissing Values in Each Column:")
print(df.isnull().sum())