import streamlit as st
import pandas as pd
import random

def show_model_development():
    st.markdown("""<h1 style='font-family: Athiti; text-align: center;'>Algorithm & Model Development</h1>""", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Data Preprocessing",
        "Detail of DataSet (Classical)",
        "Detail of DataSet (NN)",
        "Development Model",
        "Theory of ML Model"
    ])
    
    with tab1:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Data Preprocessing📑
    </h4>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    แหล่งที่มาของข้อมูล (Data Preprocessing)
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       ข้อมูลที่เราใช้ในการวิเคราะห์และฝึกโมเดล Machine Learning ในโปรเจกต์นี้เป็นชุดข้อมูลเกี่ยวกับ
                    <span style="background-color: #990000;">ขยะขวดพลาสติกในประเทศไทย 
                    ตั้งแต่ปี 2000 ถึง 2024</span>
                    ซึ่งครอบคลุมทั้งปริมาณขยะที่เกิดขึ้น
                    อัตราการรีไซเคิล และปัจจัยอื่น ๆ ที่เกี่ยวข้อง เช่น จำนวนประชากรและนโยบายของรัฐบาล 
                    แต่เนื่องจากเราไม่มีชุดข้อมูลจริงที่ครบถ้วนสมบูรณ์ในทุกมิติ เราจึงสร้างชุดข้อมูลสมมติ (synthetic dataset) ขึ้นมาโดยอิงจากข้อมูลและแนวโน้มที่เชื่อถือได้จากแหล่งต่าง ๆ 
                    เพื่อให้เหมาะสมกับการทดลองและพัฒนาโมเดล
    </p>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    แนวคิดของข้อมูล    
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - กรมควบคุมมลพิษ (Pollution Control Department) รายงานว่าประเทศไทยสร้างขยะพลาสติกประมาณ 2 ล้านตันต่อปี และขวดพลาสติกเป็นส่วนสำคัญของขยะประเภทนี้ <br>
                    - Greenpeace Thailand ที่ระบุถึงปัญหาขยะพลาสติกแบบใช้ครั้งเดียวทิ้ง (Single-use Plastics) ซึ่งรวมถึงขวดน้ำด้วย <br>
                    - ธนาคารโลก (World Bank) ที่ให้ข้อมูลประชากรไทยเริ่มต้นที่ 62 ล้านคนในปี 2000 และเติบโตช้าลงในช่วงหลัง <br>
    </p>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    การสร้างและปรับแต่ง DataSet
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    เพื่อให้ครอบคลุมของข้อมูลและมีความละเอียด โดยใช้ Code Gen ข้อมูลออกมาให้มีความหลากหลายในการ ฝึกฝน Model Machine Learning <br>
                    ปริมาณขยะขวดพลาสติก: เพิ่มขึ้น 2-5% ต่อปีตามแนวโน้มการบริโภคที่สูงขึ้น และเพิ่มความผันผวนเล็กน้อย (±20 ล้านขวด) เพื่อจำลองความไม่แน่นอนในชีวิตจริง <br>
                    อัตราการรีไซเคิล: เติบโตช้ากว่า (1-3% ต่อปี) แต่ได้รับอิทธิพลจากนโยบาย เช่น เพิ่มขึ้นมากขึ้นในช่วงที่มีนโยบายเพิ่มมากขึ้น (2020-2024) <br>
                    ประชากร: ปรับเพิ่ม 0.1-0.3% ต่อปีตามข้อมูลจริง <br>
                    แนวโน้มการรีไซเคิล: ออกแบบเป็นคะแนน 0-100 โดยเริ่มจาก 20 และเพิ่มขึ้นตามเวลาและนโยบาย เพื่อสะท้อนการรับรู้ของสังคม <br>
    </p>""", unsafe_allow_html=True)
        code = '''import pandas as pd
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
print(" Missing Values in Each Column:")
print(df.isnull().sum())'''
        st.code(code, language="python", line_numbers=True, wrap_lines=False, height=700)
        st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Athiti:wght@400&display=swap');
        .about-container {
            text-align: center;
            font-family: 'Athiti', sans-serif !important;
            font-size: 16px;
            font-weight: 400;
            line-height: 1.6;
            color: #ffffff;
        }
        .about-container h5 {
            font-family: 'Athiti', sans-serif !important;
            font-size: 20px;
            color: #ffffff;
            margin: 0;
        }
        .stApp {
            background-color: #121212;
        }
    </style>
    <div class="about-container">
        <h5>ตัวอย่าง Code Python ในการสร้าง DataSet</h5>
    </div>
""", unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Detail of DataSet (Classical)🧸
    </h4>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    ข้อมูลในไฟล์ CSV
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - <span style="font-weight: bold;">Date</span> จะเป็นการระบุ ปี และเดือนของข้อมูล <br>
                    - <span style="font-weight: bold;">Plastic Bottle Waste Generated</span> เป็นการบ่งบอกขยะขวดที่พลาสติกที่เกิดขึ้นในแต่ละปีและเดือน <br>
                    - <span style="font-weight: bold;">Recycling Rate</span> อัตราการรีไซเคิลของขยะ <br>
                    - <span style="font-weight: bold;">Recycling Percentage</span> อัตราการรีไซเคิลแบบเปอร์เซ็นต์ <br>
                    - <span style="font-weight: bold;">Recycling Trend</span> เทรนด์การรีไซเคิลของขยะ <br>
                    - <span style="font-weight: bold;">Population</span> ความนิยมในการรีไซเคิล <br>
                    - <span style="font-weight: bold;">Recycling Policy Level</span> นโยบายการรีไซเคิลแต่ละปีและเดือน <br>
    </p>""", unsafe_allow_html=True)
        df = pd.read_csv(r"dataset/thai_plastic_bottle_waste_monthly_dataset_with_missing.csv")
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    ตารางในไฟล์ CSV
    </h5>""", unsafe_allow_html=True)
        st.dataframe(df)
        st.markdown("""<p style='font-family: Athiti; text-align: center;'>
                    <span style="font-weight: bold;">โดยในข้อมูลจากตารางของไฟล์ CSV นั้นจะพบว่ามีการหายไปของข้อมูลบางช่อง</span> <br> <br>
    </p>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    Feature Engineering
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    <span style="font-weight: bold;">1. YEAR:</span> ปีจาก DATE - ดูแนวโน้มรายปี <br>
                    <span style="font-weight: bold;">2. MONTH:</span> เดือนจาก DATE - ดูความแตกต่างรายเดือน <br>
                    <span style="font-weight: bold;">3. WASTE_PER_CAPITA:</span> ขยะ (ล้านขวด) ÷ ประชากร (ล้านคน) - ขยะต่อคน <br>
                    <span style="font-weight: bold;">4. RECYCLING_PER_CAPITA:</span> รีไซเคิล (ล้านขวด) ÷ ประชากร (ล้านคน) - รีไซเคิลต่อคน <br>
                    <span style="font-weight: bold;">5. UNRECYCLED_WASTE:</span> ขยะทั้งหมด - รีไซเคิล - ขยะที่เหลือ <br>
                    <span style="font-weight: bold;">6. RECYCLING_PERCENTAGE_CHANGE:</span> % รีไซเคิลเปลี่ยนจากเดือนก่อน - วัดการเปลี่ยนแปลง <br>
                    <span style="font-weight: bold;">7. RECYCLING_TREND_CHANGE:</span> แนวโน้ม (0-100) เปลี่ยนจากเดือนก่อน - วัดการพัฒนา <br>
                    <span style="font-weight: bold;">8. POLICY_LEVEL_CATEGORY:</span> 0-3 เป็นชื่อ (NO POLICY, BASIC, MODERATE, ADVANCED) - อ่านง่าย <br>
                    <span style="font-weight: bold;">9. CALCULATED_RECYCLING_PERCENTAGE:</span> รีไซเคิล ÷ ขยะทั้งหมด × 100 - เติมข้อมูลที่หาย <br><br>
</p>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    การแก้ไขให้ Missing Data มีความสมบูรณ์ให้กับการ Train Model
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    <span style="font-weight: bold;">ทำไมต้องใช้ค่าเฉลี่ย?</span>
                    <span style="font-weight: bold;">เรียบง่ายและรวดเร็ว:</span> ไม่ต้องคำนวณอะไรซับซ้อน แค่หาค่าเฉลี่ยของคอลัมน์นั้น ๆ แล้วใส่ข้อมูลทดแทนเข้าไป <br>
                    <span style="font-weight: bold;">สมเหตุสมผล:</span> ถ้าไม่มีข้อมูลในเดือนนั้น ค่าเฉลี่ยจากเดือนอื่น ๆ ก็เป็นตัวเลขที่ใกล้เคียงความเป็นจริงได้ดีในระดับหนึ่ง <br>
                    <span style="font-weight: bold;">เหมาะกับข้อมูลที่ไม่ผันผวนมาก:</span> ถ้าข้อมูลของเราไม่มีอะไรหวือหวาเกินไป ค่าเฉลี่ยก็ช่วยให้ภาพรวมยังดูสมดุล <br> <br>
    </p>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
                    ข้อมูลที่ไม่สมบูรณ์ดีอย่างไร?
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    <span style="font-weight: bold;">สะท้อนความเป็นจริงของการเก็บข้อมูล: </span>การขาดหายของข้อมูลอาจบ่งบอกถึงข้อจำกัดในกระบวนการเก็บข้อมูล เช่น ความไม่สม่ำเสมอของการรายงาน หรือเหตุการณ์ที่ทำให้ข้อมูลไม่ถูกบันทึก (เช่น ภัยธรรมชาติ) ซึ่งช่วยให้เข้าใจบริบทของข้อมูลได้ดีขึ้น <br>
                    <span style="font-weight: bold;">เป็นตัวชี้วัดความน่าเชื่อถือ: </span>จำนวนและตำแหน่งของ missing values สามารถใช้ประเมินคุณภาพของชุดข้อมูล และช่วยกำหนดวิธีการวิเคราะห์ที่เหมาะสม <br>
                    <span style="font-weight: bold;">กระตุ้นการพัฒนาเทคนิคการจัดการ: </span>ข้อมูลที่ไม่สมบูรณ์ผลักดันให้เกิดการพัฒนาวิธีการเติมข้อมูล (imputation) หรือการวิเคราะห์ที่ทนทานต่อข้อมูลที่ขาดหาย (robust analysis) ซึ่งเป็นประโยชน์ต่อศาสตร์ข้อมูลในระยะยาว <br>
    </p>""", unsafe_allow_html=True)

    with tab3:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Detail of DataSet (NN)👩‍💻
    </h4>""", unsafe_allow_html=True)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - <span style="font-weight: bold;">Comment</span> กาารระบุข้อมูลของข้อความ <br>
                    - <span style="font-weight: bold;">Sentiment</span> เป็นการบ่งบอกอารมณ์ของข้อความ <br>
    </p>""", unsafe_allow_html=True)
        df = pd.read_csv(r"dataset/YoutubeCommentsDataSet.csv")
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    ตารางในไฟล์ CSV
    </h5>""", unsafe_allow_html=True)
        st.dataframe(df)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    Code การพัฒนาโมเดล Neural Network
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>1.นำเข้าไลบรารีที่จำเป็นทั้งหมด เช่น pandas สำหรับจัดการข้อมูล, torch สำหรับการสร้างโมเดล
    </h5>""", unsafe_allow_html=True)
        code = '''import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
import joblib
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>2.ข้อความในคอลัมน์ 'Comment' ถูกแปลงเป็นเวกเตอร์ TF-IDF โดยใช้ TfidfVectorizer ซึ่งจำกัดจำนวนคำที่สำคัญที่ใช้ในการสร้างเวกเตอร์. 
                    ส่วนของ Label ในคอลัมน์ 'Sentiment' ถูกแปลงเป็นตัวเลขเพื่อใช้ในการฝึกโมเดล โดย LabelEncoder จะแปลงค่าของ 'negative', 'neutral', 'positive' 
                    เป็นตัวเลข 0, 1, 2 ตามลำดับ.
    </h5>""", unsafe_allow_html=True)
        code = '''# อ่านข้อมูลจาก CSV และจัดการข้อมูลที่หายไป
