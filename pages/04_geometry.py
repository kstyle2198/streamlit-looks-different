import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Random Geometry Wave Background",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the geometry effect and styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        position: relative;
        overflow: hidden;
    }
    
    /* Canvas for the geometry effect */
    #geometryCanvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1; /* Canvas를 배경으로 보냅니다 */
        pointer-events: none;
    }
    
    /* Content styling */
    .content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.1); /* 투명도 조절 */
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px); /* 배경 블러 효과 */
        -webkit-backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for the geometry effect
# 자동으로 랜덤한 위치에 효과를 생성하는 기능 추가
geometry_js = """
<canvas id="geometryCanvas"></canvas>
<script>
// Initialize variables
let canvas = document.getElementById('geometryCanvas');
let ctx = canvas.getContext('2d');
let points = [];
let width = window.innerWidth;
let height = window.innerHeight;
canvas.width = width;
canvas.height = height;

let mouse = {x: 0, y: 0};
let colors = ['#ff9a9e', '#fad0c4', '#a1c4fd', '#c2e9fb', '#ffecd2', '#fcb69f'];

// <<< NEW FUNCTION >>> 
// 랜덤한 위치에 파티클 폭발 효과를 생성하는 함수
function createRandomBurst() {
    let randomX = Math.random() * width;
    let randomY = Math.random() * height;
    
    // 클릭 효과와 유사하게 15개의 파티클을 랜덤 위치에 생성
    for (let i = 0; i < 15; i++) {
        points.push({
            x: randomX + (Math.random() - 0.5) * 50,
            y: randomY + (Math.random() - 0.5) * 50,
            radius: Math.random() * 4 + 1,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: Math.random() * 1 + 0.5,
            angle: Math.random() * Math.PI * 2
        });
    }
}

// Initialize the canvas
function initgeometry() {
    // Create initial points
    for (let i = 0; i < 30; i++) {
        points.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2 + 1,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: Math.random() * 0.5 + 0.2,
            angle: Math.random() * Math.PI * 2
        });
    }
    
    // Add event listeners (기존 마우스 이벤트는 그대로 유지)
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('click', handleClick);
    window.addEventListener('resize', handleResize);
    
    // Start animation
    animate();

    // <<< ADDED >>>
    // 2초마다 createRandomBurst 함수를 호출하여 자동 효과 생성
    setInterval(createRandomBurst, 2000); // 2000ms = 2 seconds
}

// Handle mouse move
function handleMouseMove(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    
    if (Math.random() > 0.7) {
        points.push({
            x: mouse.x + (Math.random() - 0.5) * 100,
            y: mouse.y + (Math.random() - 0.5) * 100,
            radius: Math.random() * 3 + 1,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: Math.random() * 0.5 + 0.2,
            angle: Math.random() * Math.PI * 2
        });
    }
}

// Handle click
function handleClick(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    
    for (let i = 0; i < 15; i++) {
        points.push({
            x: mouse.x + (Math.random() - 0.5) * 50,
            y: mouse.y + (Math.random() - 0.5) * 50,
            radius: Math.random() * 4 + 1,
            color: colors[Math.floor(Math.random() * colors.length)],
            speed: Math.random() * 1 + 0.5,
            angle: Math.random() * Math.PI * 2
        });
    }
}

// Handle window resize
function handleResize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
}

// Animation loop
function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, width, height);
    
    for (let i = 0; i < points.length; i++) {
        let point = points[i];
        
        point.x += Math.cos(point.angle) * point.speed;
        point.y += Math.sin(point.angle) * point.speed;
        point.radius -= 0.05;
        
        if (point.radius <= 0) {
            points.splice(i, 1);
            i--;
            continue;
        }
        
        ctx.beginPath();
        ctx.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
        ctx.fillStyle = point.color;
        ctx.fill();
        
        for (let j = i + 1; j < points.length; j++) {
            let otherPoint = points[j];
            let dx = point.x - otherPoint.x;
            let dy = point.y - otherPoint.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < 100) {
                ctx.beginPath();
                ctx.moveTo(point.x, point.y);
                ctx.lineTo(otherPoint.x, otherPoint.y);
                ctx.strokeStyle = `rgba(168, 216, 234, ${1 - distance/100})`;
                ctx.lineWidth = 0.5;
                ctx.stroke();
            }
        }
    }
}

// Initialize when page loads
window.addEventListener('load', initgeometry);
</script>
"""

# HTML for the canvas
canvas_html = """
<canvas id="geometryCanvas"></canvas>
"""

# Content
# CSS의 'content' 클래스를 적용하여 제목이 더 잘 보이도록 개선
st.markdown(
    """
    <div class="content">
        <h1 style="
            font-family: 'Arial', sans-serif;
            font-size: 3rem;
            color: #fcfdff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.4);
            text-align: center;
            ">
        Random Geometry Effect with Streamlit
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# HTML과 JS를 Streamlit에 렌더링
html(canvas_html + geometry_js, height=200)
