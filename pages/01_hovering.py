import streamlit as st
import base64
from PIL import Image
import os

st.set_page_config(layout="wide")

# ==== Background Image ====
def get_base64_of_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file, overlay_color="rgba(255,255,255,0.5)"):
    bin_str = get_base64_of_image(image_file)
    page_bg_img = f"""
    <style>
    /* App Full Background */
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"] {{
        position: relative;
        background: url("data:image/png;base64,{bin_str}") no-repeat center center fixed;
        background-size: cover;
    }}

    /* Overlay Effect */
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
    Hovering Effect with Streamlit
    </h1>
    """,
    unsafe_allow_html=True
)

# Inject CSS style for Hover effect
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
main_h0_container = st.container(horizontal=True, horizontal_alignment="center", vertical_alignment="distribute", height=350, border=False, gap="medium")
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
                st.image("./images/sample2.jpg", use_container_width=True)
        with st.container(horizontal=True, border=False, height="stretch"):
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me!")
            with st.container(border=True, width="stretch", height="stretch"):
                st.markdown("Hover me too!")
    with st.container(border=True, width="stretch"):
        st.subheader("This is a container No3.")
        st.markdown("Hover me too!")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

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

