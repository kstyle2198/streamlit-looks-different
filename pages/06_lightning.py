import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Gray Lightning Effect",
    page_icon="⚡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling (Light Theme)
st.markdown("""
<style>
    /* Body background for light theme */
    body {
        background-color: #FFFFFF;
    }

    /* Main container styling */
    .main {
        position: relative;
        overflow: hidden;
    }
    
    /* Canvas for the lightning effect */
    #lightningCanvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    
    /* Content styling */
    .content {
        position: relative;
        z-index: 1;
        background: rgba(245, 245, 245, 0.75); /* Light, translucent background */
        padding: 2.5rem;
        border-radius: 18px;
        margin: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(45deg, #6c757d, #adb5bd);
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for the lightning effect (Gray version)
lightning_js = """
<script>
// Initialize variables
let canvas, ctx;
let lightningBolts = [];
let width, height;
let flashAlpha = 0;

// Lightning class to create and manage a single bolt
class Lightning {
    constructor(x, y, segments, branches) {
        this.x = x;
        this.y = y;
        this.segments = [];
        this.alpha = 1;
        this.life = 1;
        
        // --- COLOR CHANGE: Set to a random gray value ---
        const grayValue = Math.floor(Math.random() * 100) + 80; // from 80 to 180
        this.color = `rgba(${grayValue}, ${grayValue}, ${grayValue}, ${Math.random() * 0.4 + 0.6})`;
        
        this.branchOut = branches;

        // Create the main path of the lightning
        let currentPoint = { x: this.x, y: this.y };
        this.segments.push(currentPoint);

        for (let i = 0; i < segments; i++) {
            const angle = Math.atan2(height, width/2) + (Math.random() - 0.5) * 0.5;
            const length = Math.random() * 20 + 10;
            const nextPoint = {
                x: currentPoint.x + Math.cos(angle) * length,
                y: currentPoint.y + Math.sin(angle) * length
            };
            this.segments.push(nextPoint);
            currentPoint = nextPoint;

            // Chance to create a branch
            if (this.branchOut && Math.random() > 0.85 && this.segments.length < segments - 5) {
                lightningBolts.push(new Lightning(currentPoint.x, currentPoint.y, segments - this.segments.length, false));
            }
        }
    }

    draw() {
        if (this.alpha <= 0) return;
        ctx.beginPath();
        ctx.moveTo(this.segments[0].x, this.segments[0].y);
        for (let i = 1; i < this.segments.length; i++) {
            ctx.lineTo(this.segments[i].x, this.segments[i].y);
        }
        ctx.strokeStyle = this.color.replace(/, ([0-9\.]+)\)/, `, ${this.alpha})`);
        ctx.lineWidth = Math.random() * 1.5 + 0.5;
        
        // --- GLOW CHANGE: Set to gray for depth ---
        ctx.shadowColor = 'gray';
        ctx.shadowBlur = 15;
        
        ctx.stroke();
        ctx.shadowBlur = 0; // Reset shadow
    }

    update() {
        this.life -= 0.02;
        this.alpha = this.life;
        return this.life > 0;
    }
}

// Initialize the canvas
function initLightning() {
    canvas = document.getElementById('lightningCanvas');
    ctx = canvas.getContext('2d');
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;

    document.addEventListener('click', handleClick);
    window.addEventListener('resize', handleResize);

    animate();
}

// Handle click to create lightning
function handleClick(e) {
    createLightning(e.clientX, 0);
}

// Create a new lightning bolt
function createLightning(x, y) {
    lightningBolts.push(new Lightning(x, y, 30, true));
    flashAlpha = 0.4; // Trigger screen flash (less intense)
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

    // --- BACKGROUND CHANGE: Use semi-transparent white for fade-out effect on light bg ---
    ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';
    ctx.fillRect(0, 0, width, height);

    // Create random lightning strikes occasionally
    if (Math.random() > 0.985) {
        createLightning(Math.random() * width, 0);
    }

    // Update and draw lightning bolts
    for (let i = lightningBolts.length - 1; i >= 0; i--) {
        if (lightningBolts[i].update()) {
            lightningBolts[i].draw();
        } else {
            lightningBolts.splice(i, 1);
        }
    }

    // --- FLASH CHANGE: Use a gray flash ---
    if (flashAlpha > 0) {
        ctx.fillStyle = `rgba(128, 128, 128, ${flashAlpha})`;
        ctx.fillRect(0, 0, width, height);
        flashAlpha -= 0.05; // Fade out the flash
    }
}

// Initialize when page loads
window.addEventListener('load', initLightning);
</script>
"""

# HTML for the canvas
canvas_html = '<canvas id="lightningCanvas"></canvas>'

# Main content wrapped in a styled div

st.markdown(
    """
    <h1 style="
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        color: #333333; /* Dark gray text */
        text-shadow: 1px 1px 3px #aaaaaa;
        text-align: center;
    ">
    Gray Lightning Effect
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="font-size: 1.1rem; color: #555555; text-align: center; line-height: 1.7;">
    This is a demonstration of a dynamic background effect using Streamlit, HTML Canvas, and JavaScript. 
    Click anywhere on the background to trigger a lightning strike! ⚡️
    </p>
    """,
    unsafe_allow_html=True
)

# Inject the HTML and JavaScript into the Streamlit app
html(canvas_html + lightning_js, height=0)