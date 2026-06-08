<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>听音跟读 UI - 终极高保真版</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

  :root {
    --bg-color: #7DBA45;         /* 修正为原图的青苹果绿 */
    --card-outer: #FDF3CC;       /* 外圈淡黄色 */
    --card-inner: #FFFFFF;
    --card-dash: #F5D381;
    --text-blue: #1A3E6D;        /* 更深的藏青色 */
    --btn-blue: #5B95F8;         /* 修正喇叭按钮蓝 */
    --btn-green: #68CD5E;        /* 修正我的音频绿 */
    --btn-orange: #FEA426;       /* 录音主色 */
    --btn-orange-dark: #FB861D;
    --btn-orange-shadow: #E26800;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    user-select: none;
    -webkit-user-select: none;
    -webkit-tap-highlight-color: transparent;
  }

  body {
    background-color: var(--bg-color);
    font-family: 'Nunito', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: hidden;
  }

  /* 核心容器 */
  .app-container {
    position: relative;
    width: 100vw;
    height: 56.25vw; /* 16:9 比例 */
    max-height: 100vh;
    max-width: 177.78vh;
    background-color: var(--bg-color);
    overflow: hidden;
    display: flex;
    justify-content: center;
  }

  /* ================= 顶部返回按钮 ================= */
  .back-btn {
    position: absolute;
    top: 5%;
    left: 3%;
    width: 5.5%;
    aspect-ratio: 1/1;
    background: var(--bg-color);
    border-radius: 1.5vw;
    border: 0.35vw solid #FFF;
    box-shadow: 0 0.4vw 0 rgba(0,0,0,0.08), inset 0 0.5vw 0.5vw rgba(255,255,255,0.4);
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    transition: transform 0.1s;
  }
  .back-btn:active { transform: scale(0.9) translateY(0.2vw); box-shadow: 0 0.1vw 0 rgba(0,0,0,0.08); }
  /* 粗壮的圆角返回箭头 */
  .back-btn svg { width: 55%; fill: #FFF; }

  /* ================= 中间主卡片 (趋近正方形) ================= */
  .main-card-wrap {
    position: absolute;
    top: 9%;
    width: 32%;
    aspect-ratio: 1 / 1.05;
    background: var(--card-outer);
    border-radius: 3vw;
    padding: 0.8vw;
    box-shadow: 0 1vw 0px rgba(0,0,0,0.06);
  }

  .main-card {
    width: 100%;
    height: 100%;
    background: var(--card-inner);
    border-radius: 2.2vw;
    border: 0.25vw dashed var(--card-dash);
    display: flex;
    flex-direction: column;
    position: relative;
  }

  /* 鸭子插图区 */
  .image-area {
    flex: 0.65;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }

  /* 底部淡蓝色阴影 */
  .duck-shadow {
    position: absolute;
    bottom: 8%;
    width: 50%;
    height: 12%;
    background: #DCEAF5;
    border-radius: 50%;
  }

  /* 精调版小黄鸭 SVG */
  .duck-svg {
    width: 60%;
    height: 80%;
    z-index: 2;
    transform: translateY(-2%);
  }

  /* 精简四芒星 */
  .card-sp {
    position: absolute;
    fill: #FFD64B;
  }
  .card-sp-1 { width: 1vw; left: 18%; top: 45%; }
  .card-sp-2 { width: 1.2vw; right: 15%; bottom: 25%; }
  .card-sp-3 { width: 0.6vw; right: 20%; top: 30%; opacity: 0.6; }

  /* 单词区 */
  .word-area {
    flex: 0.35;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 5.5vw;
    font-weight: 900;
    color: var(--text-blue);
    letter-spacing: 0.05vw;
    border-top: 0.25vw dashed var(--card-dash);
  }

  /* ================= 底部录音控制区 ================= */
  .controls-area {
    position: absolute;
    bottom: 3.5%;
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    gap: 4.5vw;
  }

  .control-group {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.8vw;
    cursor: pointer;
  }

  /* 粗体带阴影的文字 */
  .control-label {
    color: #FFF;
    font-size: 1.3vw;
    font-weight: 800;
    text-shadow: 0 0.2vw 0 rgba(0,0,0,0.15);
  }

  /* 侧边圆形按钮 (加厚白边) */
  .side-btn {
    width: 5.5vw;
    height: 5.5vw;
    border-radius: 50%;
    border: 0.4vw solid #FFF;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0.5vw 0px rgba(0,0,0,0.08), inset 0 0.6vw 0.5vw rgba(255,255,255,0.4);
    transition: transform 0.1s, box-shadow 0.1s;
    position: relative;
  }
  .side-btn.play-orig { background: var(--btn-blue); }
  .side-btn.play-mine { background: var(--btn-green); }
  
  /* 粗壮版图标 */
  .side-btn svg { width: 55%; fill: #FFF; }
  .side-btn:active {
    transform: scale(0.9);
    box-shadow: 0 0.1vw 0px rgba(0,0,0,0.08), inset 0 0.6vw 0.5vw rgba(255,255,255,0.4);
  }

  .control-group.is-locked { opacity: 0.5; filter: grayscale(0.6); pointer-events: none; }

  /* 中央录音大按钮 */
  .center-group { margin-bottom: 0.5vw; }
  .record-wrap {
    position: relative;
    width: 8.5vw;
    height: 8.5vw;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  /* 外围两圈光环 */
  .record-ring {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    border: 0.15vw solid rgba(255, 255, 255, 0.8);
    box-shadow: 0 0 1vw rgba(255,255,255,0.5), inset 0 0 0.5vw rgba(255,255,255,0.5);
    transition: all 0.3s;
  }
  .record-ring-outer {
    width: 115%; height: 115%;
    border: 0.2vw solid #A7E082; /* 原图的淡绿色外圈 */
    box-shadow: none;
  }

  /* 核心橙色按钮 */
  .record-btn {
    width: 82%;
    height: 82%;
    border-radius: 50%;
    background: linear-gradient(to bottom, var(--btn-orange), var(--btn-orange-dark));
    border: 0.35vw solid #FFF;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0.6vw 0px var(--btn-orange-shadow), inset 0 0.8vw 0.6vw rgba(255,255,255,0.4);
    z-index: 2;
    transition: transform 0.1s;
    position: relative;
  }
  
  /* 原图录音按钮上的两颗小星星 */
  .record-btn-sp { position: absolute; fill: #FFF; opacity: 0.9; }
  .record-btn-sp-1 { width: 0.8vw; top: 15%; left: 15%; }
  .record-btn-sp-2 { width: 0.6vw; bottom: 20%; right: 15%; }

  /* 粗壮版麦克风 */
  .record-btn svg { width: 45%; fill: #FFF; position: relative; z-index: 3;}
  .record-wrap:active .record-btn { transform: scale(0.9) translateY(0.2vw); box-shadow: 0 0.2vw 0px var(--btn-orange-shadow); }

  /* 录音波纹动效 */
  .is-playing::after {
    content: ''; position: absolute; width: 100%; height: 100%;
    border-radius: 50%; border: 0.3vw solid #FFF;
    animation: ripple 1s cubic-bezier(0.1, 0.8, 0.3, 1) infinite;
  }
  .center-group.is-recording .record-ring { animation: pulse-ring 1s ease-out infinite; }
  .center-group.is-recording .record-btn { background: #FF6B6B; box-shadow: 0 0.6vw 0px #C73535; }

  /* ================= 右下角 ================= */
  .bottom-right-controls {
    position: absolute;
    bottom: 5%;
    right: 4%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.8vw;
  }
  .next-btn {
    background: linear-gradient(to bottom, #FFC04B, #FF9418);
    border: 0.2vw solid #FFF;
    border-radius: 3vw;
    padding: 0.7vw 1.2vw;
    color: #FFF;
    font-size: 1.3vw;
    font-weight: 800;
    display: flex;
    align-items: center;
    gap: 0.2vw;
    cursor: pointer;
    box-shadow: 0 0.4vw 0 #E27200, 0 0.5vw 1vw rgba(0,0,0,0.1);
  }
  .next-btn:active { transform: scale(0.95) translateY(0.2vw); box-shadow: 0 0.1vw 0 #E27200; }
  /* 更贴近原图的箭头 */
  .next-btn svg { width: 1.2vw; fill: #FFF; margin-top: 0.1vw;}
  
  .skip-text { color: rgba(255,255,255,0.8); font-size: 1.1vw; font-weight: 700; cursor: pointer; }

  /* 粒子爆炸 */
  .click-particle { position: absolute; pointer-events: none; fill: #FFF; z-index: 100; animation: particle-fly 0.6s cubic-bezier(0.1, 0.8, 0.25, 1) forwards; }

  /* 动画关键帧 */
  @keyframes ripple { 0% { transform: scale(1); opacity: 0.8; } 100% { transform: scale(1.6); opacity: 0; } }
  @keyframes pulse-ring { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(1.6); opacity: 0; } }
  @keyframes particle-fly { 0% { transform: translate(-50%, -50%) scale(1); opacity: 1; } 100% { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0); opacity: 0; } }
  @keyframes bounce-unlock { 0% { transform: scale(0.8); } 50% { transform: scale(1.2); } 100% { transform: scale(1); } }
  
  .svg-defs { display: none; }
</style>
</head>
<body>

<svg class="svg-defs">
  <defs>
    <path id="star-path" d="M50 0 C50 30 70 50 100 50 C70 50 50 70 50 100 C50 70 30 50 0 50 C30 50 50 30 50 0 Z" />
  </defs>
</svg>

<div class="app-container" id="app">
  
  <button class="back-btn">
    <svg viewBox="0 0 24 24">
      <path d="M20 10.5H8.83l4.88-4.88c.58-.59.58-1.54 0-2.12-.59-.58-1.54-.58-2.12 0l-7.5 7.5c-.58.59-.58 1.54 0 2.12l7.5 7.5c.59.58 1.54.58 2.12 0 .58-.59.58-1.54 0-2.12L8.83 13.5H20c.83 0 1.5-.67 1.5-1.5s-.67-1.5-1.5-1.5z"/>
    </svg>
  </button>

  <div class="main-card-wrap">
    <div class="main-card">
      <div class="image-area">
        <svg viewBox="0 0 100 100" class="card-sp card-sp-1"><use href="#star-path"/></svg>
        <svg viewBox="0 0 100 100" class="card-sp card-sp-2"><use href="#star-path"/></svg>
        <svg viewBox="0 0 100 100" class="card-sp card-sp-3"><use href="#star-path"/></svg>
        
        <div class="duck-shadow"></div>
        
        <svg viewBox="0 0 200 200" class="duck-svg">
          <defs>
            <linearGradient id="body-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#FFEA45" />
              <stop offset="80%" stop-color="#FFC500" />
              <stop offset="100%" stop-color="#F29C00" />
            </linearGradient>
            <linearGradient id="beak-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#FF8A25" />
              <stop offset="100%" stop-color="#F25B00" />
            </linearGradient>
          </defs>
          
          <path d="M 50 145 C 30 145, 30 105, 70 100 C 90 95, 110 90, 120 105 C 130 120, 150 110, 160 95 C 170 85, 185 95, 180 115 C 170 145, 130 155, 90 155 C 70 155, 60 145, 50 145 Z" fill="url(#body-grad)" />
          
          <path d="M 60 125 C 50 135, 60 145, 80 145 C 90 145, 100 135, 80 125 Z" fill="#FFF" opacity="0.5" filter="blur(2px)"/>

          <path d="M 85 110 C 70 125, 90 145, 120 140 C 135 135, 145 115, 130 110 C 110 100, 95 95, 85 110 Z" fill="#FFB700" stroke="#F29C00" stroke-width="2" stroke-linejoin="round"/>
          <path d="M 95 120 C 105 130, 120 130, 125 125" fill="none" stroke="#F29C00" stroke-width="2" stroke-linecap="round"/>

          <circle cx="100" cy="65" r="38" fill="url(#body-grad)" />
          <ellipse cx="85" cy="45" rx="10" ry="6" fill="#FFF" opacity="0.6" transform="rotate(-20 85 45)" filter="blur(1px)"/>

          <path d="M 60 78 C 50 85, 70 95, 85 85" fill="#DD5000" />
          <path d="M 85 80 C 70 95, 40 85, 55 70 C 65 60, 75 65, 85 80 Z" fill="url(#beak-grad)" />
          
          <circle cx="110" cy="60" r="7.5" fill="#111" />
          <circle cx="108" cy="57" r="2.5" fill="#FFF" />
          <circle cx="113" cy="61" r="1" fill="#FFF" />
          
          <ellipse cx="128" cy="72" rx="6" ry="3.5" fill="#FF84A1" opacity="0.7"/>
        </svg>
      </div>
      
      <div class="word-area">duck</div>
    </div>
  </div>

  <div class="controls-area">
    <div class="control-group" id="btn-orig">
      <div class="side-btn play-orig">
        <svg viewBox="0 0 24 24">
          <path d="M14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77zM4 9v6h4l5 5V4L8 9H4z"/>
        </svg>
      </div>
      <div class="control-label">原音</div>
    </div>

    <div class="control-group center-group" id="btn-record">
      <div class="record-wrap">
        <div class="record-ring record-ring-outer"></div>
        <div class="record-ring"></div>
        <div class="record-btn">
          <svg viewBox="0 0 100 100" class="record-btn-sp record-btn-sp-1"><use href="#star-path"/></svg>
          <svg viewBox="0 0 100 100" class="record-btn-sp record-btn-sp-2"><use href="#star-path"/></svg>
          <svg viewBox="0 0 24 24">
             <rect x="8.5" y="2" width="7" height="11" rx="3.5" />
             <path d="M5 11v2a7 7 0 0014 0v-2" fill="none" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>
             <line x1="12" y1="20" x2="12" y2="23" stroke="#FFF" stroke-width="2.5" stroke-linecap="round"/>
          </svg>
        </div>
      </div>
      <div class="control-label" id="record-text">点击录音</div>
    </div>

    <div class="control-group is-locked" id="btn-mine">
      <div class="side-btn play-mine">
        <svg viewBox="0 0 24 24">
           <rect x="6" y="9" width="3" height="6" rx="1.5" />
           <rect x="10.5" y="4" width="3" height="16" rx="1.5" />
           <rect x="15" y="7" width="3" height="10" rx="1.5" />
        </svg>
      </div>
      <div class="control-label">我的音频</div>
    </div>
  </div>

  <div class="bottom-right-controls">
    <button class="next-btn">
      <span>下一题</span>
      <svg viewBox="0 0 24 24"><path d="M9.29 15.88L13.17 12 9.29 8.12c-.39-.39-.39-1.02 0-1.41.39-.39 1.02-.39 1.41 0l4.59 4.59c.39.39.39 1.02 0 1.41l-4.59 4.59c-.39.39-1.02.39-1.41 0-.38-.39-.38-1.03 0-1.42z"/></svg>
    </button>
    <div class="skip-text">我不会 ></div>
  </div>

</div>

<script>
  // 保持核心交互逻辑不变
  const appContainer = document.getElementById('app');
  const btnOrig = document.getElementById('btn-orig');
  const btnRecord = document.getElementById('btn-record');
  const btnMine = document.getElementById('btn-mine');
  const recordText = document.getElementById('record-text');
  
  let isRecording = false;

  function createParticles(x, y, count, colors) {
    for (let i = 0; i < count; i++) {
      const svgNS = "http://www.w3.org/2000/svg";
      const particle = document.createElementNS(svgNS, "svg");
      particle.setAttribute("viewBox", "0 0 100 100");
      particle.classList.add("click-particle");
      particle.style.fill = colors[Math.floor(Math.random() * colors.length)];
      
      const useElement = document.createElementNS(svgNS, "use");
      useElement.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#star-path");
      particle.appendChild(useElement);

      const size = (Math.random() * 1.5 + 0.8).toFixed(2);
      particle.style.width = `${size}vw`; particle.style.height = `${size}vw`;
      particle.style.left = `${x}px`; particle.style.top = `${y}px`;

      const angle = (Math.random() * 360) * (Math.PI / 180);
      const distance = Math.random() * 8 + 4;
      particle.style.setProperty('--dx', `${(Math.cos(angle) * distance).toFixed(2)}vw`);
      particle.style.setProperty('--dy', `${(Math.sin(angle) * distance).toFixed(2)}vw`);

      appContainer.appendChild(particle);
      particle.addEventListener('animationend', () => particle.remove());
    }
  }

  function playAudioAnimation(element) {
    const btn = element.querySelector('.side-btn');
    btn.classList.remove('is-playing');
    void btn.offsetWidth;
    btn.classList.add('is-playing');
    
    const rect = btn.getBoundingClientRect();
    const containerRect = appContainer.getBoundingClientRect();
    createParticles(
      rect.left + rect.width/2 - containerRect.left, 
      rect.top + rect.height/2 - containerRect.top, 
      6, ['#FFF', '#FFD238', '#4DA2FF']
    );

    setTimeout(() => { btn.classList.remove('is-playing'); }, 1200);
  }

  btnOrig.addEventListener('click', () => playAudioAnimation(btnOrig));
  btnMine.addEventListener('click', () => {
    if(!btnMine.classList.contains('is-locked')) playAudioAnimation(btnMine);
  });

  btnRecord.addEventListener('click', (e) => {
    if(isRecording) return;
    isRecording = true;
    
    btnRecord.classList.add('is-recording');
    recordText.innerText = '正在录音...';

    const rect = e.currentTarget.getBoundingClientRect();
    const containerRect = appContainer.getBoundingClientRect();
    createParticles(
      rect.left + rect.width/2 - containerRect.left, 
      rect.top + rect.height/2 - containerRect.top, 
      12, ['#FFF', '#FF6B6B', '#FFD238']
    );

    setTimeout(() => {
      btnRecord.classList.remove('is-recording');
      recordText.innerText = '重新录音';
      isRecording = false;

      if(btnMine.classList.contains('is-locked')){
        btnMine.classList.remove('is-locked');
        btnMine.style.animation = 'bounce-unlock 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
        setTimeout(()=> { btnMine.style.animation = ''; }, 500);
      }
    }, 2500);
  });
</script>

</body>
</html>