df = pd.read_csv('/content/YoutubeCommentsDataSet.csv')
df = df.dropna(subset=['Comment'])
df['Comment'] = df['Comment'].fillna('').astype(str)

# แปลง Labels เป็นตัวเลข
label_encoder = LabelEncoder()
label_encoder.fit(['negative', 'neutral', 'positive'])
labels = label_encoder.transform(df['Sentiment'].values)

# แปลงข้อความเป็นเวกเตอร์ TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X = tfidf.fit_transform(df['Comment'].values).toarray()
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>3.ข้อมูลถูกแบ่งออกเป็นสองชุด: ชุดฝึก (training) และชุดทดสอบ (testing) โดยใช้ train_test_split จาก sklearn. 
                    ชุดฝึกจะใช้ในการฝึกโมเดล ส่วนชุดทดสอบจะใช้สำหรับการประเมินผลของโมเดลหลังการฝึก.
    </h5>""", unsafe_allow_html=True)

        code = '''# แบ่งข้อมูล
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# แปลงข้อมูลเป็น Tensor
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

# สร้าง DataLoader
train_data = TensorDataset(X_train_tensor, y_train_tensor)
test_data = TensorDataset(X_test_tensor, y_test_tensor)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)
test_loader = DataLoader(test_data, batch_size=32)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>4.สร้างโมเดล Neural Network ด้วย PyTorch โดยใช้ architecture ที่ประกอบด้วย 2 เลเยอร์ที่เป็น Fully Connected Layers. 
                    เลเยอร์แรกมี 128 นิวรอนและเชื่อมต่อกับอินพุตที่มีขนาด 5000. เลเยอร์ที่สองมี 3 นิวรอน ซึ่งจะส่งออก 3 
                    คลาสที่แสดงถึงความคิดเห็นในเชิงลบ, กลาง, และบวก.
    </h5>""", unsafe_allow_html=True)
        
        code = '''# สร้างโมเดล
class SentimentNN(nn.Module):
    def __init__(self):
        super(SentimentNN, self).__init__()
        self.fc1 = nn.Linear(5000, 128)
        self.fc2 = nn.Linear(128, 3)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return self.softmax(x)

model = SentimentNN()
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>5.โมเดลนี้ใช้ CrossEntropyLoss เป็น Loss Function สำหรับการคำนวณค่าผิดพลาดระหว่างค่าที่คาดการณ์และค่าจริง. 
                    ส่วน Adam optimizer ถูกใช้ในการปรับค่าพารามิเตอร์ของโมเดล.
    </h5>""", unsafe_allow_html=True)
        
        code = '''# Loss function และ Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>6.โมเดลจะถูกฝึกด้วยข้อมูลที่แบ่งไว้ในชุดฝึก. ในแต่ละรอบการฝึก (epoch), โมเดลจะคำนวณค่า Loss จากข้อมูลที่ป้อนเข้าไปและปรับค่าพารามิเตอร์โดยใช้ optimizer. 
                    กระบวนการนี้จะดำเนินไปจนถึงจำนวน epoch ที่กำหนด.
    </h5>""", unsafe_allow_html=True)
        
        code = '''# ฝึกโมเดล
num_epochs = 60
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {running_loss/len(train_loader)}')
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>7.หลังจากการฝึกเสร็จสิ้น, โมเดลจะถูกทดสอบด้วยชุดทดสอบที่ไม่ได้ใช้ในการฝึก. เราคำนวณอัตราความถูกต้อง (accuracy) 
                    โดยการเปรียบเทียบผลลัพธ์ที่คาดการณ์กับค่าจริง.
    </h5>""", unsafe_allow_html=True)
        
        code = '''# ประเมินโมเดล
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy: {100 * correct / total}%')
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>8.เมื่อโมเดลได้รับการฝึกเสร็จสมบูรณ์, โมเดลและตัวแปลงข้อความ (TF-IDF vectorizer และ Label encoder) 
                    จะถูกบันทึกลงไฟล์เพื่อใช้ในอนาคต. 
                    การบันทึกนี้ช่วยให้เราโหลดโมเดลและตัวแปลงที่ฝึกแล้วมาใช้ในการทำนายในขั้นตอนถัดไปโดยไม่ต้องฝึกใหม่.
    </h5>""", unsafe_allow_html=True)
        
        code = '''# บันทึกโมเดลและตัวแปลงข้อความ
