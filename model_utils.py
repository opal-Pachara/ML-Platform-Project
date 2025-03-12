import pickle
import numpy as np
import streamlit as st

def load_model(model_path):
    """โหลดโมเดลจากไฟล์ .pkl"""
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        st.success("โหลดโมเดล Decision Tree สำเร็จ!")
        
        # ตรวจสอบจำนวน feature ที่โมเดลต้องการ (ถ้าเป็น DecisionTreeClassifier)
        try:
            expected_features = model.n_features_in_
            st.info(f"โมเดลนี้ต้องการ {expected_features} features สำหรับการทำนาย")
        except AttributeError:
            st.warning("ไม่สามารถตรวจสอบจำนวน features ที่โมเดลต้องการได้ กรุณาระบุจำนวน features ด้วยตัวเอง")
            expected_features = 4  # ค่าเริ่มต้น (ปรับตามโมเดลของคุณ)
        
        return model, expected_features
    except FileNotFoundError:
        st.error(f"ไม่พบไฟล์ที่: {model_path}")
        return None, None
    except pickle.UnpicklingError:
        st.error("ไฟล์เสียหายหรือไม่ใช่ไฟล์ pickle ที่ถูกต้อง")
        return None, None
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการโหลดโมเดล: {str(e)}")
        return None, None

def predict_with_model(model, input_data, expected_features):
    """ทำนายผลด้วยโมเดล"""
    if not input_data:
        st.warning("กรุณาใส่ข้อมูลก่อนกดทำนาย")
        return
    
    try:
        # แปลงข้อมูลจาก string เป็น list
        data = [float(x) for x in input_data.split(',')]
        
        # ตรวจสอบจำนวน feature
        if len(data) != expected_features:
            st.error(f"โมเดลต้องการ {expected_features} features แต่คุณกรอก {len(data)} ค่า กรุณากรอกให้ครบ")
            return
        
        # แปลงเป็น numpy array
        data_array = np.array(data).reshape(1, -1)
        # ทำนายด้วยโมเดล
        prediction = model.predict(data_array)
        st.success(f"ผลการทำนายจาก Decision Tree: {prediction[0]}")
    except ValueError:
        st.error("กรุณาใส่ข้อมูลในรูปแบบตัวเลขที่ถูกต้อง คั่นด้วย comma")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการทำนาย: {str(e)}")