import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Aurora Background",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for aurora background
st.markdown("""
<style>
    body {
        margin: 0;
        overflow: hidden;
    }

    /* Content styling */
    .content {
        position: relative;
        z-index: 1;
        background: rgba(255, 255, 255, 0.08);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem auto;
        max-width: 900px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    #auroraCanvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

# Aurora Background Effect
aurora_js = """
<canvas id="auroraCanvas"></canvas>
<script>
let canvas = document.getElementById("auroraCanvas");
let ctx = canvas.getContext("2d");
let width = window.innerWidth;
let height = window.innerHeight;
canvas.width = width;
canvas.height = height;

let gradients = [];
let colors = [
  ["#ff9a9e", "#fad0c4"],
  ["#a1c4fd", "#c2e9fb"],
  ["#fbc2eb", "#a6c1ee"],
  ["#84fab0", "#8fd3f4"]
];

// Gradient objects
for (let i = 0; i < 5; i++) {
  gradients.push({
    x: Math.random() * width,
    y: Math.random() * height,
    r: Math.random() * 600 + 400,
    dx: (Math.random() - 0.5) * 0.6,
    dy: (Math.random() - 0.5) * 0.6,
    color: colors[Math.floor(Math.random() * colors.length)]
  });
}

// Draw loop
function animate() {
  ctx.clearRect(0, 0, width, height);

  gradients.forEach((g) => {
    let gradient = ctx.createRadialGradient(g.x, g.y, 0, g.x, g.y, g.r);
    gradient.addColorStop(0, g.color[0]);
    gradient.addColorStop(1, g.color[1]);
    
    ctx.fillStyle = gradient;
    ctx.globalAlpha = 0.35;
    ctx.beginPath();
    ctx.arc(g.x, g.y, g.r, 0, Math.PI * 2);
    ctx.fill();

    g.x += g.dx;
    g.y += g.dy;

    if (g.x < -g.r) g.x = width + g.r;
    if (g.y < -g.r) g.y = height + g.r;
    if (g.x > width + g.r) g.x = -g.r;
    if (g.y > height + g.r) g.y = -g.r;
  });

  requestAnimationFrame(animate);
}

animate();

window.addEventListener("resize", () => {
  width = window.innerWidth;
  height = window.innerHeight;
  canvas.width = width;
  canvas.height = height;
});
</script>
"""

# Content
st.markdown(
    """
    <div class="content">
        <h1 style="
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 3rem;
            color: #ffffff;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
        ">
        ✨ Aurora Gradient Wave Effect ✨
        </h1>
        <p style="color:#f0f0f0; font-size:1.2rem;">
        A soft, modern aurora-style animated background for Streamlit apps.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Inject aurora effect
html(aurora_js, height=0)