joblib.dump(model, 'sentiment_model.pkl')
torch.save(model.state_dict(), 'sentiment_model.pth')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Model and Vectorizer saved successfully!")
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.image("img/Accuracy Model/W&B Chart 3_9_2025, 8_53_00 PM.png", caption="Accuracy Model Neural Network")

    with tab4:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Development Model
    </h4>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    ขั้นตอนการพัฒนาโมเดล Machine Learning
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti;'>
    หลังจากที่เราได้เตรียมข้อมูลของ Model Machine Learning สำเร็จ
    </h5>""", unsafe_allow_html=True)
        st.markdown("""<h5 style='font-family: Athiti;'>
    1.ก็ทำการเริ่มต้นด้วยการโหลดข้อมูลขยะพลาสติกรายเดือนจากไฟล์ CSV เข้ามาในตัวแปร เพื่อเตรียมไว้สำหรับการวิเคราะห์ต่อไป
    </h5>""", unsafe_allow_html=True)
        code = '''df = pd.read_csv("thai_plastic_bottle_waste_monthly_dataset_with_missing.csv")
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>2.โค้ดนี้แยกข้อมูลวันที่ออกเป็นปีและเดือน เพื่อให้สามารถใช้งานแยกส่วนได้ง่ายขึ้นในการวิเคราะห์
    </h5>""", unsafe_allow_html=True)
        code = '''df['Year'] = df['Date'].apply(lambda x: int(x.split('-')[0]))
df['Month'] = df['Date'].apply(lambda x: int(x.split('-')[1]))
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>3.ส่วนนี้สร้างฟีเจอร์ใหม่ เช่น ขยะต่อประชากร หรือการผสมตัวแปรนโยบายและแนวโน้ม เพื่อเพิ่มข้อมูลที่เป็นประโยชน์สำหรับโมเดล
    </h5>""", unsafe_allow_html=True)
        code = '''df['Waste_per_Population'] = df['Plastic Bottle Waste Generated (Million Bottles)'] / df['Population (Million)']
