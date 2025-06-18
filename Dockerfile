# ใช้ base image เป็น python แบบ slim (เล็ก)
FROM python:3.10-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอก requirements.txt เข้ามาก่อน แล้วติดตั้งก่อน เพื่อใช้ layer cache
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์ทั้งหมดเข้ามาใน container
COPY . .

# เปิด port สำหรับ Streamlit
EXPOSE 8501

# คำสั่งให้ container รันเมื่อถูกสั่ง start
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
