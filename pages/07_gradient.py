import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pastel Gradient Background",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for pastel gradient background
st.markdown("""
<style>
    /* 전체 페이지 배경에 파스텔톤 애니메이션 그라데이션 적용 */
    body {
        margin: 0;
        padding: 0;
        height: 100vh;
        background: linear-gradient(-45deg, #f9d5e5, #cfe0e8, #d6eadf, #fff1e6);
        background-size: 400% 400%;
        animation: gradient-animation 18s ease infinite; 
        overflow: hidden;
    }

    .stApp {
        background: transparent; 
    }

    .main > div {
        background: transparent;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* 콘텐츠 박스 스타일 */
    .content-box {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.6); 
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }

    /* 제목 스타일 */
    .title-text {
        font-family: 'Arial', sans-serif;
        font-size: 3rem;
        color: #4a4a4a;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.8);
        text-align: center;
        margin-bottom: 1rem;
    }

    /* 설명 텍스트 스타일 */
    .description-text {
        font-family: 'Segoe UI', sans-serif;
        font-size: 1.2rem;
        color: #5a5a5a;
        text-align: center;
        line-height: 1.6;
        margin-top: 1.5rem;
    }

    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
</style>
""", unsafe_allow_html=True)

# Streamlit 앱의 콘텐츠
st.markdown(
    """
    <div class="content-box">
        <h1 class="title-text">
            Welcome to the Future!
        </h1>
        <p class="description-text">
            Enjoy a calm and elegant user interface with a soft pastel gradient background. 
            Subtle transitions create a soothing environment for your data and insights.
        </p>
        <p class="description-text">
            Pastel tones help reduce eye strain while keeping the interface stylish and modern.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