df['Waste_Policy_Interaction'] = df['Plastic Bottle Waste Generated (Million Bottles)'] * df['Recycling Policy Level (0-3)']
df['Trend_Policy_Interaction'] = df['Recycling Trend (0-100)'] * df['Recycling Policy Level (0-3)']
df['Year_Trend'] = df['Year'] * df['Recycling Trend (0-100)'])
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>4.โค้ดนี้กำหนดฟีเจอร์ที่ใช้ในการทำนาย (11 ตัวแปร) และตั้งเป้าหมายเป็นอัตราการรีไซเคิล เพื่อเตรียมข้อมูลสำหรับโมเดล
    </h5>""", unsafe_allow_html=True)
        
        code = '''features = ['Year', 'Month', 'Plastic Bottle Waste Generated (Million Bottles)', 
            'Recycling Percentage (%)', 'Recycling Trend (0-100)', 
            'Population (Million)', 'Recycling Policy Level (0-3)', 
            'Waste_per_Population', 'Waste_Policy_Interaction', 'Trend_Policy_Interaction', 'Year_Trend']
X = df[features]
y = df['Recycling Rate (Million Bottles)']
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>5.ส่วนนี้ใช้เทคนิคเติมข้อมูลที่ขาดหายในฟีเจอร์และเป้าหมาย โดยดูจากข้อมูลใกล้เคียง เพื่อให้ข้อมูลครบถ้วน
    </h5>""", unsafe_allow_html=True)
        code = '''imputer = KNNImputer(n_neighbors=5, weights='distance')
X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=features)
y_imputed = pd.Series(imputer.fit_transform(y.values.reshape(-1, 1)).flatten(), name=y.name)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>6.โค้ดนี้ตรวจสอบและลบแถวที่มีข้อมูลขาดหายเหลืออยู่ออก เพื่อให้แน่ใจว่าข้อมูลสมบูรณ์
    </h5>""", unsafe_allow_html=True)
        code = '''mask = X_imputed.notna().all(axis=1) & y_imputed.notna()
