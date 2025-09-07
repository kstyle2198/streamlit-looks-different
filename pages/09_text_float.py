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
