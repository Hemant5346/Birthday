import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="A Magical Love Game 💖", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<style>
html,body{margin:0;padding:0;width:100%;height:100%;overflow:hidden;background:radial-gradient(circle at top,#ffe6f1,#ffd1e8,#fff);font-family:'Poppins',sans-serif;}
.game{width:100%;height:100%;display:flex;justify-content:center;align-items:center;}
.card{width:90%;max-width:600px;padding:40px 30px;border-radius:36px;background:rgba(255,255,255,0.94);backdrop-filter:blur(12px);box-shadow:0 40px 90px rgba(255,105,180,0.35);text-align:center;}
.screen{display:none;}
.screen.active{display:block;}
h1{font-family:'Pacifico',cursive;color:#ff4f9a;font-size:2.8rem;}
p{color:#555;line-height:1.8;font-size:1.1rem;margin-bottom:30px;}
.tap-area{margin-top:30px;padding:18px;background:linear-gradient(135deg,#ff4f9a,#ff8fc1);color:white;border-radius:999px;font-size:1.1rem;cursor:pointer;user-select:none;}
.progress{margin-top:18px;color:#999;font-size:0.9rem;}
.heart{position:fixed;font-size:24px;animation:floatUp 2.5s ease forwards;pointer-events:none;}
@keyframes floatUp{from{transform:translateY(0) scale(1);opacity:1;}to{transform:translateY(-140px) scale(1.6);opacity:0;}}
.rain{position:fixed;top:-40px;animation:fall 4s linear forwards;}
@keyframes fall{to{transform:translateY(120vh);opacity:0;}}
.glow{width:60px;height:60px;border-radius:50%;position:absolute;background:radial-gradient(circle, #ff85c2 0%, rgba(255,95,162,0) 70%);animation:move 3s linear infinite;}
@keyframes move{0%{transform:translate(0,0);}100%{transform:translate(300px,200px);}}
.confetti{position:fixed;width:10px;height:10px;background:#ff4f9a;animation:confettiFall 4s linear forwards;pointer-events:none;}
@keyframes confettiFall{0%{transform:translateY(0);}100%{transform:translateY(120vh) rotate(360deg);opacity:0;}}
.big-message{font-size:1.2rem;line-height:1.9;color:#ff4f9a;margin-top:20px;}
</style>
</head>
<body>

<audio id="bgm" loop>
<source src="https://cdn.pixabay.com/audio/2023/04/16/audio_9e6a6eae1f.mp3">
</audio>
<audio id="pop">
<source src="https://cdn.pixabay.com/audio/2022/03/10/audio_4b2d8a9a84.mp3">
</audio>

<div class="game">
<div class="card">

<!-- SCREEN 1 -->
<div class="screen active" id="s1">
<h1>Tap Anywhere 💕</h1>
<p>Every tap is a little reminder of how special you are 💕</p>
<div class="tap-area" onclick="burst(); next(2)">Start Tapping ✨</div>
<div class="progress">1 / 6</div>
</div>

<!-- SCREEN 2 -->
<div class="screen" id="s2">
<h1>Collect the Hearts 💖</h1>
<p>Each heart you collect brings more love 💖</p>
<div class="tap-area" onclick="countTap()">Tap ❤️ <span id="count">0</span>/5</div>
<div class="progress">2 / 6</div>
</div>

<!-- SCREEN 3 -->
<div class="screen" id="s3">
<h1>Let It Rain 🌸</h1>
<p>Sometimes love falls softly, just like these hearts 🌸</p>
<div class="tap-area" onclick="rain(); next(4)">Make it Rain 💞</div>
<div class="progress">3 / 6</div>
</div>

<!-- SCREEN 4 -->
<div class="screen" id="s4">
<h1>Follow the Glow ✨</h1>
<p>Sometimes you need to follow the light… that’s how I feel about you ✨</p>
<div class="tap-area" onclick="startGlow(); next(5)">Follow 💗</div>
<div class="progress">4 / 6</div>
</div>

<!-- SCREEN 5 -->
<div class="screen" id="s5">
<h1>One Last Tap 💗</h1>
<p>Almost there… every tap shows how much I care 💗</p>
<div class="tap-area" onclick="finalTap()">Tap ✨ <span id="final">0</span>/7</div>
<div class="progress">5 / 6</div>
</div>

<!-- SCREEN 6: FINAL BIG MESSAGE -->
<div class="screen" id="s6">
<h1>Happy Birthday 🎉</h1>
<p class="big-message">
From the bottom of my heart, I hope today fills you with as much joy as you bring to everyone around you.  
You are amazing, beautiful, and loved more than words can express.  
Every moment with you is a treasure, and I hope this little game made you smile and feel special.  
May your day be magical, your heart light, and your smile brighter than the stars.  
Always remember… you are cherished, appreciated, and truly wonderful. 💖💞✨
</p>
<div class="progress">6 / 6 — Complete 💝</div>
</div>

</div>
</div>

<script>
const bgm=document.getElementById("bgm");
bgm.volume=0.5; bgm.play();

function next(n){
 document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
 document.getElementById('s'+n).classList.add('active');
}

function burst(){
 document.getElementById("pop").play();
 for(let i=0;i<15;i++){
  let h=document.createElement("div");
  h.className="heart";
  h.innerHTML="💖";
  h.style.left=Math.random()*100+"vw";
  h.style.bottom="20px";
  document.body.appendChild(h);
  setTimeout(()=>h.remove(),2500);
 }
}

let taps=0;
function countTap(){
 burst();
 taps++;
 document.getElementById("count").innerText=taps;
 if(taps>=5) next(3);
}

function rain(){
 for(let i=0;i<25;i++){
  let r=document.createElement("div");
  r.className="rain";
  r.innerHTML="💗";
  r.style.left=Math.random()*100+"vw";
  r.style.fontSize=(18+Math.random()*18)+"px";
  document.body.appendChild(r);
  setTimeout(()=>r.remove(),4000);
 }
}

function startGlow(){
 for(let i=0;i<10;i++){
  let g=document.createElement("div");
  g.className="glow";
  g.style.top=Math.random()*70+"%";
  g.style.left=Math.random()*70+"%";
  document.body.appendChild(g);
  setTimeout(()=>g.remove(),6000);
 }
}

let final=0;
function finalTap(){
 burst();
 final++;
 document.getElementById("final").innerText=final;
 if(final>=7){
   for(let i=0;i<50;i++){
     let c=document.createElement("div");
     c.className="confetti";
     c.style.left=Math.random()*100+"vw";
     c.style.background=["#ff4f9a","#ff85c2","#ffd1e8","#ffe6f1"][Math.floor(Math.random()*4)];
     document.body.appendChild(c);
     setTimeout(()=>c.remove(),4000);
   }
   next(6);
 }
}
</script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=False)
