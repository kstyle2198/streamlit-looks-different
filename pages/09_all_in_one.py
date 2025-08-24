import streamlit as st
import base64
from PIL import Image
import os

# ==== 배경 처리 ====
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file, overlay_color="rgba(255,255,255,0.5)"):
    bin_str = get_base64_of_image(image_file)
    page_bg_img = f"""
    <style>
    /* 앱 전체 배경 */
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {{
        position: relative;
        background: url("data:image/png;base64,{bin_str}") no-repeat center center fixed;
        background-size: cover;
    }}

    /* 오버레이 효과 */
    [data-testid="stAppViewContainer"]::before,
    [data-testid="stHeader"]::before {{
        content: "";
        position: absolute;
        top: 0; right: 0; bottom: 0; left: 0;
        background: {overlay_color};
        z-index: 0;
    }}

    .stApp {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("./images/bg_img1.jpg", overlay_color="rgba(255,255,255,0.6)")  

st.set_page_config(layout="wide")
# Title
st.markdown(
    """
    <h1 style="
        font-family: 'Arial';
        font-size: 60px;
        color: #003082;
        text-shadow: 2px 2px 4px #aaa;
        text-align: center;
        ">
    Parallax Effect with Streamlit
    </h1>
    """,
    unsafe_allow_html=True
)


# Hover 효과를 위한 CSS 스타일 주입
st.markdown(
    """
    <style>
    /* container 자체에만 hover 적용 */
    .st-emotion-cache-uvlrfw {
        transition: all 0.35s ease;
        border-radius: 16px;
    }
    .st-emotion-cache-uvlrfw:hover {
        background: rgba(255, 255, 255, 0.25);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(12px) saturate(150%);
        -webkit-backdrop-filter: blur(12px) saturate(150%);
        transform: translateY(-6px);
    }
    </style>
    """,
        unsafe_allow_html=True
    )

# ==== main_h0_container에 custom class 부여 ====
st.markdown('<div class="st-emotion-cache-uvlrfw">', unsafe_allow_html=True)
main_h0_container = st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="distribute", height=400, border=False, gap="medium")
with main_h0_container:
    with st.container(border=True, width="stretch"):
        with st.container(horizontal=True):
            with st.container(border=False, width="stretch", height="stretch"):
                st.image("./images/sample1.jpg", use_container_width=True)
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me!")
                
    with st.container(border=True, width="stretch"):
        with st.container(horizontal=True, border=False, height="stretch"):
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me!")
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me too!")
        with st.container(horizontal=True, border=False, height="stretch"):
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me!")
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me too!")
        with st.container(horizontal=True, border=False, height="stretch"):
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me!")
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me too!")

    with st.container(border=True, width="stretch"):
        st.subheader("This is a container No3.")
        st.markdown("Hover me too!")
st.markdown("</div>", unsafe_allow_html=True)



# ==== CSS 스타일 주입 ====
def inject_custom_css():
    """ 패럴랙스 및 기타 UI 효과를 위한 CSS를 주입합니다. """
    # 이미지 파일 경로 설정
    img1_path = "./images/bg_img1.jpg"
    img2_path = "./images/bg_img2.jpg"

    # 이미지 Base64 인코딩
    bin_str1 = get_base64_of_image(img1_path)
    bin_str2 = get_base64_of_image(img2_path)
    
    if not bin_str1 or not bin_str2:
        return # 이미지 로딩 실패 시 CSS 주입 중단

    custom_css = f"""
    <style>
        /* 기본 HTML 및 Body 스타일 초기화 */
        body, html {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}

        /* 패럴랙스 섹션 컨테이너 */
        .parallax {{
            /* 패럴랙스 효과의 핵심 */
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover;

            /* 섹션의 최소 높이 설정 */
            min-height: 400px;
            
            /* 콘텐츠를 중앙에 배치하기 위한 Flexbox 설정 */
            display: flex;
            align-items: center;
            justify-content: center;

            /* 여백 제거 */
            margin: 0 !important;
            padding: 0 !important;
        }}

        /* 첫 번째 패럴랙스 섹션의 배경 이미지 */
        .parallax-1 {{
            background-image: url("data:image/jpeg;base64,{bin_str1}");
        }}

        /* 두 번째 패럴랙스 섹션의 배경 이미지 */
        .parallax-2 {{
            background-image: url("data:image/jpeg;base64,{bin_str2}");
        }}
        
        /* 패럴랙스 섹션 위의 텍스트 스타일 */
        .parallax-text {{
            font-size: 3rem;
            font-weight: bold;
            color: white;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px 40px;
            border-radius: 10px;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
        }}

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# ==== UI 렌더링 ====

# 1. CSS 주입
inject_custom_css()

# 2. 첫 번째 패럴랙스 섹션
st.markdown(
    '<div class="parallax parallax-1"><div class="parallax-text">Scroll Down 👇</div></div>',
    unsafe_allow_html=True
)

st.markdown('<div class="st-emotion-cache-uvlrfw">', unsafe_allow_html=True)
main_h1_container = st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="distribute", height=300, border=False, gap="medium")
with main_h1_container:
    with st.container(border=True, width="stretch"):
        st.subheader("Test")
        st.markdown("Test")


    with st.container(border=True, width="stretch"):
        st.subheader("Test")
        st.markdown("Test")

st.markdown("</div>", unsafe_allow_html=True)


# 4. 두 번째 패럴랙스 섹션
st.markdown(
    '<div class="parallax parallax-2"><div class="parallax-text">Awesome Effect! ✨</div></div>',
    unsafe_allow_html=True
)

# 5. 다른 콘텐츠 섹션 추가 (선택)
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.header("More Content")
st.write("You can create dynamic pages by alternating the parallax section and the general content section.")
st.markdown("</div>", unsafe_allow_html=True)


with st.expander("Show More", expanded=False):
    with st.container(border=True):
        st.markdown(
            """
            ## What is the parallax effect?
            The parallax effect is a visual effect in which the background image moves slower than the content when scrolling. This allows you to add depth and dynamic feel to your web page.

            ## Implementing the Parallax Effect in Streamlit
            In Streamlit, you can easily implement the parallax effect using HTML and CSS. In the example above, you created two parallax sections, each setting up a different background image.
            """
        )   



# ==== 이미지 슬라이더 컴포넌트 ====
from streamlit_carousel import carousel

items = [
    {"title": "고창읍성1", "text": "This is first slide", "img": "./slides/slide1.jpg"},
    {"title": "고창읍성2", "text": "This is second slide", "img": "./slides/slide2.jpg"},
    {"title": "고창읍성3", "text": "This is third slide", "img": "./slides/slide3.jpg"},
    {"title": "고창읍성4", "text": "This is fourth slide", "img": "./slides/slide4.jpg"},
]

carousel(items, container_height=470, slide=True, fade=True, width=0.5,)
