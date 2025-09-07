import streamlit as st
from streamlit.components.v1 import html

# Page configuration
st.set_page_config(
    page_title="Aurora Background",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)


def aurora_effect_01():
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

  # Inject aurora effect
  html(aurora_js, height=0)



def aurora_effect_02():
  # Custom CSS
  st.markdown("""
  <style>
  body { margin:0; overflow:hidden; }
  .content {
      position: relative;
      z-index: 1;
      background: rgba(255,255,255,0.08);
      padding: 2rem;
      border-radius: 20px;
      margin: 2rem auto;
      max-width: 900px;
      text-align: center;
      box-shadow: 0 8px 32px rgba(0,0,0,0.25);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,0.2);
  }
  #auroraCanvas {
      position: fixed;
      top:0; left:0;
      width:100vw; height:100vh;
      z-index:-1;
      pointer-events:none;
  }
  </style>
  """, unsafe_allow_html=True)

  # Aurora effect JS
  aurora_js = """
  <canvas id="auroraCanvas"></canvas>
  <script>
  const canvas = document.getElementById('auroraCanvas');
  const ctx = canvas.getContext('2d');
  let width = canvas.width = window.innerWidth;
  let height = canvas.height = window.innerHeight;

  // Color palettes
  const colors = [
      ['#ff9a9e','#fad0c4','#ffdde1'],
      ['#a1c4fd','#c2e9fb','#89f7fe'],
      ['#fbc2eb','#a6c1ee','#d9afd9'],
      ['#84fab0','#8fd3f4','#a6f77b']
  ];

  // Aurora layers
  const layers = [];
  for(let i=0;i<6;i++){
      layers.push({
          color: colors[Math.floor(Math.random()*colors.length)],
          yOffset: Math.random()*height,
          amplitude: Math.random()*150+100,
          wavelength: Math.random()*0.01+0.005,
          speed: Math.random()*0.01+0.1,
          alpha: Math.random()*0.3+0.2
      });
  }

  function drawAurora(){
      ctx.clearRect(0,0,width,height);
      layers.forEach(layer=>{
          ctx.beginPath();
          for(let x=0;x<width;x++){
              const y = layer.yOffset + Math.sin(x*layer.wavelength + Date.now()*0.002*layer.speed) * layer.amplitude;
              ctx.lineTo(x,y);
          }
          const grad = ctx.createLinearGradient(0,0,0,height);
          grad.addColorStop(0, layer.color[0]);
          grad.addColorStop(0.5, layer.color[1]);
          grad.addColorStop(1, layer.color[2]);
          ctx.fillStyle = grad;
          ctx.globalAlpha = layer.alpha;
          ctx.lineTo(width,height);
          ctx.lineTo(0,height);
          ctx.closePath();
          ctx.fill();
      });
      requestAnimationFrame(drawAurora);
  }

  drawAurora();

  window.addEventListener('resize', ()=>{
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
  });
  </script>
  """

  html(aurora_js, height=300)


if __name__ == "__main__":
    st.title("Aurora Background Effects")
    st.write("Explore different aurora-style animated background effects for your Streamlit apps.")

    st.header("Aurora Effect 01")
    aurora_effect_01()

    st.header("Aurora Effect 02")
    aurora_effect_02()    