X_imputed = X_imputed[mask]
y_imputed = y_imputed[mask]
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>7.ส่วนนี้กำจัดข้อมูลที่ผิดปกติ (outliers) ออกจากฟีเจอร์และเป้าหมาย เพื่อให้ข้อมูลสะอาดและน่าเชื่อถือมากขึ้น
    </h5>""", unsafe_allow_html=True)
        code = '''def remove_outliers(df_col):
    z_scores = (df_col - df_col.mean()) / df_col.std()
    return df_col[abs(z_scores) < 3]

for col in X_imputed.columns:
    X_imputed[col] = remove_outliers(X_imputed[col])
y_imputed = remove_outliers(y_imputed)

mask = X_imputed.notna().all(axis=1) & y_imputed.notna()
X_imputed = X_imputed[mask]
y_imputed = y_imputed[mask]
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>8.โค้ดนี้แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบในสัดส่วน 80:20 เพื่อใช้ฝึกโมเดลและทดสอบผล
    </h5>""", unsafe_allow_html=True)
        code = '''X_train, X_test, y_train, y_test = train_test_split(X_imputed, y_imputed, test_size=0.2, random_state=42)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>9.ส่วนนี้ปรับสเกลข้อมูลให้อยู่ในระดับเดียวกัน เพื่อให้โมเดลทำงานได้ดีขึ้น
    </h5>""", unsafe_allow_html=True)
        code = '''scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)

        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>SVR Model
    </h5>""", unsafe_allow_html=True)
        code = '''svr = SVR(kernel='rbf')
param_grid_svr = {'C': [50, 100, 200], 'epsilon': [0.01, 0.1], 'gamma': ['scale', 0.01, 0.1]}
grid_search_svr = GridSearchCV(svr, param_grid_svr, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_svr.fit(X_train_scaled, y_train)
best_svr = grid_search_svr.best_estimator_
y_pred_svr = best_svr.predict(X_test_scaled)
svr_mse = mean_squared_error(y_test, y_pred_svr)
svr_r2 = r2_score(y_test, y_pred_svr)
print("SVR - MSE:", svr_mse, "R²:", svr_r2)
with open('svr_model_new.pkl', 'wb') as f:
    pickle.dump(best_svr, f)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       โค้ดนี้พัฒนาโมเดล 
                    <span style="background-color: #990000;">SVR (Support Vector Regression)</span>
                    โดยใช้เคอร์เนลแบบ rbf ซึ่งเหมาะกับข้อมูลที่ไม่เป็นเส้นตรง มีการกำหนดตัวเลือกพารามิเตอร์ 
                    เช่น C (ควบคุมการลงโทษความผิดพลาด), epsilon (กำหนดขอบเขตความคลาดเคลื่อนที่ยอมรับได้), 
                    และ gamma (ควบคุมความโค้งของเส้นแบ่ง) จากนั้นใช้ GridSearchCV ค้นหาชุดพารามิเตอร์ที่ดีที่สุดด้วยการแบ่งข้อมูลฝึกเป็น 5 ส่วน (5-fold cross-validation) 
                    เพื่อลดความคลาดเคลื่อน (MSE) หลังจากฝึกโมเดลด้วยข้อมูลฝึกที่ปรับสเกลแล้ว เลือกโมเดลที่ดีที่สุด ทำนายผลกับข้อมูลทดสอบ วัดผลด้วย MSE (ความคลาดเคลื่อนเฉลี่ย) 
                    และ R² (ความสามารถในการอธิบายข้อมูล) สุดท้ายบันทึกโมเดลลงไฟล์เพื่อใช้งานต่อไป
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>Decision Tree Regressor
    </h5>""", unsafe_allow_html=True)
        code = '''dt = DecisionTreeRegressor(random_state=42)
param_grid_dt = {'max_depth': [5, 7, 10], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4]}
grid_search_dt = GridSearchCV(dt, param_grid_dt, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_dt.fit(X_train_scaled, y_train)
best_dt = grid_search_dt.best_estimator_
y_pred_dt = best_dt.predict(X_test_scaled)
dt_mse = mean_squared_error(y_test, y_pred_dt)
dt_r2 = r2_score(y_test, y_pred_dt)
print("Decision Tree - MSE:", dt_mse, "R²:", dt_r2)
with open('dt_model_new.pkl', 'wb') as f:
    pickle.dump(best_dt, f)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       โค้ดนี้พัฒนาโมเดล 
                    <span style="background-color: #990000;">Decision Tree Regressor</span>
                    ซึ่งเป็นโมเดลที่ตัดสินใจโดยแบ่งข้อมูลเป็นกิ่งเหมือนต้นไม้ โดยตั้งค่า random_state 
                    เพื่อให้ผลลัพธ์สม่ำเสมอ กำหนดพารามิเตอร์ เช่น max_depth (ความลึกสูงสุดของต้นไม้ เพื่อควบคุมความซับซ้อน), 
                    min_samples_split (จำนวนตัวอย่างขั้นต่ำที่ต้องมีก่อนแยกกิ่ง), และ min_samples_leaf (จำนวนตัวอย่างขั้นต่ำในใบ) 
                    ใช้ GridSearchCV ค้นหาค่าที่ดีที่สุดด้วยการทดสอบ 5-fold cross-validation เพื่อลด MSE หลังจากฝึกโมเดลด้วยข้อมูลฝึก 
                    เลือกโมเดลที่เหมาะสม ทำนายผลกับข้อมูลทดสอบ วัดประสิทธิภาพด้วย MSE และ R² แล้วบันทึกโมเดลลงไฟล์สำหรับใช้ในอนาคต
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>KNeighborsRegressor (KNN)
    </h5>""", unsafe_allow_html=True)
        code = '''knn = KNeighborsRegressor()
