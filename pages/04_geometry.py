import streamlit as st
import numpy as np
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="geometry Wave Background",
    page_icon="🌊",
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
        z-index: -1;
        pointer-events: none;
    }
    
    /* Content styling */
    .content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
    }
    
    /* Title styling */
    .title {
        font-size: 3rem;
        color: #1f3a60;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Text styling */
    .text {
        font-size: 1.2rem;
        color: #2c3e50;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# JavaScript for the geometry effect
geometry_js = """
<script>
// Initialize variables
let canvas, ctx;
let points = [];
let width, height;
let mouse = {x: 0, y: 0};
let colors = ['#ff9a9e', '#fad0c4', '#a1c4fd', '#c2e9fb', '#ffecd2', '#fcb69f'];

// Initialize the canvas
function initgeometry() {
    canvas = document.getElementById('geometryCanvas');
    ctx = canvas.getContext('2d');
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width;
    canvas.height = height;
    
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
    
    // Add event listeners
    document.addEventListener('mousemove', handleMouseMove);
    document.addEventListener('click', handleClick);
    window.addEventListener('resize', handleResize);
    
    // Start animation
    animate();
}

// Handle mouse move
function handleMouseMove(e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    
    // Add a point near the mouse
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
    
    // Create a geometry effect on click
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
    
    // Clear canvas with a slight fade effect
    ctx.fillStyle = 'rgba(248, 249, 250, 0.2)';
    ctx.fillRect(0, 0, width, height);
    
    // Update and draw points
    for (let i = 0; i < points.length; i++) {
        let point = points[i];
        
        // Move point
        point.x += Math.cos(point.angle) * point.speed;
        point.y += Math.sin(point.angle) * point.speed;
        
        // Shrink point
        point.radius -= 0.05;
        
        // Remove points that are too small
        if (point.radius <= 0) {
            points.splice(i, 1);
            i--;
            continue;
        }
        
        // Draw point
        ctx.beginPath();
        ctx.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
        ctx.fillStyle = point.color;
        ctx.fill();
        
        // Draw connecting lines between nearby points
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

# Combine everything
# html(canvas_html + geometry_js, width=500, height=500)

# Content
# st.markdown('<div class="stMainBlockContainer">', unsafe_allow_html=True)
st.markdown(
        """
        <h1 style="
            font-family: 'Arial';
            font-size: 60px;
            color: #fcfdff;
            text-shadow: 2px 2px 4px #aaa;
            text-align: center;
            ">
        Geometry Effect with Streamlit
        </h1>
        """,
        unsafe_allow_html=True
    )

# Add some sample controls
col1, col2 = st.columns(2)
with col1:
    speed = st.slider("Animation Speed", 0.5, 2.0, 1.0, 0.1)
with col2:
    density = st.slider("geometry Density", 10, 50, 30, 5)

st.markdown("""
<p class="text">
Adjust the sliders to change the animation behavior. The changes will take effect on the next interaction.
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

l1_container = st.container(horizontal=True, height="stretch")
with l1_container:
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height="stretch"):
        html(canvas_html + geometry_js, height=300)
    with st.container(horizontal=False, border=True, width="stretch", vertical_alignment="top", height="stretch"):
        html(canvas_html + geometry_js, height=300)