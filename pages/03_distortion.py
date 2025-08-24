# ==== Background Image with Wave Effect ====
import streamlit as st
import base64

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
        overflow: hidden;
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

    /* Wave effect (subtle distortion) */
    [data-testid="stAppViewContainer"]::after {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: inherit;
        background-size: cover;
        mix-blend-mode: soft-light;
        filter: url('#wave');
        animation: waveMove 12s ease-in-out infinite alternate;
        z-index: 0;
        opacity: 0.8;
    }}

    @keyframes waveMove {{
        0%   {{ transform: scale(1.02) translateX(-1%) translateY(-1%); }}
        50%  {{ transform: scale(1.05) translateX(1%) translateY(1%); }}
        100% {{ transform: scale(1.02) translateX(-1%) translateY(0%); }}
    }}

    .stApp {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("./images/bg_ranny.jpg", overlay_color="rgba(255,255,255,0.6)")


# --- Streamlit 앱 메인 부분 ---

# 페이지 설정 (넓은 레이아웃)
st.set_page_config(layout="wide")

sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras non nisi feugiat, tincidunt nulla eget, luctus nisl. Integer eleifend justo in purus hendrerit laoreet. Vivamus vestibulum eros augue, quis hendrerit purus fringilla vitae. In quis ipsum nisl. Morbi vulputate est turpis, vel gravida magna eleifend consequat. Sed placerat rutrum dui nec porttitor. Curabitur non blandit tellus, sit amet congue felis. Maecenas ante purus, malesuada nec sem eget, lobortis egestas neque. Nam pretium a neque at scelerisque. Sed lobortis interdum vestibulum. Proin risus lectus, lobortis porta pellentesque at, ullamcorper lobortis sem. Quisque ut neque congue, aliquam eros id, pulvinar elit. Suspendisse ornare accumsan elit ac bibendum. Ut porta, massa sit amet sodales aliquam, enim eros fermentum ex, eget bibendum lorem risus vel nisi. Donec posuere sagittis purus, eu malesuada diam.
Praesent pellentesque eget purus at iaculis. Aliquam eu ligula lectus. Donec at ligula in mi ornare congue. Integer ornare in tellus a volutpat. Integer dapibus leo nec massa maximus, quis luctus metus aliquet. Sed id diam in odio rutrum condimentum vitae in ex. Ut sit amet orci arcu. Vestibulum blandit libero sit amet erat bibendum fringilla. Curabitur quis tempor erat.
Morbi ut lectus nec nunc imperdiet feugiat. Aliquam consequat dui ut vulputate eleifend. Aenean nec dui nulla. Quisque placerat dictum est, ac gravida sapien sagittis vel. Cras tortor nulla, gravida suscipit facilisis placerat, venenatis sit amet tellus. Aliquam non justo velit. Sed at rutrum nibh, a sodales neque. Ut at sodales eros. Aliquam erat volutpat. In quis faucibus sapien. Vivamus nisl metus, gravida id sodales non, imperdiet ut nisl. Sed porttitor arcu quis magna condimentum suscipit. Nulla non tempus ligula. Morbi ornare pellentesque purus vitae posuere. Donec auctor viverra finibus.
Sed venenatis convallis tempor. Integer ultricies dolor nulla, nec pharetra magna accumsan in. Praesent efficitur ante dolor, feugiat ultricies turpis feugiat eu. Cras quis commodo tortor. Cras cursus sollicitudin luctus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus egestas eget felis a rhoncus. Ut placerat enim metus, id euismod purus consectetur vitae. Curabitur id auctor lorem. Nunc et faucibus tortor, a tincidunt metus. Integer convallis ac dui sed venenatis.
Cras sit amet sapien ornare, ultrices sem in, interdum quam. Vivamus eu mauris ut mi ullamcorper aliquet quis non lacus. Praesent gravida ante turpis, in semper augue facilisis at. Curabitur mattis sed ipsum id molestie. Phasellus accumsan volutpat nibh id semper. Morbi at orci nec sem venenatis consectetur. Proin ac leo in purus ornare finibus. Integer vehicula finibus arcu, eu laoreet lacus blandit in. Vivamus euismod turpis eget erat fringilla viverra. Integer tincidunt hendrerit tincidunt. Donec eget porta sapien. Vestibulum tempus interdum diam, ut tincidunt diam iaculis sit amet. Donec ornare ut augue vehicula tincidunt. 
"""


if __name__ == "__main__":
    
    # Title
    st.markdown(
        """
        <h1 style="
            font-family: 'Arial';
            font-size: 60px;
            color: #fcfdff;
            text-shadow: 2px 2px 4px #aaa;
            text-align: center;
            ">
        Distortion Effect with Streamlit
        </h1>
        """,
        unsafe_allow_html=True
    )

 
    st.markdown("---")
    st.markdown(
        """
        <style>
        .stMarkdown p {
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(sample_text)
    
    