param_grid_knn = {'n_neighbors': [3, 5, 7], 'weights': ['uniform', 'distance'], 'p': [1, 2]}
grid_search_knn = GridSearchCV(knn, param_grid_knn, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_knn.fit(X_train_scaled, y_train)
best_knn = grid_search_knn.best_estimator_
y_pred_knn = best_knn.predict(X_test_scaled)
knn_mse = mean_squared_error(y_test, y_pred_knn)
knn_r2 = r2_score(y_test, y_pred_knn)
print("KNN - MSE:", knn_mse, "R²:", knn_r2)
with open('knn_model_new.pkl', 'wb') as f:
    pickle.dump(best_knn, f)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       โค้ดนี้พัฒนาโมเดล 
                    <span style="background-color: #990000;">KNeighborsRegressor (KNN)</span>
                    ซึ่งทำนายโดยดูข้อมูลที่ใกล้เคียงที่สุด กำหนดพารามิเตอร์ เช่น n_neighbors (จำนวนเพื่อนบ้านที่ใช้ทำนาย), 
                    weights (วิธีถ่วงน้ำหนักระหว่างแบบเท่ากันหรือตามระยะห่าง), และ p (ระยะห่างแบบ Manhattan หรือ Euclidean) 
                    ใช้ GridSearchCV หาค่าที่ดีที่สุดด้วย 5-fold cross-validation เพื่อลด MSE ฝึกโมเดลด้วยข้อมูลฝึกที่ปรับสเกลแล้ว 
                    เลือกโมเดลที่ดีที่สุด ทำนายผลกับข้อมูลทดสอบ วัดผลด้วย MSE และ R² สุดท้ายบันทึกโมเดลลงไฟล์เพื่อใช้งานต่อ
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>Random Forest
    </h5>""", unsafe_allow_html=True)
        code = '''rf = RandomForestRegressor(random_state=42)
param_grid_rf = {'n_estimators': [100, 200], 'max_depth': [10, 15, 20], 'min_samples_split': [2, 5]}
grid_search_rf = GridSearchCV(rf, param_grid_rf, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_rf.fit(X_train_scaled, y_train)
best_rf = grid_search_rf.best_estimator_
y_pred_rf = best_rf.predict(X_test_scaled)
rf_mse = mean_squared_error(y_test, y_pred_rf)
rf_r2 = r2_score(y_test, y_pred_rf)
print("Random Forest - MSE:", rf_mse, "R²:", rf_r2)
with open('rf_model_new.pkl', 'wb') as f:
    pickle.dump(best_rf, f)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       โค้ดนี้พัฒนาโมเดล 
                    <span style="background-color: #990000;">Random Forest Regressor</span>
                    ซึ่งรวมหลาย ๆ Decision Tree เพื่อเพิ่มความแม่นยำ ตั้งค่า random_state 
                    เพื่อผลลัพธ์ที่คงที่ กำหนดพารามิเตอร์ เช่น n_estimators (จำนวนต้นไม้), max_depth (ความลึกสูงสุด)
                    , และ min_samples_split (จำนวนตัวอย่างขั้นต่ำก่อนแยก) ใช้ GridSearchCV ค้นหาค่าที่ดีที่สุดด้วย 5-fold cross-validation 
                    เพื่อลด MSE ฝึกโมเดลด้วยข้อมูลฝึก เลือกโมเดลที่ดีที่สุด ทำนายผล วัดประสิทธิภาพด้วย MSE และ R² แล้วบันทึกโมเดลลงไฟล์
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti;'>
    <br>SVR Linear
    </h5>""", unsafe_allow_html=True)
        code = '''svm_reg = SVR(kernel='linear')
param_grid_svm = {'C': [10, 50, 100], 'epsilon': [0.01, 0.1, 0.5]}
grid_search_svm = GridSearchCV(svm_reg, param_grid_svm, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid_search_svm.fit(X_train_scaled, y_train)
best_svm = grid_search_svm.best_estimator_
y_pred_svm = best_svm.predict(X_test_scaled)
svm_mse = mean_squared_error(y_test, y_pred_svm)
svm_r2 = r2_score(y_test, y_pred_svm)
print("SVM Linear - MSE:", svm_mse, "R²:", svm_r2)
with open('svm_linear_model_new.pkl', 'wb') as f:
    pickle.dump(best_svm, f)
'''
        st.code(code, language="python", line_numbers=False, wrap_lines=False)
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       โค้ดนี้พัฒนาโมเดล 
                    <span style="background-color: #990000;">SVR ด้วยเคอร์เนล linear</span>
                    ซึ่งเหมาะกับข้อมูลที่มีความสัมพันธ์แบบเส้นตรง กำหนดพารามิเตอร์ เช่น C (ควบคุมความเข้มงวด) 
                    และ epsilon (ขอบเขตความคลาดเคลื่อน) ใช้ GridSearchCV หาค่าที่ดีที่สุดด้วย 5-fold cross-validation 
                    เพื่อลด MSE ฝึกโมเดลด้วยข้อมูลฝึก เลือกโมเดลที่เหมาะสม ทำนายผลกับข้อมูลทดสอบ วัดผลด้วย MSE และ R² สุดท้ายบันทึกโมเดลลงไฟล์
    </p>""", unsafe_allow_html=True)
        
        with tab5:
            st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Theory of ML Model📑
    </h4>""", unsafe_allow_html=True)
            st.markdown("""<h5 style='font-family: Athiti;'>
    ทฤษฎีของ Model Machine Learning ที่เลือกใช้
    </h5>""", unsafe_allow_html=True)
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    SVR (Support Vector Regression)
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           <span style="background-color: #E22427;">SVR หรือ Support Vector Regression</span>
                        เป็นโมเดลที่เหมือนนักวาดเส้นเก่ง ๆ ที่พยายามลากเส้นโค้งให้ผ่านจุดข้อมูลให้ได้มากที่สุด 
                        เช่น ถ้าจะทำนายอัตราการรีไซเคิลจากปริมาณขยะและนโยบาย มันจะหาเส้นที่ครอบคลุมข้อมูลทั้งหมด โดยมี "ขอบเขต" (เรียกว่า epsilon) 
                        ที่บอกว่า "ผิดนิดหน่อยไม่เป็นไร" ถ้าข้อมูลซับซ้อน เช่น ขยะเยอะขึ้นแต่รีไซเคิลไม่ตาม SVR จะใช้เคล็ดลับที่เรียกว่าเคอร์เนล (เช่น rbf) 
                        เพื่อเปลี่ยนข้อมูลให้อยู่ในรูปแบบที่จัดการง่ายขึ้น แล้วหาเส้นโค้งที่เหมาะสมที่สุด มันเก่งเรื่องจับความสัมพันธ์ที่ไม่เป็นเส้นตรง และเน้นจุดสำคัญ (support vectors) ที่ช่วยกำหนดเส้นนั้น
    </p>""", unsafe_allow_html=True)
            st.image("img/Illustration-of-the-Machine-Learning-ML-regression-models-A-SVR-example-of-a.png",caption="SVR")

            st.markdown("""<h5 style='font-family: Athiti;'>
    Decision Tree Regressor
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           <span style="background-color: #E22427;">Decision Tree Regressor</span>
                        เหมือนต้นไม้ที่ช่วยตัดสินใจ โดยเริ่มจากคำถามง่าย ๆ 
                        เช่น "ปริมาณขยะมากกว่า 10 ล้านขวดไหม?" หรือ "นโยบายรีไซเคิลเข้มงวดแค่ไหน?" 
                        แล้วแตกกิ่งออกไปตามคำตอบ เช่น ถ้าขยะเยอะก็ไปทางหนึ่ง ถ้าน้อยก็ไปอีกทาง จนถึง "ใบ" สุดท้ายที่ให้คำตอบเป็นตัวเลข 
                        เช่น อัตราการรีไซเคิล 5 ล้านขวด โมเดลนี้แบ่งข้อมูลออกเป็นกลุ่มย่อย ๆ โดยดูว่ากลุ่มไหนใกล้เคียงกันมากที่สุด แล้วคำนวณค่าเฉลี่ยในแต่ละกลุ่ม 
                        มันเข้าใจง่าย แต่ถ้าต้นไม้ใหญ่เกินไปอาจจำข้อมูลเกินจำเป็น (overfitting) เลยต้องกำหนดความลึกหรือขนาดให้พอดี
    </p>""", unsafe_allow_html=True)
            st.image("img/DT.png",caption="Decision Tree Regressor")
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    KNeighborsRegressor (KNN)
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           <span style="background-color: #E22427;">KNN หรือ KNeighborsRegressor</span>
                        เป็นโมเดลที่ใช้ไอเดีย "เพื่อนบ้านใกล้เคียง" มาช่วยทำนาย ถ้าจะเดาอัตราการรีไซเคิล 
                        มันจะดูข้อมูลในอดีตที่คล้ายกับสถานการณ์ปัจจุบัน เช่น "เดือนนี้ขยะ 12 ล้านขวด นโยบายระดับ 2 มีอะไรใกล้เคียงบ้าง?" 
                        แล้วเลือก "เพื่อนบ้าน" ที่ใกล้ที่สุด (เช่น 3 หรือ 5 เดือนที่คล้ายกัน) มาคำนวณค่าเฉลี่ยของอัตราการรีไซเคิลจากข้อมูลเหล่านั้น KNN 
                        ไม่ได้สร้างโมเดลซับซ้อน แค่จำข้อมูลเก่า ๆ ไว้ แล้วดูว่าอะไรใกล้เคียงที่สุด ฉะนั้นถ้าข้อมูลดีและครบ มันจะเดาได้แม่น แต่ถ้าข้อมูลแตกต่างกันมาก อาจสับสนได้
    </p>""", unsafe_allow_html=True)
            st.image("img/KNN.png",caption="KNeighborsRegressor")
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    Random Forest Regressor
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           <span style="background-color: #E22427;">Random Forest Regressor</span> 
                        เหมือนป่าที่เต็มไปด้วยต้นไม้ตัดสินใจ (Decision Trees) หลายสิบหรือหลายร้อยต้น 
                        แต่ละต้นจะเดาอัตราการรีไซเคิลจากมุมมองของตัวเอง เช่น ต้นหนึ่งดูขยะ ต้นหนึ่งดูนโยบาย อีกต้นดูแนวโน้มรีไซเคิล แล้ว Random Forest 
                        จะรวบรวมคำทำนายจากทุกต้นมาเฉลี่ยกัน เพื่อให้ได้ผลลัพธ์ที่น่าเชื่อถือ มันแก้ปัญหาที่ Decision Tree ตัวเดียวอาจเดาผิดพลาดหรือจำเกินไป 
                        โดยการ "โหวต" จากหลายต้นไม้ ทำให้ทนทานต่อข้อมูลแปลก ๆ และแม่นยำขึ้น แต่วิธีนี้ใช้เวลาคิดนานกว่านิดหน่อย
    </p>""", unsafe_allow_html=True)
            st.image("img/RDF.png",caption="Random Forest Regressor")
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    SVR Linear
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           <span style="background-color: #E22427;">SVR Linear</span> 
                        เป็นน้องของ SVR แต่แทนที่จะใช้เส้นโค้ง มันใช้เส้นตรงในการทำนาย เหมาะกับข้อมูลที่ความสัมพันธ์ไม่ซับซ้อนมาก 
                        เช่น ถ้าปริมาณขยะเพิ่มขึ้นแล้วอัตราการรีไซเคิลเพิ่มตามแบบเรียบง่าย SVR Linear จะลากเส้นตรงผ่านข้อมูล โดยมีขอบเขต (epsilon) 
                        ที่ยอมให้ผิดพลาดได้บ้าง และใช้พารามิเตอร์ C เพื่อควบคุมว่าเส้นจะยืดหยุ่นแค่ไหน มันเร็วกว่า SVR แบบ rbf เพราะไม่ต้องเปลี่ยนข้อมูลไปมิติสูง 
                        แต่อาจไม่เก่งกับข้อมูลที่ซับซ้อนหรือไม่เป็นเส้นตรง
    </p>""", unsafe_allow_html=True)
            st.image("img/SVRL.png",caption="SVR Linear")

            st.markdown("""<h5 style='font-family: Athiti;'>
    <br>Metrics การวัดประสิทธิของโมเดล Machine Learning
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                           การวัดประสิทธิภาพของโมเดล Machine Learning เป็นขั้นตอนสำคัญที่ช่วยให้
                        เราประเมินความแม่นยำและความน่าเชื่อถือของการทำนายได้ ในโปรเจกต์นี้ เราได้นำ 
                        Metrics มาใช้ในการประเมินโมเดลแต่ละตัว ดังนี้ <br> 
                        <span style="font-weight: bold;">MAE (Mean Absolute Error)</span> <br>
                        <span style="font-weight: bold;">RMSE (Root Mean Squared Error)</span> <br>
                        <span style="font-weight: bold;">R² (R-Squared)</span> <br>
                        <span style="font-weight: bold;">MAPE (Mean Absolute Percentage Error)</span> <br>
                        <span style="font-weight: bold;">Accuracy (%)</span> <br> <br>
    </p>""", unsafe_allow_html=True)
            st.markdown("""<h5 style='font-family: Athiti;'>
    MAE (Mean Absolute Error)
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       MAE คือ ค่าความคลาดเคลื่อนเฉลี่ยของการทำนาย โดยไม่สนใจเครื่องหมายบวกหรือลบ
                    บางครั้งไม่อยากให้มีที่ค่าคลาดเคลื่อนที่สูง ๆ มีน้ำหนักมากเกินไป  ดังนั้นจึงใช้ 
                    ค่าเฉลี่ยของค่าความผิดพลาดแบบสัมบูรณ์(Absolute) แทน
    </p>""", unsafe_allow_html=True)
            st.latex(r'''
                    MAE = \frac{1}{n}  Σ|y_i – ŷ_i|
                    ''')
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    RMSE (Root Mean Squared Error)
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       RMSE คือ ค่ารากที่สองของค่าเฉลี่ยของความคลาดเคลื่อนที่ยกกำลังสอง 
                    ใช้เพื่อวัดว่าค่าที่โมเดลทำนายแตกต่างจากค่าจริงมากน้อยเพียงใด
                    ถ้าเราบวกลบค่าคลาดเคลื่อนตรง ๆ อาจมีบางค่าหักล้างต่อกันได้ ดังนั้นจึงยกกำลังสองก่อนเฉลี่ย 
                    แต่พอยกกำลังสอง หน่วยของค่าจะเปลี่ยนไปจากเดิม 
                    ดังนั้นจึงจำเป็นต้อง ถอดรูทกลับ เพื่อให้หน่วยตรงกับค่าจริง ๆ
    </p>""", unsafe_allow_html=True)
            st.latex(r'''
                    \text{RMSE} = \sqrt{\frac{1}{n}  \sum_{i=1}^{n} (\text{prediction}_i - \text{actual}_i)^2}
                    ''')
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    R² (R-Squared)
    </h5>""", unsafe_allow_html=True)
            
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       R² หรือ Coefficient of Determination เป็นค่าที่บ่งบอกว่าโมเดลอธิบายความแปรปรวนของข้อมูลได้ดีแค่ไหน
                    บางครั้งเราต้องการดูว่าโมเดลของเรา ดีกว่าการเดาแบบสุ่มไม หรือ อธิบายความสัมพันธ์ของตัวแปรได้ดีแค่ไหน
    </p>""", unsafe_allow_html=True)
            st.latex(r'''
                    R^2 = 1 - \frac{\sum_{i=1}^{n} (\text{actual}_i - \text{prediction}_i)^2}{\sum_{i=1}^{n} (\text{actual}_i - \bar{\text{actual}})^2}
                    ''')
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    MAPE
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       MAPE คือ ค่าคลาดเคลื่อนโดยคิดเป็นเปอร์เซ็นต์ของค่าจริง ทำให้สามารถเปรียบเทียบโมเดลที่มีหน่วยต่างกันได้
                    บางครั้งเราต้องการดูว่าโมเดลพยากรณ์พลาดไปกี่เปอร์เซ็นต์ของค่าจริง 
    </p>""", unsafe_allow_html=True)
            st.latex(r'''
                    \text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{\text{actual}_i - \text{prediction}_i}{\text{actual}_i} \right| \times 100
                    ''')
            
            st.markdown("""<h5 style='font-family: Athiti;'>
    Accuracy
    </h5>""", unsafe_allow_html=True)
            st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                       Accuracy เป็นตัวชี้วัดที่คำนวณจากค่า MAPE เพื่อหาค่าควาแม่นยำของโมเดล
    </p>""", unsafe_allow_html=True)
            st.latex(r'''
                    Accuracy = 100 - MAPE
                    ''')
            
            st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Athiti:wght@400&display=swap');
        .about-container {
            text-align: center;
            font-family: 'Athiti', sans-serif !important;
            font-size: 16px;
            font-weight: 400;
            line-height: 1.6;
            color: #ffffff;
        }
        .about-container h5 {
            font-family: 'Athiti', sans-serif !important;
            font-size: 20px;
            color: #ffffff;
            margin: 0;
        }
        .stApp {
            background-color: #121212;
        }
    </style>
    <div class="about-container">
        <h5>ผลการประเมินประสิทธิภาพของโมเดล</h5>
    </div>
""", unsafe_allow_html=True)
            df = pd.read_csv(r"dataset/model_performance.csv")
            st.dataframe(df)
            st.image("img/Accuracy Model/MAE.png", caption="MAE")
            st.image("img/Accuracy Model/RMSE.png", caption="RMSE")
            st.image("img/Accuracy Model/R2.png", caption="R²")
            st.image("img/Accuracy Model/Accuracy.png", caption="Accuracy")