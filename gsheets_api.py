import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# เชื่อมต่อ Google Sheets
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    try:
        # ตรวจสอบ environment variable ก่อน
        google_sheets_key = os.getenv("GOOGLE_SHEETS_KEY")
        if google_sheets_key:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(google_sheets_key), scope)
        else:
            # ใช้ไฟล์ในเครื่อง
            creds = ServiceAccountCredentials.from_json_keyfile_name("google-sheets-key.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("VisitorLog").sheet1  # ชื่อ Google Sheet ต้องตรงกับที่คุณสร้าง
        return sheet
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

def log_visitor(sheet):
    if sheet is None:
        return 0  # ถ้าเชื่อมต่อไม่ได้ คืนค่า 0
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(datetime.now().timestamp())
        row = [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), st.session_state.session_id]
        sheet.append_row(row)
    data = sheet.get_all_values()
    session_ids = set(row[1] for row in data[1:])  # ข้ามหัวคอลัมน์
    visitor_count = len(session_ids)
    return visitor_count
