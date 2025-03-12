import streamlit as st
import base64

def show_introduction():
    st.markdown("""<h1 style='font-family: Athiti; text-align: center;'>Introduction & Data Set</h1>""", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Introduction",
        "What is AI ML DL",
        "Why Data Prepare for Training",
        "What is Data Set",
        "Machine Learning",
        "Neural Network"
    ])
    with tab1:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Introduction☺️
    </h4>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    Introduction Intellgent System
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       เว็บไซต์นี้เป็นส่วนหนึ่งของรายวิชา 
                    <span style="background-color: #990000;">Intellgent System 040613701</span> 
                    ซึ่งมุ่งเน้นการศึกษาหลักการระบบอัจฉริยะพื้นฐานและการประยุกต์ใช้ 
                    Machine Learning และ Neural Network ในการแก้ปัญหาต่าง ๆ ในโลกความเป็นจริง
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    จุดประสงค์ของเว็บไซต์
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - ให้ความเข้าใจเกี่ยวกับ ขั้นตอนการพัฒนาโมเดล AI ตั้งแต่การเตรียมข้อมูลไปจนถึงการนำไปใช้งาน<br>
                    - อธิบายทฤษฎีพื้นฐานของ Machine Learning และ Neural Network<br>
                    - สาธิตตัวอย่างการทำงานของโมเดล Machine Learning และ Neural Network<br> 
                    - แสดงให้เห็นถึง ความแตกต่าง ของอัลกอริทึม(Algorithm) แต่ละชนิด<br>
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<h5 style='font-family: Athiti; text-indent: 2.5em;'>
    เนื้อหาภายในเว็บไซต์
    </h5>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
                    - Introduction – แนะนำรายวิชาและวัตถุประสงค์ของเว็บไซต์<br>
                    - Algorithm & Model Development – อธิบายแนวทางการพัฒนาโมเดล Machine Learning และ Neural Network<br>
                    - Machine Learning Model – สาธิตการทำงานของโมเดล Machine Learning<br> 
                    - Neural Network Model – สาธิตการทำงานของโมเดล Neural Network<br>
                    <br>
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""
    <style>
        .about-container {
            text-align: center;
            font-family: 'Athiti', sans-serif;
        }
        .about-content {
            display: flex;
            justify-content: center;
            gap: 50px;
            font-size: 16px;
            text-align: left;
        }
    </style>
    <div class="about-container">
        <h5>About Us</h5>
        <div class="about-content">
            <div>
                <b>จัดทำโดย</b><br>
                นายพชร วรวัตร <br>
                รหัสนักศึกษา 6404062610324 <br>
                ห้อง DE-RA ชั้นปีที่ 4 <br>
            </div>
            <div>
                <b>อาจารย์ผู้สอน</b><br>
                ดร.ณัฐกิตติ์ จิตรเอื้อตระกูล (NJR) <br>
                ดร.ธรรศฏภณ สุระศักดิ์ (TSR) <br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    What is AI,ML,DL?🧐
    </h4>""", unsafe_allow_html=True)
        st.header("Artificial Intelligence :red[(AI)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       ปัญญาประดิษฐ์ หรือ AI คือ
                     ”ระบบ” ในการวิเคราะห์และประมวลผลที่มีความคล้ายคลึงกับความฉลาดของมนุษย์ 
                    และสามารถนำออกมาเป็นผลลัพธ์ต่างๆ เช่น การทำนายพฤติกรรมของลูกค้าใน 
                    E-Commerce หรือการวิเคราะห์อาการของผู้ป่วยจากข้อมูลต่างๆในโรงพยาบาล
    </p>""", unsafe_allow_html=True)
        
        st.header("Machine Learning :blue[(ML)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       Machine Learning คือ “การทำให้ระบบคอมพิวเตอร์สามารถเรียนรู้ได้ด้วยตนเองโดยใช้ข้อมูล” 
                    Machine Learning เป็น subset ของ AI จุดประสงค์คือเพื่อใช้ในการสร้างแอปพลิเคชั่นที่มีประสิทธิภาพมากกว่ามนุษย์ในการทำงานบางประเภท 
                    โดยการทำให้ฉลาดขึ้น สามารถพัฒนา และเรียนรู้ได้ด้วยตนเอง
    </p>""", unsafe_allow_html=True)
        
        st.header("Deep Learning :green[(DL)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       Deep Learning คือ “วิธีการเรียนรู้ลักษณะต่างๆ ของข้อมูล” โดยมีพื้นฐานการทำงานหรือการเรียนรู้จากระบบประสาทของสมองมุษย์ 
                    และ Deep Learning เป็น 
                    subset ของ Machine Learning อีกด้วย
    </p>""", unsafe_allow_html=True)
        
        st.image("img/ML-DL-AI.jpg", caption="How Difference of AI ML And DL")

    with tab3: 
        st.markdown("""<h4 style='font-family: Athiti; text-align: left;text-indent: 2.5em;'>
    🤖Why prepare data for artificial intelligence training?🤔
    </h4>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       โดยปกติตัว AI ก็คล้าย ๆ กับมนุษย์ทั่วไปนี่แหละ เปรียบเสมือนมนุษย์คนนึงจะแยกว่าอันไหนคือ 
                รถ หรือ คนได้ยังไง? ซึ่งคำตอบนั้นก็ง่าย ๆ ตรงตัวก็คือเราต้องเคยเห็นทั้ง รถและคนมาก่อน ว่ารถรูปร่างเป็นแบบไหนคนเป็นแบบไหนรูปร่างยังไง 
                แตกต่างกันอย่างไร เพราะว่าเรานั้นมีข้อมูลเยอะมากพอนั้นเอง (Data) แต่ถ้ามองในมุมกลับกัน ถ้าถามว่า รถที่เราไม่เคยเห็น 
                หรือมีรูปแบบที่เราไม่เคยเห็นมาก่อนก็อาจจะทำให้เรานั้นทายไม่ค่อยจะถูก เพราะว่าเรามี ข้อมูล(Data) ไม่เยอะมากพอหรือไม่เคยเห้นมากพอนั้นเอง
    </p>""", unsafe_allow_html=True)
        
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       จากที่เกริ่นมาเราจะเห็นได้ว่า ข้อมูล(Data) ถ้ามีมากพอเราจะเรียนรู้สิ่งต่าง ๆ 
                ได้มากยิ่งขึ้น จากการเรียนรู้สิ่งต่าง ๆ ที่มากขึ้นตามไปนั้นเอง โดยทั้งหมดนี้ถ้าเราจะสร้าง AI ให้มันฉลาดหรือมีความแม่นยำที่สูงนั้นจำเป็นต้อง 
                มีข้อมูล(Data) เป็นจำนวนมากให้กับ ตัว AI เพื่อให้มันเรียนรู้จากข้อมูลที่เรานำไปสอนมัน 
                แล้วให้ตัว AI ค่อย ๆ ทำความเข้าใจจนสุดท้ายมันก็จะสร้าง Model ออกมานั้นเอง ยิ่งเรามี Data ให้มันเรียนรู้มากพอและหลากหลายจะทำให้ตัว AI ของเราก็จะยิ่งแม่นยำมากยิ่งขึ้นนั้นเอง
    </p>""", unsafe_allow_html=True)
        
        st.image("img/Blog_Selecting-the-Right-AI-Training-Data-is-Important.jpg", caption="How Intelligent of Artificial Intelligence")
        
    with tab4:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    What is Data Set🔎
    </h4>""", unsafe_allow_html=True)
        st.header("Data Set :blue[(ชุดข้อมูล)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       Data Set หรือ ชุดข้อมูล คือ กลุ่มของข้อมูลที่ถูกเก็บรวบรวมไว้เพื่อใช้ในการวิเคราะห์ ประมวลผล 
                หรือฝึกสอนโมเดลปัญญาประดิษฐ์ (AI) เช่น Machine Learning (ML) หรือ Deep Learning (DL)
                ประเภทของ Data Set <br>
    </p>""", unsafe_allow_html=True)
        
        st.header("Structured Data :red[(ข้อมูลที่มีโครงสร้าง)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       ข้อมูลที่ถูกจัดเก็บในรูปแบบที่เป็นระเบียบ เช่น ตารางในฐานข้อมูล (Database), Excel, CSV<br>
                ตัวอย่าง: รายการสินค้าพร้อมราคาที่เก็บอยู่ใน Excel หรือ MySQL<br>
    </p>""", unsafe_allow_html=True)
        
        st.header("Unstructured Data :green[(ข้อมูลที่ไม่มีโครงสร้าง)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       ข้อมูลที่ไม่มีรูปแบบแน่นอน เช่น ข้อความ รูปภาพ วิดีโอ เสียง
                ตัวอย่าง: ข้อความรีวิวสินค้า, รูปภาพจากกล้องวงจรปิด
                Semi-structured Data (ข้อมูลกึ่งมีโครงสร้าง)
                ข้อมูลที่มีบางส่วนมีโครงสร้าง แต่ไม่เป็นระเบียบทั้งหมด เช่น JSON, XML, NoSQL<br>
                ตัวอย่าง: ข้อมูลจาก API ที่ส่งมาในรูปแบบ JSON<br>
    </p>""", unsafe_allow_html=True)
        
        st.header("Semi-structured Data :grey[(ข้อมูลกึ่งมีโครงสร้าง)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       ข้อมูลที่ไม่มีรูปแบบแน่นอน เช่น ข้อความ รูปภาพ วิดีโอ เสียง
                ตัวอย่าง: ข้อความรีวิวสินค้า, รูปภาพจากกล้องวงจรปิด
                Semi-structured Data (ข้อมูลกึ่งมีโครงสร้าง)
                ข้อมูลที่มีบางส่วนมีโครงสร้าง แต่ไม่เป็นระเบียบทั้งหมด เช่น JSON, XML, NoSQL<br>
                ตัวอย่าง: ข้อมูลจาก API ที่ส่งมาในรูปแบบ JSON<br><br>
    </p>""", unsafe_allow_html=True)
        
        st.image("img/datatype.png", caption="Type of Data Set")
        
    with tab5:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Machine Learning📎
    </h4>""", unsafe_allow_html=True)
        st.header("Machine Learning :blue[(ML)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       ที่มุ่งเน้นการพัฒนาอัลกอริธึม (Algorithm) และเทคนิคที่ช่วยให้คอมพิวเตอร์สามารถ
                        เรียนรู้จากข้อมูลได้โดยไม่จําเป็นต้องมีการเขียนโปรแกรมที่ชัดเจนสําหรับการทํางานแต่ละอย่าง การ
                        ทํางานของ Machine Learning จะขึ้นอยู่กับการฝึกสอนโมเดลด้วยข้อมูลจํานวนมาก ซึ่งโมเดลจะทําการ
                        วิเคราะห์และค้นหารูปแบบจากข้อมูลเหล่านั้น เพื่อให้สามารถทําการคาดการณ์หรือจําแนกประเภทข้อมูล
                        ใหม่ได้อย่างแม่นยํา
                        การเรียนรู้ของเครื่องแบ่งออกเป็นสามประเภทหลัก ๆ
    </p>""", unsafe_allow_html=True)
        
        st.header("- Supervised Learning :orange[(Label)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       การเรียนรู้แบบผู้สอน (Supervised Learning)
                    เป็นการเรียนรู้แบบโดยจะมีผู้สอน เรียกง่าย ๆคือ
                    โมเดลจะถูกฝึกสอนด้วยข้อมูลที่มีการติดป้ายกํากับ (Label) ซึ่งหมายถึงข้อมูลที่มีผลลัพธ์ที่ถูกต้องกํากับ
                    อยู่ เมื่อโมเดลได้รับข้อมูลนี้จะทําการเรียนรู้และสร้างฟังก์ชันเพื่อคาดการณ์ผลลัพธ์ที่ต้องการเมื่อได้รับ
                    ข้อมูลใหม่
    </p>""", unsafe_allow_html=True)
        
        st.header("- Unsupervised Learning :green[(Data Driven)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning) เป็นการเรียนรู้แบบรูปแบบไม่มีผู้สอน โมเดลจะ
                ทําการเรียนรู้จากข้อมูลที่ไม่มีการติดป้ายกํากับ ซึ่งจะเน้นในการค้นหารูปแบบหรือโครงสร้างที่ซ่อนอยู่ใน
                ข้อมูล การเรียนรู้แบบนี้มักถูกนํามาใช้ในงานที่ต้องการค้นหาความสัมพันธ์ระหว่างข้อมูลที่ไม่มีการจัด
                หมวดหมู่ เช่น การทําคลัสเตอร์ (Clustering) ที่ช่วยในการจัดกลุ่มข้อมูลที่มีลักษณะคล้ายกัน โดยไม่
                ต้องการข้อมูลที่มีการติดป้ายกํากับ
    </p>""", unsafe_allow_html=True)
        
        st.header("- Reinforcement Learning :gray[(Reward)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       การเรียนรู้แบบเสริมกําลัง (Reinforcement Learning) เป็นการเรียนรู้แบบเสริมเป็นวิธีการที่โมเดลจะ
                    ทําการทดลองและเรียนรู้จากผลตอบแทนหรือบทลงโทษที่ได้รับจากการกระทํา โดยในกระบวนการนี้
                    โมเดลจะเรียนรู้จากการลองผิดลองถูก เพื่อพัฒนากลยุทธ์ที่ดีที่สุดในการตัดสินใจในสถานการณ์ที่มีความ
                    ไม่แน่นอน ตัวอย่างการใช้ Reinforcement Learning คือการฝึกโมเดลให้เล่นเกม โดยโมเดลจะได้รับ
                    คะแนนเป็นผลตอบแทนเมื่อทําได้ดี และจะได้รับบทลงโทษเมื่อทําผิด
    </p>""", unsafe_allow_html=True)

        st.image("img/ML-Type.png", caption="How Difference of Type Learning")
    
    with tab6:
        st.markdown("""<h4 style='font-family: Athiti; text-align: center;text-indent: 2.5em;'>
    Neural Network🧠
    </h4>""", unsafe_allow_html=True)
        st.header("- Neural Network :red[(Weight&Bias)]")
        st.markdown("""<p style='font-family: Athiti; text-align: justify;'>
       อ้างอิงจากระบบประสาทในมนุษย์ ถูกออกแบบมาเพื่อให้
                สามารถเรียนรู้และประมวลผลข้อมูลได้อย่างมีประสิทธิภาพ โดยมีหน่วยประมวลผลที่เรียกว่า "นิวรอน"
                (Neurons) ที่ทําหน้าที่รับข้อมูล คํานวณ และส่งผลลัพธ์ไปยังนิวรอนในชั้นถัด ๆ ไป
                โครงสร้างของโครงข่ายประสาทเทียมแบ่งออกเป็นสามชั้นหลัก ได้แก่ ชั้นนําเข้าข้อมูล (Input Layer)
                ที่ใช้สําหรับรับข้อมูลที่จะวิเคราะห์ ชั้นซ่อน (Hidden Layers) ซึ่งอยู่ระหว่างชั้นนําเข้าและชั้นส่งออก ซึ่ง
                อาจมีหลายชั้น และชั้นส่งออก (Output Layer) ที่ให้ผลลัพธ์สุดท้ายจากการประมวลผลข้อมูล
                เมื่อข้อมูลถูกส่งเข้ามายังโครงข่าย<br>
                <br>
       นิวรอนแต่ละตัวจะใช้ฟังก์ชันการกระตุ้น (Activation Function) ใน
                การคํานวณเพื่อกําหนดว่านิวรอนจะส่งข้อมูลไปยังชั้นถัดไปหรือไม่ การคํานวณนี้จะใช้ "น้ําหนัก"
                (Weights) และ "อคติ" (Bias) เป็นปัจจัยสําคัญ<br>
                น้ําหนัก (Weights) เป็นค่าที่แสดงถึงความสําคัญของข้อมูลที่ส่งเข้าสู่นิวรอนแต่ละตัว โดยค่าของ
                น้ําหนักจะถูกปรับในระหว่างกระบวนการฝึกอบรม (Training) เพื่อเพิ่มความแม่นยําในการจําแนก
                ประเภทหรือลงทํานายผลลัพธ์ ค่าน้ําหนักที่สูงบ่งบอกว่าข้อมูลนั้นมีความสําคัญในกระบวนการคํานวณ
                มากขึ้น
                อคติ (Bias) ช่วยเพิ่มความยืดหยุ่นให้กับผลลัพธ์ของนิวรอน โดยทําหน้าที่เป็นค่าที่ถูกเพิ่มเข้ามาในการ
                คํานวณ ทําให้โครงข่ายสามารถปรับตัวเข้ากับข้อมูลได้ดีขึ้น และช่วยสร้างผลลัพธ์ที่มีประสิทธิภาพ <br>
                <br>
       แม้ใน กรณีที่ข้อมูลมีลักษณะเฉพาะหรือไม่เป็นเชิงเส้น
                <span style="background-color: #990000;"> "โดยการฝึกอบรมโครงข่ายประสาทเทียมมมักใช้เทคนิคที่เรียกว่า การย้อนกลับ (Backpropagation) เพื่อ
                ปรับปรุงน้ําหนัก (Weights) และอคติ(Bias) โดยการคํานวณค่าความผิดพลาด (Error) ระหว่างผลลัพธ์ที่
                ทํานายและค่าจริง แล้วทําการปรับน้ําหนัก (Weights) และอคติ(Bias) เพื่อลดค่าความผิดพลาด " (Neurons)</span>
    </p>""", unsafe_allow_html=True)

        file_ = open("img/visuNN.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)