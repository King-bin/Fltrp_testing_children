<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>图文判断 UI 高保真互动版</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@700;800;900&display=swap');

  :root {
    --bg-color: #76AE45;
    --card-outer: #F9EAB6;
    --card-inner: #FFFFFF;
    --card-dash: #F5D381;
    --text-blue: #234E84;
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
    border: 0.35vw solid #FFF;
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
  .back-btn svg {
    width: 60%;
    fill: #FFF;
  }

  /* ================= 中间主卡片 ================= */
  .main-card-wrap {
    position: absolute;
    top: 10%;
    width: 38%;
    height: 65%;
    background: var(--card-outer);
    border-radius: 2.5vw;
    padding: 0.6vw;
    box-shadow: 0 0.8vw 0px rgba(0,0,0,0.08);
  }

  .main-card {
    width: 100%;
    height: 100%;
    background: var(--card-inner);
    border-radius: 2vw;
    border: 0.2vw dashed var(--card-dash);
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
  }

  /* 单词区域 */
  .word-area {
    flex: 0.4;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 4.5vw;
    font-weight: 900;
    color: var(--text-blue);
    letter-spacing: 0.1vw;
    border-bottom: 0.2vw dashed var(--card-dash);
  }

  /* 图片区域 */
  .image-area {
    flex: 0.6;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  /* 鸭子插图 SVG */
  .duck-svg {
    width: 65%;
    height: 80%;
    filter: drop-shadow(0 0.5vw 0.5vw rgba(0,0,0,0.05));
    z-index: 2;
  }

  /* 卡片内部星星闪烁 */
  .card-sp {
    position: absolute;
    fill: #FFD238;
    width: 1.2vw;
    animation: twinkle 2s infinite ease-in-out alternate;
  }
  .card-sp-1 { left: 15%; top: 40%; }
  .card-sp-2 { right: 15%; bottom: 25%; width: 1.5vw; animation-delay: 1s;}

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
  .action-btn-wrapper.green-wrap {
    background: var(--btn-green-wrap);
  }
  .action-btn-wrapper.blue-wrap {
    background: var(--btn-blue-wrap);
  }

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
    pointer-events: none; /* 让外层 wrapper 处理点击 */
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
    transition: transform 0.3s;
  }

  /* 按钮四周的星光 */
  .btn-sp {
    position: absolute;
    fill: #FFF;
    opacity: 0.8;
  }
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

  /* 下一题按钮 */
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
    position: relative;
  }
  .next-btn:active {
    transform: scale(0.95) translateY(0.2vw);
    box-shadow: 0 0.1vw 0 var(--btn-orange-shadow);
  }
  .next-btn.is-disabled {
    opacity: 0.5;
    filter: grayscale(0.5);
    pointer-events: none;
  }
  .next-btn svg { width: 1vw; fill: #FFF; }
  
  /* 我不会 文本 */
  .skip-text {
    color: #FFF;
    font-size: 1.2vw;
    font-weight: 700;
    opacity: 0.8;
    cursor: pointer;
    transition: opacity 0.2s;
  }
  .skip-text:active {
    opacity: 0.5;
  }


  /* ================= 酷炫交互动效状态 ================= */
  
  /* 1. 点击按下瞬时下凹 */
  .action-btn-wrapper:active {
    transform: scale(0.94);
  }
  .action-btn-wrapper:active .btn-green-inner {
    box-shadow: 0 0.1vw 0 var(--btn-green-shadow), inset 0 0.2vw 0.5vw rgba(0,0,0,0.2);
  }
  .action-btn-wrapper:active .btn-blue-inner {
    box-shadow: 0 0.1vw 0 var(--btn-blue-shadow), inset 0 0.2vw 0.5vw rgba(0,0,0,0.2);
  }

  /* 2. 选中后的 Q 弹放大与发光 */
  .action-btn-wrapper.is-selected {
    transform: scale(1.1);
    z-index: 5;
  }
  .action-btn-wrapper.is-selected.green-wrap {
    box-shadow: 0 0 2vw rgba(63, 199, 85, 0.7), 0 0.6vw 0px rgba(0,0,0,0.1);
    animation: wrapper-bounce 0.4s ease-out;
  }
  .action-btn-wrapper.is-selected.blue-wrap {
    box-shadow: 0 0 2vw rgba(42, 136, 254, 0.7), 0 0.6vw 0px rgba(0,0,0,0.1);
    animation: wrapper-shake 0.4s ease-in-out;
  }

  /* 3. 未选中项变暗缩小 */
  .action-btn-wrapper.is-dimmed {
    opacity: 0.4;
    transform: scale(0.9);
  }

  /* 动画关键帧 */
  @keyframes wrapper-bounce {
    0% { transform: scale(1); }
    40% { transform: scale(1.15); }
    70% { transform: scale(1.05); }
    100% { transform: scale(1.1); }
  }

  @keyframes wrapper-shake {
    0%, 100% { transform: scale(1.1) translateX(0); }
    20%, 60% { transform: scale(1.1) translateX(-0.5vw); }
    40%, 80% { transform: scale(1.1) translateX(0.5vw); }
  }

  @keyframes twinkle {
    0% { opacity: 0.3; transform: scale(0.8); }
    100% { opacity: 1; transform: scale(1.2); }
  }

  /* SVG 共用小星星形状 */
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
    <div class="main-card">
      <div class="word-area">duck</div>
      <div class="image-area">
        <svg viewBox="0 0 100 100" class="card-sp card-sp-1"><use href="#star-path"/></svg>
        <svg viewBox="0 0 100 100" class="card-sp card-sp-2"><use href="#star-path"/></svg>
        
        <svg viewBox="0 0 200 200" class="duck-svg">
          <defs>
            <radialGradient id="duck-body" cx="40%" cy="30%" r="60%">
              <stop offset="0%" stop-color="#FFF250" />
              <stop offset="70%" stop-color="#FFD600" />
              <stop offset="100%" stop-color="#E8A900" />
            </radialGradient>
            <radialGradient id="duck-beak" cx="30%" cy="30%" r="50%">
              <stop offset="0%" stop-color="#FF9F30" />
              <stop offset="100%" stop-color="#ED6200" />
            </radialGradient>
          </defs>
          
          <ellipse cx="100" cy="165" rx="60" ry="12" fill="#D3E5F5" />
          
          <path d="M60 160 C 20 160, 20 100, 60 100 C 80 100, 90 80, 100 80 C 130 80, 160 100, 165 120 C 175 110, 185 105, 180 125 C 175 145, 140 160, 100 160 Z" fill="url(#duck-body)" />
          
          <path d="M50 115 C 35 125, 40 145, 60 150 C 65 150, 60 135, 50 115 Z" fill="#FFF" opacity="0.4" filter="blur(2px)"/>
          
          <circle cx="100" cy="70" r="40" fill="url(#duck-body)" />
          <circle cx="85" cy="55" r="10" fill="#FFF" opacity="0.6" filter="blur(1px)"/>
          
          <path d="M100 30 Q 105 20, 115 25 Q 108 32, 105 32 Z" fill="#FFD600" />
          
          <path d="M65 75 Q 40 70, 45 85 Q 60 90, 75 80 Z" fill="url(#duck-beak)" />
          <path d="M50 82 Q 60 85, 72 79" fill="none" stroke="#C44800" stroke-width="2" stroke-linecap="round"/>
          
          <circle cx="105" cy="65" r="7" fill="#1A1A1A" />
          <circle cx="103" cy="63" r="2.5" fill="#FFF" />
          <circle cx="107" cy="66" r="1" fill="#FFF" />
          
          <ellipse cx="122" cy="75" rx="6" ry="3" fill="#FF8BA7" opacity="0.6"/>

          <path d="M85 115 C 75 130, 95 150, 125 145 C 135 140, 140 125, 125 120 C 110 115, 95 105, 85 115 Z" fill="#FFC900" stroke="#E8A900" stroke-width="2" stroke-linejoin="round"/>
          <path d="M95 125 C 105 135, 120 135, 125 130" fill="none" stroke="#E8A900" stroke-width="2" stroke-linecap="round"/>
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
      <svg viewBox="0 0 24 24">
        <path d="M8.59 16.59L13.17 12 8.59 7.41 10 6l6 6-6 6-1.41-1.41z"/>
      </svg>
    </button>
    <div class="skip-text">我不会 &gt;</div>
  </div>

</div>

<script>
  const wrapCorrect = document.getElementById('wrap-correct');
  const wrapWrong = document.getElementById('wrap-wrong');
  const btnNext = document.getElementById('btn-next');

  // 处理选中逻辑
  function handleSelect(selectedWrap, dimmedWrap) {
    if (selectedWrap.classList.contains('is-selected')) return;

    // 切换状态类名 (Q弹发光 / 变暗缩小)
    selectedWrap.classList.remove('is-dimmed');
    selectedWrap.classList.add('is-selected');
    
    dimmedWrap.classList.remove('is-selected');
    dimmedWrap.classList.add('is-dimmed');

    // 激活下一题按钮
    btnNext.classList.remove('is-disabled');
  }

  // 绑定对错按钮点击事件
  wrapCorrect.addEventListener('click', () => handleSelect(wrapCorrect, wrapWrong));
  wrapWrong.addEventListener('click', () => handleSelect(wrapWrong, wrapCorrect));

  // 点击下一题重置整个状态流
  btnNext.addEventListener('click', () => {
    // 只有非禁用状态下才可点击重置
    if (!btnNext.classList.contains('is-disabled')) {
      wrapCorrect.classList.remove('is-selected', 'is-dimmed');
      wrapWrong.classList.remove('is-selected', 'is-dimmed');
      btnNext.classList.add('is-disabled');
    }
  });
</script>

</body>
</html>