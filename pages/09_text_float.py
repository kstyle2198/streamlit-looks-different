import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Random Floating Word Effect",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        position: relative;
        overflow: hidden;
        background: #ffffff; /* 흰색 배경 */
    }
    #geometryCanvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        pointer-events: none;
        background: #ffffff; /* 캔버스도 흰색 배경 */
    }
    .content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(200, 200, 200, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for floating word effect
word_js = """
<canvas id="geometryCanvas"></canvas>
<script>
let canvas = document.getElementById('geometryCanvas');
let ctx = canvas.getContext('2d');
let width = window.innerWidth;
let height = window.innerHeight;
canvas.width = width;
canvas.height = height;

// 보여줄 문장
let sentence = "Streamlit makes data apps simple and beautiful. 스트림릿은 데이터 앱을 쉽고 아름답게 만듭니다.";
let words = sentence.split(" ");

// 파스텔톤 색상
let colors = [
    '#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF',
    '#E0BBE4', '#FFDAC1', '#B5EAD7', '#C7CEEA'
];

let activeWords = [];

// Word 생성
function spawnWord() {
    let word = words[Math.floor(Math.random() * words.length)];
    activeWords.push({
        text: word,
        x: Math.random() * width,
        y: Math.random() * height,
        dx: (Math.random() - 0.5) * 0.5, // 천천히 이동
        dy: (Math.random() - 0.5) * 0.5,
        opacity: 0,
        life: 0,
        maxLife: 250 + Math.random() * 100,
        fadeIn: true,
        color: colors[Math.floor(Math.random() * colors.length)]
    });
}

// Animation
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < activeWords.length; i++) {
        let w = activeWords[i];
        w.life++;

        // 움직임
        w.x += w.dx;
        w.y += w.dy;

        // 페이드인
        if (w.fadeIn && w.opacity < 1) {
            w.opacity += 0.02;
            if (w.opacity >= 1) w.fadeIn = false;
        } 
        // 페이드아웃
        else if (!w.fadeIn) {
            w.opacity -= 0.01;
        }

        ctx.font = "bold 28px Arial";
        ctx.fillStyle = `rgba(${hexToRgb(w.color)},${w.opacity})`;
        ctx.fillText(w.text, w.x, w.y);

        if (w.life > w.maxLife || w.opacity <= 0) {
            activeWords.splice(i, 1);
            i--;
        }
    }
}

// HEX → RGB 변환 함수
function hexToRgb(hex) {
    hex = hex.replace('#','');
    let bigint = parseInt(hex, 16);
    let r = (bigint >> 16) & 255;
    let g = (bigint >> 8) & 255;
    let b = bigint & 255;
    return r + "," + g + "," + b;
}

// 일정 간격으로 단어 추가
setInterval(spawnWord, 1500);

// 반응형
window.addEventListener('resize', () => {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
});

animate();
</script>
"""

# Content
st.markdown(
    """
    <div class="content">
        <h1 style="
            font-family: 'Arial', sans-serif;
            font-size: 3rem;
            color: #444;
            text-align: center;
            ">
        Random Floating Word Effect (Pastel Colors)
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# HTML + JS 렌더링
html(word_js, height=200)



### 아래는 CAVAS가 아니라 백그라운드 전체 화면 위에 단어가 떠다니는 효과
# import streamlit as st
# from streamlit.components.v1 import html

# # Page configuration
# st.set_page_config(
#     page_title="Floating Words Fullscreen",
#     page_icon="✨",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # CSS + JS: 전체 화면 최상위 레이어에 단어 효과
# fullscreen_effect = """
# <style>
# body {
#     background: #ffffff; /* 전체 흰색 배경 */
#     overflow: hidden;
#     margin: 0;
#     padding: 0;
# }

# /* 전체 화면 최상위 레이어 */
# #floating-layer {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100vw;
#     height: 100vh;
#     z-index: 9999; /* 모든 콘텐츠 위 */
#     pointer-events: none; /* 클릭 방해 X */
# }

# /* 단어 스타일 */
# .floating-word {
#     position: absolute;
#     font-size: 28px;
#     font-weight: bold;
#     opacity: 0;
#     white-space: nowrap;
#     transition: opacity 2s ease-in-out;
# }
# </style>

# <div id="floating-layer"></div>

# <script>
# let sentence = "Streamlit makes data apps simple and beautiful";
# let words = sentence.split(" ");

# // 파스텔톤 색상
# let colors = [
#     '#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF',
#     '#E0BBE4', '#FFDAC1', '#B5EAD7', '#C7CEEA'
# ];

# function spawnWord() {
#     let layer = document.getElementById("floating-layer");
#     let word = words[Math.floor(Math.random() * words.length)];
#     let span = document.createElement("span");
#     span.className = "floating-word";
#     span.innerText = word;
#     span.style.color = colors[Math.floor(Math.random() * colors.length)];

#     // 랜덤 위치
#     let startX = Math.random() * window.innerWidth;
#     let startY = Math.random() * window.innerHeight;
#     span.style.left = startX + "px";
#     span.style.top = startY + "px";

#     layer.appendChild(span);

#     // 이동 방향 (랜덤)
#     let dx = (Math.random() - 0.5) * 1.5;
#     let dy = (Math.random() - 0.5) * 1.5;

#     let opacity = 0;
#     let life = 0;
#     let maxLife = 300 + Math.random() * 200;

#     setTimeout(() => { span.style.opacity = 1; }, 50);

#     function animate() {
#         life++;
#         startX += dx;
#         startY += dy;
#         span.style.left = startX + "px";
#         span.style.top = startY + "px";

#         if (life > maxLife * 0.7) {
#             opacity -= 0.01;
#             span.style.opacity = opacity;
#         } else if (opacity < 1) {
#             opacity += 0.02;
#             span.style.opacity = opacity;
#         }

#         if (life > maxLife || opacity <= 0) {
#             span.remove();
#         } else {
#             requestAnimationFrame(animate);
#         }
#     }

#     animate();
# }

# // 0.15초마다 단어 생성
# setInterval(spawnWord, 150);
# </script>
# """

# # Streamlit 콘텐츠
# st.markdown(
#     """
#     <div style="position: relative; z-index: 1; text-align: center; margin-top: 5rem;">
#         <h1 style="font-size: 3rem; color: #444;">
#             Floating Words Fullscreen (Pastel Colors)
#         </h1>
#         <p style="font-size: 1.2rem; color: #666;">
#             단어들이 전체 화면 위에 나타났다 움직이며 사라지는 효과
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # HTML 렌더링
# html(fullscreen_effect, height=100)

# with st.container():
#     st.write("---")
#     st.header("Try it yourself!")

# with st.expander("✨ About this effect"):
#     st.markdown("""
#     - This effect creates floating words that appear, move, and fade out across the entire screen.
#     - The words are randomly selected from a predefined sentence and displayed in pastel colors.
#     - The effect is implemented using HTML, CSS, and JavaScript, and is rendered in Streamlit using the `html` component.
#     - The floating words layer is positioned above all other content to ensure visibility.
#     - The words move slowly in random directions and fade in and out smoothly.
#     """)


