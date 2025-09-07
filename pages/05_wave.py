import streamlit as st
from streamlit.components.v1 import html
import random

# Page configuration
st.set_page_config(
    page_title="Ripple Wave Background",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        position: relative;
        overflow: hidden;
    }
    
    /* Canvas for the ripple effect */
    #rippleCanvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        pointer-events: all;
    }
    
    /* Content styling */
    .content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.85);
        padding: 2.5rem;
        border-radius: 18px;
        margin: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.5);
    }
    
    /* Title styling */
    .title {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #0061ff, #60efff);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        margin-bottom: 1.5rem;
        text-align: center;
        font-weight: 800;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Text styling */
    .text {
        font-size: 1.25rem;
        color: #2c3e50;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #0061ff, #60efff);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(0, 97, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 97, 255, 0.4);
    }
    
    /* Slider styling */
    .stSlider>div>div>div {
        background: linear-gradient(45deg, #0061ff, #60efff);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for the ripple effect
ripple_js = """
<script>
// Initialize variables
let canvas, ctx;
let ripples = [];
let width, height;
let mouse = {x: 0, y: 0, moved: false};

// Ripple class
class Ripple {
    constructor(x, y, radius, color, speed) {
        this.x = x;
        this.y = y;
        this.initialRadius = radius;
        this.radius = radius;
        this.maxRadius = radius + Math.random() * 100 + 50;
        this.color = color;
        this.speed = speed;
        this.alpha = 1;
        this.life = 1;
    }
    
    draw() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(${this.color}, ${this.alpha})`;
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Draw inner circle for better visual effect
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius * 0.7, 0, Math.PI * 2);
        ctx.strokeStyle = `rgba(${this.color}, ${this.alpha * 0.6})`;
        ctx.lineWidth = 1;
        ctx.stroke();
    }
    
    update() {
        this.radius += this.speed;
        this.life -= 0.01;
        this.alpha = this.life;
        
        if (this.life <= 0) {
            return false;
        }
        return true;
    }
}

// Initialize the canvas
function initRipple() {
    canvas = document.getElementById('rippleCanvas');
    ctx = canvas.getContext('2d');
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
    
    // Add event listeners
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('click', handleClick);
    document.addEventListener('touchmove', handleTouchMove, {passive: false});
    window.addEventListener('resize', handleResize);
    
    // Start animation
    animate();
}

// Handle mouse move
function handleMouseMove(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.moved = true;
}

// Handle touch move
function handleTouchMove(e) {
    if (e.touches.length > 0) {
        mouse.x = e.touches[0].clientX;
        mouse.y = e.touches[0].clientY;
        mouse.moved = true;
        
        // Create ripples on touch move
        if (Math.random() > 0.7) {
            createRipple();
        }
    }
    e.preventDefault();
}

// Handle click
function handleClick(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    createRipple();
    
    // Create additional ripples around the click point
    for (let i = 0; i < 3; i++) {
        setTimeout(() => {
            createRipple(
                mouse.x + (Math.random() - 0.5) * 100,
                mouse.y + (Math.random() - 0.5) * 100
            );
        }, i * 150);
    }
}

// Create a new ripple
function createRipple(x = null, y = null) {
    const rippleX = x || mouse.x;
    const rippleY = y || mouse.y;
    const colors = [
        '0, 97, 255',  // Blue
        '96, 239, 255', // Light blue
        '0, 200, 255',  // Cyan
        '0, 150, 255'   // Deep blue
    ];
    
    ripples.push(new Ripple(
        rippleX,
        rippleY,
        Math.random() * 5 + 5,
        colors[Math.floor(Math.random() * colors.length)],
        Math.random() * 0.8 + 0.5
    ));
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
    
    // Clear canvas with a slight fade effect (배경 투명효과)
    ctx.clearRect(0, 0, width, height);
    
    // Create random ripples occasionally
    if (Math.random() > 0.97) {
        createRipple(
            Math.random() * width,
            Math.random() * height
        );
    }
    
    // Create ripple when mouse moves
    if (mouse.moved && Math.random() > 0.8) {
        createRipple();
        mouse.moved = false;
    }
    
    // Update and draw ripples
    for (let i = 0; i < ripples.length; i++) {
        if (ripples[i].update()) {
            ripples[i].draw();
        } else {
            ripples.splice(i, 1);
            i--;
        }
    }
}

// Initialize when page loads
window.addEventListener('load', initRipple);
</script>
"""

# HTML for the canvas
canvas_html = """
<canvas id="rippleCanvas"></canvas>
"""


# Content
# st.markdown('<div class="content">', unsafe_allow_html=True)
st.markdown(
        """
        <h1 style="
            font-family: 'Arial';
            font-size: 60px;
            color: #fcfdff;
            text-shadow: 2px 2px 4px #aaa;
            text-align: center;
            ">
        Ripple Drop Wave Effect with Streamlit
        </h1>
        """,
        unsafe_allow_html=True
    )

# Add some sample controls
# col1, col2 = st.columns(2)
# with col1:
#     speed = st.slider("Animation Speed", 0.5, 2.0, 1.0, 0.1)
# with col2:
#     density = st.slider("Ripple Density", 10, 50, 30, 5)


st.markdown("""
<p class="text">
Adjust the sliders to change the animation behavior. The changes will take effect on the next interaction.
</p>
""", unsafe_allow_html=True)


html(canvas_html + ripple_js, height=0)