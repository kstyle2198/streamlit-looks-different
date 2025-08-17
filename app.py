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
col1, col2 = st.columns([1, 1])
with col1:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height="stretch"):
        if st.button(":green[**Hovering with Streamlit**]", use_container_width=True):
            st.switch_page("pages/01_hovering.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/hovering.gif", use_container_width=True)

with col2:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height="stretch"):
        if st.button(":blue[**Parallax Effect with Streamlit**]", use_container_width=True):
            st.switch_page("pages/02_parallax.py")   # pages 폴더 안에 sub_page.py 있어야 함
        with st.container(border=True):
            st.image("./images/parallax.gif", use_container_width=True)