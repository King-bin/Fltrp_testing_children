<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>音频判断 UI 高保真互动版</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

  :root {
    --bg-color: #6EB63C;
    --card-outer: #FAF0CA;
    --card-inner: #FFFFFF;
    --card-dash: #F2D588;
    --audio-green: #46BA4C;
    --btn-green-wrap: #E4F2D8;
    --btn-green: #3FC755;
    --btn-green-shadow: #28A23C;
    --btn-blue-wrap: #DCE9FB;
    --btn-blue: #2A88FE;
    --btn-blue-shadow: #146AE0;
    --btn-orange: #FFB031;
    --btn-orange-shadow: #E28810;
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

  /* ================= 核心容器 (保持 16:9 比例) ================= */
  .app-container {
    position: relative;
    width: 100vw;
    height: 56.25vw; /* 16:9 */
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
    width: 6%;
    aspect-ratio: 1/1;
    background: var(--bg-color);
    border-radius: 1.5vw;
    border: 0.3vw solid #FFF;
    box-shadow: 0 0.4vw 0 rgba(0,0,0,0.1), inset 0 0.5vw 0.5vw rgba(255,255,255,0.3);
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    transition: transform 0.1s ease;
  }
  .back-btn:active {
    transform: scale(0.9) translateY(0.2vw);
    box-shadow: 0 0.1vw 0 rgba(0,0,0,0.1), inset 0 0.5vw 0.5vw rgba(255,255,255,0.3);
  }
  .back-btn svg { width: 60%; fill: #FFF; }

  /* ================= 中间主卡片 ================= */
  .main-card-wrap {
    position: absolute;
    top: 10%;
    width: 40%;
    height: 65%;
    background: var(--card-outer);
    border-radius: 2.5vw;
    padding: 0.6vw;
    box-shadow: 0 0.8vw 0px rgba(0,0,0,0.08);
  }

  /* 音频播放按钮 (左上角悬浮) */
  .audio-wrap {
    position: absolute;
    top: -2.5vw;
    left: -2.5vw;
    width: 7vw;
    aspect-ratio: 1;
    border-radius: 50%;
    border: 0.2vw solid #FFF;
    background: rgba(255, 255, 255, 0.2);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    box-shadow: 0 0.5vw 1vw rgba(0,0,0,0.05);
  }
  .audio-btn {
    width: 75%;
    height: 75%;
    border-radius: 50%;
    background: var(--audio-green);
    border: 0.3vw solid #FFF;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0.4vw 0px rgba(0,0,0,0.15), inset 0 0.5vw 0.5vw rgba(255,255,255,0.3);
    cursor: pointer;
    transition: transform 0.1s, box-shadow 0.1s;
  }
  .audio-btn:active {
    transform: scale(0.92) translateY(0.2vw);
    box-shadow: 0 0.1vw 0px rgba(0,0,0,0.15), inset 0 0.5vw 0.5vw rgba(255,255,255,0.3);
  }
  .audio-btn svg {
    width: 55%;
    fill: #FFF;
    margin-right: -0.2vw; /* 微调视觉中心 */
  }

  /* 音频波纹动画 */
  @keyframes pulse-ring {
    0% { transform: scale(0.8); opacity: 0.8; }
    100% { transform: scale(1.4); opacity: 0; }
  }
  .audio-wrap.is-playing::after {
    content: '';
    position: absolute;
    width: 100%; height: 100%;
    border-radius: 50%;
    border: 0.3vw solid #FFF;
    animation: pulse-ring 1s ease-out infinite;
  }

  .main-card {
    width: 100%;
    height: 100%;
    background: var(--card-inner);
    border-radius: 2vw;
    border: 0.2vw dashed var(--card-dash);
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
  }

  /* 装饰点缀 */
  .card-deco {
    position: absolute;
    z-index: 1;
  }
  .deco-star-1 { fill: #FFC635; width: 2vw; top: 15%; left: 15%; animation: twinkle 2s infinite alternate;}
  .deco-star-2 { fill: #4DA2FF; width: 1.5vw; top: 28%; left: 10%; animation: twinkle 1.5s infinite alternate-reverse;}
  .deco-swirl { stroke: #F4B04F; stroke-width: 0.3vw; stroke-linecap: round; fill: none; width: 1.5vw; top: 15%; right: 15%; }

  @keyframes twinkle {
    0% { opacity: 0.4; transform: scale(0.8); }
    100% { opacity: 1; transform: scale(1.1); }
  }

  /* 书桌插画区 */
  .illustration-area {
    width: 70%;
    height: 70%;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
  }
  .desk-shadow {
    position: absolute;
    bottom: 0%;
    width: 80%;
    height: 12%;
    background: rgba(0,0,0,0.05);
    border-radius: 50%;
  }
  .desk-svg { width: 90%; height: 90%; z-index: 2; }

  /* ================= 底部判断按钮 ================= */
  .actions-area {
    position: absolute;
    bottom: 5%;
    width: 42%;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .action-btn-wrapper {
    width: 46%;
    aspect-ratio: 2.3/1;
    border-radius: 5vw;
    padding: 0.5vw;
    box-shadow: 0 0.6vw 0px rgba(0,0,0,0.1);
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.3s, box-shadow 0.3s;
    cursor: pointer;
  }
  .action-btn-wrapper.green-wrap { background: var(--btn-green-wrap); }
  .action-btn-wrapper.blue-wrap { background: var(--btn-blue-wrap); }

  .action-btn {
    width: 100%;
    height: 100%;
    border-radius: 4vw;
    border: none;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    pointer-events: none;
  }

  .btn-green-inner {
    background: var(--btn-green);
    box-shadow: 0 0.5vw 0 var(--btn-green-shadow), inset 0 0.8vw 0.5vw rgba(255,255,255,0.4);
  }
  .btn-blue-inner {
    background: var(--btn-blue);
    box-shadow: 0 0.5vw 0 var(--btn-blue-shadow), inset 0 0.8vw 0.5vw rgba(255,255,255,0.4);
  }

  /* 按钮高光 */
  .action-btn::before {
    content: '';
    position: absolute;
    top: 5%;
    left: 5%;
    right: 5%;
    height: 40%;
    background: linear-gradient(to bottom, rgba(255,255,255,0.6), transparent);
    border-radius: 3vw;
    pointer-events: none;
  }

  /* 表情图标 SVG */
  .icon-face {
    height: 55%;
    position: relative;
    z-index: 2;
    margin-bottom: 0.4vw;
  }

  /* 按钮四周的星光 */
  .btn-sp { position: absolute; fill: #FFF; opacity: 0.8; }
  .btn-sp-1 { width: 0.8vw; top: 15%; left: 10%; }
  .btn-sp-2 { width: 0.6vw; bottom: 20%; right: 10%; }

  /* ================= 右下角区域 ================= */
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
    background: linear-gradient(to bottom, #FFC548, var(--btn-orange));
    border: 0.2vw solid #FFF;
    border-radius: 3vw;
    padding: 0.8vw 1.5vw;
    color: #FFF;
    font-size: 1.4vw;
    font-weight: 800;
    font-family: 'Nunito', sans-serif;
    display: flex;
    align-items: center;
    gap: 0.5vw;
    cursor: pointer;
    box-shadow: 0 0.4vw 0 var(--btn-orange-shadow), 0 0.5vw 1vw rgba(0,0,0,0.15);
    transition: transform 0.1s ease, opacity 0.3s ease, filter 0.3s ease;
  }
  .next-btn:active {
    transform: scale(0.95) translateY(0.2vw);
    box-shadow: 0 0.1vw 0 var(--btn-orange-shadow);
  }
  .next-btn.is-disabled { opacity: 0.5; filter: grayscale(0.5); pointer-events: none; }
  .next-btn svg { width: 1vw; fill: #FFF; }
  
  .skip-text {
    color: #FFF;
    font-size: 1.2vw;
    font-weight: 700;
    opacity: 0.8;
    cursor: pointer;
    transition: opacity 0.2s;
  }
  .skip-text:active { opacity: 0.5; }

  /* ================= 炫酷交互动效状态 ================= */
  /* 1. 按压反馈 */
  .action-btn-wrapper:active { transform: scale(0.94); }
  .action-btn-wrapper:active .btn-green-inner { box-shadow: 0 0.1vw 0 var(--btn-green-shadow), inset 0 0.2vw 0.5vw rgba(0,0,0,0.2); }
  .action-btn-wrapper:active .btn-blue-inner { box-shadow: 0 0.1vw 0 var(--btn-blue-shadow), inset 0 0.2vw 0.5vw rgba(0,0,0,0.2); }

  /* 2. 选中 Q 弹与呼吸发光 */
  .action-btn-wrapper.is-selected { transform: scale(1.1); z-index: 5; }
  .action-btn-wrapper.is-selected.green-wrap {
    box-shadow: 0 0 2vw rgba(63, 199, 85, 0.7), 0 0.6vw 0px rgba(0,0,0,0.1);
    animation: wrapper-bounce 0.4s ease-out;
  }
  .action-btn-wrapper.is-selected.blue-wrap {
    box-shadow: 0 0 2vw rgba(42, 136, 254, 0.7), 0 0.6vw 0px rgba(0,0,0,0.1);
    animation: wrapper-shake 0.4s ease-in-out;
  }

  /* 3. 未选中变暗缩小 */
  .action-btn-wrapper.is-dimmed { opacity: 0.4; transform: scale(0.9); }

  /* 4. 内部表情特效 */
  .action-btn-wrapper.is-selected .green-wrap .icon-face { animation: icon-celebrate 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.5) forwards; }
  .action-btn-wrapper.is-selected .blue-wrap .icon-face { animation: icon-cross-spin 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.2) forwards; }

  /* 5. 爆炸粒子系统 */
  .click-particle {
    position: absolute; pointer-events: none; fill: #FFF; z-index: 100;
    animation: particle-fly 0.6s cubic-bezier(0.1, 0.8, 0.25, 1) forwards;
  }
  .particle-star-gold { fill: #FFD238; }
  .particle-star-cyan { fill: #26FFF6; }

  /* 动画关键帧 */
  @keyframes wrapper-bounce { 0% { transform: scale(1); } 40% { transform: scale(1.15); } 70% { transform: scale(1.05); } 100% { transform: scale(1.1); } }
  @keyframes wrapper-shake { 0%, 100% { transform: scale(1.1) translateX(0); } 20%, 60% { transform: scale(1.1) translateX(-0.5vw); } 40%, 80% { transform: scale(1.1) translateX(0.5vw); } }
  @keyframes icon-celebrate { 0% { transform: scale(1) translateY(0); } 30% { transform: scale(1.3) translateY(-1vw) rotate(-10deg); } 50% { transform: scale(1.3) translateY(-1vw) rotate(10deg); } 70% { transform: scale(1.1) translateY(0) rotate(0); } 100% { transform: scale(1.1) translateY(0); } }
  @keyframes icon-cross-spin { 0% { transform: scale(1) rotate(0); } 50% { transform: scale(1.2) rotate(180deg); } 100% { transform: scale(1.1) rotate(180deg); } }
  @keyframes particle-fly { 0% { transform: translate(-50%, -50%) translate(0, 0) scale(1); opacity: 1; } 100% { transform: translate(-50%, -50%) translate(var(--dx), var(--dy)) scale(0); opacity: 0; } }

  /* SVG 符号隐藏 */
  .star-symbol { display: none; }
</style>
</head>
<body>

<svg class="star-symbol">
  <defs>
    <path id="star-path" d="M50 0 C50 30 70 50 100 50 C70 50 50 70 50 100 C50 70 30 50 0 50 C30 50 50 30 50 0 Z" />
  </defs>
</svg>

<div class="app-container" id="app">
  
  <button class="back-btn">
    <svg viewBox="0 0 24 24">
      <path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z" stroke="#FFF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </button>

  <div class="main-card-wrap">
    
    <div class="audio-wrap" id="audio-player">
      <div class="audio-btn">
        <svg viewBox="0 0 24 24">
          <path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/>
        </svg>
      </div>
    </div>

    <div class="main-card">
      <svg viewBox="0 0 100 100" class="card-deco deco-star-1"><use href="#star-path"/></svg>
      <svg viewBox="0 0 100 100" class="card-deco deco-star-2"><use href="#star-path"/></svg>
      <svg viewBox="0 0 100 100" class="card-deco deco-swirl">
        <path d="M 50 10 Q 70 10, 80 30 T 50 60 T 30 80" />
      </svg>

      <div class="illustration-area">
        <div class="desk-shadow"></div>
        <svg viewBox="0 0 200 150" class="desk-svg">
          <polygon points="15,45 185,45 180,55 20,55" fill="#B3651F"/>
          <polygon points="10,35 190,35 185,45 15,45" fill="#ECA248"/>
          <polygon points="15,25 185,25 190,35 10,35" fill="#F8BC64"/>
          <rect x="25" y="45" width="10" height="70" fill="#B3651F"/>
          <rect x="25" y="45" width="4" height="70" fill="#984A12"/>
          <rect x="160" y="45" width="10" height="70" fill="#B3651F"/>
          <rect x="160" y="45" width="4" height="70" fill="#984A12"/>
          <polygon points="25,45 165,45 160,75 30,75" fill="#ECA248"/>
          <polygon points="30,72 160,72 160,75 30,75" fill="#CC7D2C"/>
          <rect x="80" y="55" width="30" height="5" rx="2" fill="#B3651F"/>
          <rect x="25" y="55" width="12" height="65" fill="#ECA248"/>
          <rect x="25" y="55" width="4" height="65" fill="#F8BC64"/>
          <rect x="153" y="55" width="12" height="65" fill="#ECA248"/>
          <rect x="153" y="55" width="4" height="65" fill="#F8BC64"/>
        </svg>
      </div>

    </div>
  </div>

  <div class="actions-area">
    
    <div class="action-btn-wrapper green-wrap" id="wrap-correct">
      <div class="action-btn btn-green-inner">
        <svg viewBox="0 0 100 100" class="btn-sp btn-sp-1"><use href="#star-path"/></svg>
        <svg viewBox="0 0 100 100" class="btn-sp btn-sp-2"><use href="#star-path"/></svg>
        
        <svg viewBox="0 0 100 60" class="icon-face">
          <path d="M20,30 L40,50 L80,10 L70,5 L40,35 L30,25 Z" fill="#FFF" stroke="#FFF" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>
          <circle cx="43" cy="35" r="2.5" fill="#222"/>
          <circle cx="55" cy="31" r="2.5" fill="#222"/>
          <ellipse cx="38" cy="37" rx="3" ry="1.5" fill="#FF8BA7" opacity="0.8"/>
          <ellipse cx="60" cy="33" rx="3" ry="1.5" fill="#FF8BA7" opacity="0.8"/>
          <path d="M47,36 Q49,39 51,35" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </div>
    </div>

    <div class="action-btn-wrapper blue-wrap" id="wrap-wrong">
      <div class="action-btn btn-blue-inner">
        <svg viewBox="0 0 100 100" class="btn-sp btn-sp-1"><use href="#star-path"/></svg>
        <svg viewBox="0 0 100 100" class="btn-sp btn-sp-2"><use href="#star-path"/></svg>

        <svg viewBox="0 0 80 80" class="icon-face">
          <path d="M25,25 L55,55 M55,25 L25,55" fill="none" stroke="#FFF" stroke-width="16" stroke-linecap="round"/>
          <circle cx="34" cy="40" r="2.5" fill="#222"/>
          <circle cx="46" cy="40" r="2.5" fill="#222"/>
          <ellipse cx="28" cy="42" rx="3" ry="1.5" fill="#FF8BA7" opacity="0.8"/>
          <ellipse cx="52" cy="42" rx="3" ry="1.5" fill="#FF8BA7" opacity="0.8"/>
          <path d="M38,42 Q40,45 42,42" fill="none" stroke="#222" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </div>
    </div>

  </div>

  <div class="bottom-right-controls">
    <button class="next-btn is-disabled" id="btn-next">
      <span>下一题</span>
      <svg viewBox="0 0 24 24"><path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/></svg>
    </button>
    <div class="skip-text">我不会 &gt;</div>
  </div>

</div>

<script>
  const wrapCorrect = document.getElementById('wrap-correct');
  const wrapWrong = document.getElementById('wrap-wrong');
  const btnNext = document.getElementById('btn-next');
  const appContainer = document.getElementById('app');
  const audioPlayer = document.getElementById('audio-player');

  // 音频播放波动特效
  audioPlayer.addEventListener('click', () => {
    audioPlayer.classList.remove('is-playing');
    void audioPlayer.offsetWidth; // 触发重绘
    audioPlayer.classList.add('is-playing');
    setTimeout(() => { audioPlayer.classList.remove('is-playing'); }, 1000); // 1秒后停止波纹
  });

  // 物理级爆炸粒子系统
  function createBurst(e, isCorrect) {
    const rect = e.currentTarget.getBoundingClientRect();
    const containerRect = appContainer.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2 - containerRect.left;
    const centerY = rect.top + rect.height / 2 - containerRect.top;
    const particleCount = 15; // 增加粒子数量
    const colors = isCorrect ? ['#FFF', '#FFD238', '#6FFF6F'] : ['#FFF', '#26FFF6', '#FF5252'];

    for (let i = 0; i < particleCount; i++) {
      const svgNS = "http://www.w3.org/2000/svg";
      const particle = document.createElementNS(svgNS, "svg");
      particle.setAttribute("viewBox", "0 0 100 100");
      particle.classList.add("click-particle");
      
      if (i % 3 === 1) particle.classList.add("particle-star-gold");
      if (i % 3 === 2) particle.classList.add("particle-star-cyan");

      const useElement = document.createElementNS(svgNS, "use");
      useElement.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#star-path");
      particle.appendChild(useElement);

      const size = (Math.random() * 1.5 + 1.0).toFixed(2);
      particle.style.width = `${size}vw`; particle.style.height = `${size}vw`;
      particle.style.left = `${centerX}px`; particle.style.top = `${centerY}px`;

      const angle = (Math.random() * 360) * (Math.PI / 180);
      const distance = Math.random() * 10 + 6; // 爆炸范围更大
      particle.style.setProperty('--dx', `${(Math.cos(angle) * distance).toFixed(2)}vw`);
      particle.style.setProperty('--dy', `${(Math.sin(angle) * distance).toFixed(2)}vw`);
      particle.style.animationDelay = `${(Math.random() * 0.1).toFixed(2)}s`;

      appContainer.appendChild(particle);
      particle.addEventListener('animationend', () => particle.remove());
    }
  }

  // 核心交互逻辑
  function handleSelect(selectedWrap, dimmedWrap, isCorrect, e) {
    if (selectedWrap.classList.contains('is-selected')) return;

    selectedWrap.classList.remove('is-dimmed');
    selectedWrap.classList.add('is-selected');
    dimmedWrap.classList.remove('is-selected');
    dimmedWrap.classList.add('is-dimmed');

    createBurst(e, isCorrect);
    btnNext.classList.remove('is-disabled'); // 激活下一题
  }

  wrapCorrect.addEventListener('click', (e) => handleSelect(wrapCorrect, wrapWrong, true, e));
  wrapWrong.addEventListener('click', (e) => handleSelect(wrapWrong, wrapCorrect, false, e));

  // 流程重置
  btnNext.addEventListener('click', () => {
    if (!btnNext.classList.contains('is-disabled')) {
      wrapCorrect.classList.remove('is-selected', 'is-dimmed');
      wrapWrong.classList.remove('is-selected', 'is-dimmed');
      btnNext.classList.add('is-disabled');
    }
  });
</script>

</body>
</html>