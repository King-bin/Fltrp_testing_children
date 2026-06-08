<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>听音选图 UI - 高保真互动版</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

  :root {
    --bg-color: #9AA96B;         /* 莫兰迪橄榄绿背景 */
    --card-outer: #FCE18D;       /* 卡片外圈淡黄色 */
    --card-inner: #FCFAF2;
    --card-dash: #F5D381;
    --badge-top: #FFC458;        /* 选项角标渐变 */
    --badge-bottom: #F9981D;
    --audio-green-top: #78E949;  /* 音频按钮渐变 */
    --audio-green-bottom: #45B91B;
    --btn-orange: #FFAC32;       /* 下一题按钮 */
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

  /* 核心容器 (16:9 横屏比例) */
  .app-container {
    position: relative;
    width: 100vw;
    height: 56.25vw; 
    max-height: 100vh;
    max-width: 177.78vh;
    background-color: var(--bg-color);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
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
    box-shadow: 0 0.4vw 0 rgba(0,0,0,0.1), inset 0 0.5vw 0.5vw rgba(255,255,255,0.4);
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    transition: transform 0.1s;
  }
  .back-btn:active { transform: scale(0.9) translateY(0.2vw); box-shadow: 0 0.1vw 0 rgba(0,0,0,0.1); }
  .back-btn svg { width: 55%; fill: #FFF; }

  /* ================= 顶部音频播放中心 ================= */
  .audio-center {
    position: absolute;
    top: 10%;
    width: 8vw;
    height: 8vw;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  /* 悬浮光环 */
  .audio-ring {
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
  }
  .ring-1 {
    width: 140%; height: 140%;
    border: 0.15vw dashed rgba(255,255,255,0.6);
    animation: spin 15s linear infinite;
  }
  .ring-2 {
    width: 175%; height: 175%;
    border: 0.2vw dotted rgba(255,255,255,0.4);
    animation: spin-reverse 20s linear infinite;
  }

  /* 音频实体按钮 */
  .audio-btn {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(to bottom, var(--audio-green-top), var(--audio-green-bottom));
    border: 0.3vw solid rgba(255,255,255,0.3);
    box-shadow: 0 0.6vw 0px rgba(45, 126, 17, 0.6), inset 0 0.8vw 0.5vw rgba(255,255,255,0.4), 0 0 1.5vw rgba(120, 233, 73, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    z-index: 2;
    transition: transform 0.1s, box-shadow 0.1s;
  }
  .audio-btn svg { width: 50%; fill: #FFF; filter: drop-shadow(0 0.2vw 0 rgba(0,0,0,0.1)); margin-left: 0.3vw;}
  .audio-btn:active { transform: scale(0.92) translateY(0.4vw); box-shadow: 0 0.2vw 0px rgba(45, 126, 17, 0.6), inset 0 0.8vw 0.5vw rgba(255,255,255,0.4); }

  /* ================= 选项卡片区域 ================= */
  .options-container {
    position: absolute;
    top: 50%;
    transform: translateY(-40%);
    width: 85%;
    display: flex;
    justify-content: space-between;
    gap: 3vw;
  }

  .option-card-wrap {
    flex: 1;
    aspect-ratio: 1.1 / 1;
    background: var(--card-outer);
    border-radius: 2.5vw;
    padding: 0.6vw;
    box-shadow: 0 0.8vw 0px rgba(0,0,0,0.1);
    position: relative;
    cursor: pointer;
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.3s, opacity 0.3s;
  }

  .option-card {
    width: 100%;
    height: 100%;
    background: var(--card-inner);
    border-radius: 2vw;
    border: 0.25vw dashed var(--card-dash);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
  }

  /* A/B/C 角标 */
  .badge {
    position: absolute;
    top: -0.5vw;
    left: -0.5vw;
    width: 3.5vw;
    height: 3.5vw;
    border-radius: 50%;
    background: linear-gradient(to bottom, var(--badge-top), var(--badge-bottom));
    border: 0.25vw solid #FFF;
    color: #FFF;
    font-size: 2vw;
    font-weight: 900;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0.3vw 0px rgba(0,0,0,0.1);
    z-index: 5;
  }

  /* 插画缩放区 */
  .illu-svg {
    width: 70%;
    height: 70%;
    filter: drop-shadow(0 0.6vw 0.4vw rgba(0,0,0,0.1));
    z-index: 2;
  }

  /* ================= 交互动效状态 ================= */
  .option-card-wrap:active { transform: scale(0.95); }

  /* 选中状态：Q弹放大，外发光 */
  .option-card-wrap.is-selected {
    transform: scale(1.08) translateY(-1vw);
    box-shadow: 0 1vw 0px rgba(0,0,0,0.15), 0 0 2vw rgba(252, 225, 141, 0.8);
    z-index: 10;
    animation: bounce-select 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  }
  
  /* 未被选中的变暗状态 */
  .option-card-wrap.is-dimmed {
    opacity: 0.5;
    filter: grayscale(0.3);
    transform: scale(0.95);
  }

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
    box-shadow: 0 0.4vw 0 var(--btn-orange-shadow), 0 0.5vw 1vw rgba(0,0,0,0.1);
    transition: opacity 0.3s, filter 0.3s, transform 0.1s;
  }
  .next-btn:active { transform: scale(0.95) translateY(0.2vw); box-shadow: 0 0.1vw 0 var(--btn-orange-shadow); }
  .next-btn.is-disabled { opacity: 0.5; filter: grayscale(0.5); pointer-events: none; }
  .next-btn svg { width: 1.2vw; fill: #FFF; margin-top: 0.1vw;}
  
  .skip-text { color: rgba(255,255,255,0.8); font-size: 1.1vw; font-weight: 700; cursor: pointer; }

  /* ================= 粒子 & 波纹 ================= */
  .click-particle { position: absolute; pointer-events: none; fill: #FFF; z-index: 100; animation: particle-fly 0.6s cubic-bezier(0.1, 0.8, 0.25, 1) forwards; }
  
  .audio-pulse::after {
    content: ''; position: absolute; top:0; left:0; width: 100%; height: 100%;
    border-radius: 50%; border: 0.4vw solid rgba(255,255,255,0.8);
    animation: ripple 1s cubic-bezier(0.1, 0.8, 0.3, 1) forwards; pointer-events: none;
  }

  /* 动画关键帧 */
  @keyframes spin { 100% { transform: rotate(360deg); } }
  @keyframes spin-reverse { 100% { transform: rotate(-360deg); } }
  @keyframes ripple { 0% { transform: scale(1); opacity: 0.8; } 100% { transform: scale(2); opacity: 0; } }
  @keyframes particle-fly { 0% { transform: translate(-50%, -50%) scale(1); opacity: 1; } 100% { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0); opacity: 0; } }
  @keyframes bounce-select { 0% { transform: scale(1); } 50% { transform: scale(1.12) translateY(-1.5vw); } 100% { transform: scale(1.08) translateY(-1vw); } }
  
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
    <svg viewBox="0 0 24 24"><path d="M20 10.5H8.83l4.88-4.88c.58-.59.58-1.54 0-2.12-.59-.58-1.54-.58-2.12 0l-7.5 7.5c-.58.59-.58 1.54 0 2.12l7.5 7.5c.59.58 1.54.58 2.12 0 .58-.59.58-1.54 0-2.12L8.83 13.5H20c.83 0 1.5-.67 1.5-1.5s-.67-1.5-1.5-1.5z"/></svg>
  </button>

  <div class="audio-center">
    <div class="audio-ring ring-1"></div>
    <div class="audio-ring ring-2"></div>
    <div class="audio-btn" id="btn-audio">
      <svg viewBox="0 0 24 24"><path d="M14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77zM4 9v6h4l5 5V4L8 9H4z"/></svg>
    </div>
  </div>

  <div class="options-container">
    
    <div class="option-card-wrap" data-index="0">
      <div class="badge">A</div>
      <div class="option-card">
        <svg viewBox="0 0 200 200" class="illu-svg">
          <ellipse cx="100" cy="170" rx="60" ry="12" fill="rgba(0,0,0,0.06)" />
          <polygon points="65,90 75,90 70,165 60,160" fill="#B96720"/>
          <polygon points="135,90 145,90 145,160 135,165" fill="#A45513"/>
          
          <polygon points="65,40 75,40 75,100 65,100" fill="#E6953D"/>
          <polygon points="60,40 65,40 65,100 60,100" fill="#F8B15F"/>
          <polygon points="135,40 145,40 145,100 135,100" fill="#E6953D"/>
          <polygon points="145,40 150,40 150,100 145,100" fill="#C47124"/>
          
          <polygon points="75,50 135,50 135,65 75,65" fill="#F8B15F"/>
          <polygon points="75,65 135,65 135,70 75,70" fill="#C47124"/>
          <polygon points="75,80 135,80 135,95 75,95" fill="#F8B15F"/>
          <polygon points="75,95 135,95 135,100 75,100" fill="#C47124"/>

          <polygon points="45,115 155,115 155,125 45,125" fill="#B96720"/>
          <polygon points="65,90 145,90 160,115 40,115" fill="#F8B15F"/>
          <polygon points="40,115 160,115 160,120 40,120" fill="#E6953D"/>

          <polygon points="45,115 57,115 53,175 42,170" fill="#E6953D"/>
          <polygon points="42,115 45,115 45,170 42,170" fill="#F8B15F"/>
          <polygon points="143,115 155,115 155,170 147,175" fill="#E6953D"/>
          <polygon points="155,115 158,115 158,170 155,170" fill="#C47124"/>
        </svg>
      </div>
    </div>

    <div class="option-card-wrap" data-index="1">
      <div class="badge">B</div>
      <div class="option-card">
        <svg viewBox="0 0 200 200" class="illu-svg">
          <ellipse cx="100" cy="165" rx="55" ry="10" fill="rgba(0,0,0,0.06)" />
          
          <path d="M 120 45 C 160 40, 180 80, 160 140 C 150 160, 140 160, 140 150 C 155 100, 140 60, 110 50 Z" fill="#69933B"/>
          <path d="M 120 45 C 160 40, 180 80, 160 140" fill="none" stroke="#3A5C19" stroke-width="3" stroke-linecap="round"/>
          
          <path d="M 80 40 C 80 15, 120 15, 120 40" fill="none" stroke="#69933B" stroke-width="8" stroke-linecap="round"/>

          <rect x="50" y="40" width="90" height="120" rx="35" fill="#93C655"/>
          <rect x="50" y="40" width="80" height="120" rx="35" fill="#A5DB64"/>
          
          <path d="M 130 90 L 150 90 C 155 90, 155 140, 145 140 L 130 140 Z" fill="#7AB041"/>
          <rect x="135" y="105" width="15" height="30" rx="4" fill="#69933B"/>

          <path d="M 50 85 C 50 30, 130 30, 140 85 C 145 100, 45 100, 50 85 Z" fill="#93C655"/>
          <path d="M 50 85 C 50 30, 130 30, 140 85" fill="none" stroke="#B4E576" stroke-width="3"/>
          <path d="M 55 90 C 100 100, 140 85, 140 85" fill="none" stroke="#7AB041" stroke-width="4"/>

          <rect x="60" y="100" width="70" height="50" rx="15" fill="#7AB041"/>
          <rect x="65" y="105" width="60" height="40" rx="10" fill="#69933B"/>
          
          <rect x="75" y="60" width="10" height="60" fill="#333"/>
          <rect x="105" y="60" width="10" height="60" fill="#333"/>
          <rect x="72" y="100" width="16" height="8" rx="2" fill="#EAEAEA"/>
          <rect x="102" y="100" width="16" height="8" rx="2" fill="#EAEAEA"/>
        </svg>
      </div>
    </div>

    <div class="option-card-wrap" data-index="2">
      <div class="badge">C</div>
      <div class="option-card">
        <svg viewBox="0 0 200 200" class="illu-svg">
          <ellipse cx="100" cy="155" rx="65" ry="12" fill="rgba(0,0,0,0.06)" />
          
          <g transform="translate(10, 30) scale(0.9)">
            <rect x="25" y="45" width="12" height="75" fill="#B3651F"/>
            <rect x="25" y="45" width="5" height="75" fill="#984A12"/>
            <rect x="163" y="45" width="12" height="75" fill="#B3651F"/>
            <rect x="163" y="45" width="5" height="75" fill="#984A12"/>
            
            <polygon points="15,45 185,45 180,55 20,55" fill="#B3651F"/>
            <polygon points="10,30 190,30 185,45 15,45" fill="#ECA248"/>
            <polygon points="15,15 185,15 190,30 10,30" fill="#F8BC64"/>
            <polygon points="15,15 185,15 180,20 20,20" fill="#FFE299" opacity="0.5"/>
            
            <polygon points="25,45 165,45 160,75 30,75" fill="#ECA248"/>
            <polygon points="30,72 160,72 160,75 30,75" fill="#CC7D2C"/>
            <rect x="80" y="55" width="30" height="6" rx="3" fill="#B3651F"/>
            
            <rect x="25" y="55" width="14" height="75" fill="#ECA248"/>
            <rect x="25" y="55" width="5" height="75" fill="#F8BC64"/>
            <rect x="151" y="55" width="14" height="75" fill="#ECA248"/>
            <rect x="151" y="55" width="5" height="75" fill="#F8BC64"/>
          </g>
        </svg>
      </div>
    </div>

  </div>

  <div class="bottom-right-controls">
    <button class="next-btn is-disabled" id="btn-next">
      <span>下一题</span>
      <svg viewBox="0 0 24 24"><path d="M9.29 15.88L13.17 12 9.29 8.12c-.39-.39-.39-1.02 0-1.41.39-.39 1.02-.39 1.41 0l4.59 4.59c.39.39.39 1.02 0 1.41l-4.59 4.59c-.39.39-1.02.39-1.41 0-.38-.39-.38-1.03 0-1.42z"/></svg>
    </button>
    <div class="skip-text">我不会 ></div>
  </div>

</div>

<script>
  const appContainer = document.getElementById('app');
  const btnAudio = document.getElementById('btn-audio');
  const cards = document.querySelectorAll('.option-card-wrap');
  const btnNext = document.getElementById('btn-next');

  // 音频播放波动特效
  btnAudio.addEventListener('click', () => {
    btnAudio.classList.remove('audio-pulse');
    void btnAudio.offsetWidth; // 触发重绘
    btnAudio.classList.add('audio-pulse');
    setTimeout(() => { btnAudio.classList.remove('audio-pulse'); }, 1000);
  });

  // 生成粒子碎星爆炸特效
  function createParticles(x, y) {
    const colors = ['#FFF', '#FFC458', '#78E949', '#FFAC32'];
    for (let i = 0; i < 12; i++) {
      const svgNS = "http://www.w3.org/2000/svg";
      const particle = document.createElementNS(svgNS, "svg");
      particle.setAttribute("viewBox", "0 0 100 100");
      particle.classList.add("click-particle");
      particle.style.fill = colors[Math.floor(Math.random() * colors.length)];
      
      const useElement = document.createElementNS(svgNS, "use");
      useElement.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#star-path");
      particle.appendChild(useElement);

      const size = (Math.random() * 1.5 + 1.0).toFixed(2);
      particle.style.width = `${size}vw`; particle.style.height = `${size}vw`;
      particle.style.left = `${x}px`; particle.style.top = `${y}px`;

      const angle = (Math.random() * 360) * (Math.PI / 180);
      const distance = Math.random() * 10 + 5;
      particle.style.setProperty('--dx', `${(Math.cos(angle) * distance).toFixed(2)}vw`);
      particle.style.setProperty('--dy', `${(Math.sin(angle) * distance).toFixed(2)}vw`);

      appContainer.appendChild(particle);
      particle.addEventListener('animationend', () => particle.remove());
    }
  }

  // 选项卡片点击交互逻辑
  cards.forEach((card, index) => {
    card.addEventListener('click', (e) => {
      // 检查是否已经处于选中状态
      if (card.classList.contains('is-selected')) return;

      // 清除所有卡片的状态，重新分配
      cards.forEach(c => {
        c.classList.remove('is-selected');
        c.classList.add('is-dimmed');
      });

      // 激活当前卡片
      card.classList.remove('is-dimmed');
      card.classList.add('is-selected');

      // 触发爆炸特效
      const rect = card.getBoundingClientRect();
      const containerRect = appContainer.getBoundingClientRect();
      createParticles(
        rect.left + rect.width / 2 - containerRect.left, 
        rect.top + rect.height / 2 - containerRect.top
      );

      // 解锁“下一题”
      btnNext.classList.remove('is-disabled');
    });
  });

  // 点击下一题重置整个状态
  btnNext.addEventListener('click', () => {
    if(!btnNext.classList.contains('is-disabled')){
      cards.forEach(c => {
        c.classList.remove('is-selected', 'is-dimmed');
      });
      btnNext.classList.add('is-disabled');
    }
  });

</script>

</body>
</html>