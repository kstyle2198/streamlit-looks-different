import streamlit as st

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
    Streamlit looks different
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
line1_container = st.container(horizontal=True, height="stretch")
with line1_container:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":green[**Hovering Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/01_hovering.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/hovering.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":blue[**Parallax Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/02_parallax.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/parallax.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":blue[**Distortion Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/03_distortion.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/distortion.jpg", use_container_width=True)

line2_container = st.container(horizontal=True, height="stretch")
with line2_container:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":green[**Geometry Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/04_geometry.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/geometry.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":blue[**Ripple Drop Wave Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/05_wave.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/ripple.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":orange[**Lightning Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/06_lightning.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/lightning.jpg", use_container_width=True)

line3_container = st.container(horizontal=True, height="stretch")
with line3_container:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":green[**Gradient Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/07_gradient.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/gradient.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":blue[**Aurora Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/08_aurora.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/aurora.jpg", use_container_width=True)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height=350):
        if st.button(":orange[**Random Floating Word Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/09_text_float.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/floating_word.jpg", use_container_width=True)