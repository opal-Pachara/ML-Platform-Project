import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh  
from show_introduction import show_introduction
from show_model_development import show_model_development
from show_ml import show_ml
from show_nn import show_nn

def main():
    # Handle visitor count with session state
    if 'session_ids' not in st.session_state:
        st.session_state.session_ids = set()

    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(datetime.now().timestamp())
        st.session_state.session_ids.add(st.session_state.session_id)

    real_count = len(st.session_state.session_ids)
    visitor_count = 208 + real_count

    # Auto-refresh every 1 second (for the visitor count update)
    if 'refresh_enabled' not in st.session_state or st.session_state.refresh_enabled:
        st_autorefresh(interval=1000, key="visitor_refresh")

    # Conditionally hide navbar for the "Introduction & Data Set" page
    navbar_css = ""
    if st.session_state.get('selected_page', "Introduction & Data Set") == "Introduction & Data Set":
        navbar_css = """
            header[data-testid="stHeader"] {
                display: none !important;
            }
        """

    # CSS for styling, including conditional navbar hiding
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Athiti:wght@400&display=swap');
        html, body, [class*="css"] {{
            font-family: 'Athiti', sans-serif;
            font-size: 16px;
            font-weight: 400;
            line-height: 1.6;
            color: #ffffff;
        }}
        .stSidebar, .stButton>button, .stMarkdown, 
        .stTextInput, .stNumberInput {{
            font-family: 'Athiti', sans-serif !important;
            font-size: 16px !important;
            font-weight: 400 !important;
            line-height: 1.6 !important;
            color: #ffffff !important;
        }}
        /* Sidebar styling */
        .stSidebar {{
            background-color: #111217 !important;
        }}
        .stSidebar * {{
            color: #ffffff !important;
        }}
        /* ปุ่มใน Sidebar */
        .stSidebar .stButton>button {{
            background-color: #1a1b22 !important;
            color: #b0b0b0 !important;
            border: none !important;
            border-radius: 6px;
            padding: 8px 12px;
            width: 100%;
            text-align: left;
            transition: all 0.2s ease;
            margin: 4px 0;
        }}
        .stSidebar .stButton>button:hover {{
            background-color: #FF4B4B !important;
            color: #ffffff !important;
        }}
        .stSidebar .stButton>button.active {{
            background-color: #00d4ff !important;
            color: #121212 !important;
            font-weight: 600 !important;
        }}
        /* Dark Mode */
        @media (prefers-color-scheme: dark) {{
            .stApp {{
                background: #121212;
                color: #ffffff;
            }}
            h1, h2, h3, h4 {{
                color: #ffffff;
            }}
            .stButton>button:not(.stSidebar .stButton>button) {{
                background-color: #242222 !important;
                color: #ffffff !important;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #FF4B4B !important;
                transition: 0.3s;
            }}
            .stButton>button:not(.stSidebar .stButton>button):hover {{
                background-color: #333333 !important;
            }}
            .stTextInput>div>div>input {{
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #333333;
            }}
        }}
        /* Light Mode */
        @media (prefers-color-scheme: light) {{
            .stApp {{
                background: #121212;
                color: #ffffff;
            }}
            h1, h2, h3, h4 {{
                color: #ffffff;
            }}
            .stButton>button:not(.stSidebar .stButton>button) {{
                background-color: #000000 !important;
                color: #ffffff !important;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #333333 !important;
                transition: 0.3s;
            }}
            .stButton>button:not(.stSidebar .stButton>button):hover {{
                background-color: #333333 !important;
            }}
            .stTextInput>div>div>input {{
                background-color: #000000;
                color: #ffffff;
                border: 1px solid #333333;
            }}
        }}
        /* Conditional navbar hiding */
        {navbar_css}
        </style>
    """, unsafe_allow_html=True)
    
    st.logo("img/logo.png", size="large")
    st.sidebar.title("Intelligent System Project")
    st.sidebar.caption("Phatchara Worrawat 6404062610324")
    st.sidebar.title("Menu")

    # ใช้ Session State เพื่อติดตามหน้าที่เลือก
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = "Introduction & Data Set"

    # สร้างปุ่มใน Sidebar
    if st.sidebar.button("Introduction & Data Set", key="intro"):
        st.session_state.selected_page = "Introduction & Data Set"
    if st.sidebar.button("Algorithm & Model Development", key="algo"):
        st.session_state.selected_page = "Algorithm & Model Development"
    if st.sidebar.button("Machine Learning Model", key="ml"):
        st.session_state.selected_page = "Machine Learning Model"
    if st.sidebar.button("Neural Network Model", key="nn"):
        st.session_state.selected_page = "Neural Network Model"

    # ใช้ JavaScript เพื่อเพิ่มคลาส active ให้ปุ่มที่เลือก
    st.markdown(f"""
        <script>
        document.querySelectorAll('.stSidebar .stButton>button').forEach(button => {{
            button.classList.remove('active');
            if (button.textContent === "{st.session_state.selected_page}") {{
                button.classList.add('active');
            }}
        }});
        </script>
    """, unsafe_allow_html=True)

    # Visitor count and GitHub link in the sidebar
    st.sidebar.markdown(f"""
        <div style='text-align: center; padding: 15px; background-color: #1a1b22; border-radius: 10px; margin-top: 20px; border: 1px solid #333333;'>
            <h3 style='font-family: Athiti; color: #ffffff; margin: 0;'>👀 จำนวนคนเข้าชม</h3>
            <p style='font-family: Athiti; font-size: 28px; font-weight: bold; color: #00d4ff; margin: 5px 0;'>{visitor_count}</p>
            <p style='font-family: Athiti; font-size: 12px; color: #b0b0b0; margin: 0;'>อัปเดต: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
        <div style='text-align: center; margin-top: 15px;'>
            <a href='https://github.com/opal-Pachara' target='_blank' style='font-family: Athiti; font-size: 16px; color: #00d4ff; text-decoration: none;'>
                🌐 GitHub Repository
            </a>
        </div>
    """, unsafe_allow_html=True)

    # Data options for selection
    if st.session_state.selected_page == "Introduction & Data Set":
        show_introduction()
    elif st.session_state.selected_page == "Algorithm & Model Development":
        show_model_development()
    elif st.session_state.selected_page == "Machine Learning Model":
        show_ml()
    elif st.session_state.selected_page == "Neural Network Model":
        show_nn()

if __name__ == "__main__":
    main()