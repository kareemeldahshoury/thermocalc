<script lang="ts">
  import { onMount, onDestroy } from 'svelte';


  const maxDots = 3; 
  const intervalMs = 1000;

  let dotCount = 0;
  let timer: ReturnType<typeof setInterval> | null = null;

  onMount(() => {
    timer = setInterval(() => {
      dotCount = (dotCount + 1) % (maxDots + 1);
    }, intervalMs);
  });

  onDestroy(() => {
    if (timer) clearInterval(timer);
  });
</script>

<style>
  :root {
    --fg: #7A0019;
    --accent: #7aa2ff;
  }


.title {
  font-size: clamp(1.75rem, 4vw, 2.75rem);
  font-weight: 700;
  white-space: nowrap;

  background: linear-gradient(90deg, #7A0019, #f78b00);
  background-size: 200% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;

  animation: gradientShift 6s ease-in-out infinite alternate;
}

@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}





  .dots {
    display: inline-flex;
    gap: 0.05em;
    width: 2ch;        
  }

  .dot {
    opacity: 0;
    transition: opacity 180ms ease;
  }

  .dot.visible {
    opacity: 1;
  }


  @media (prefers-reduced-motion: reduce) {
    .dot { transition: none; }
  }
</style>

<div class="page">
  <div class="card" aria-live="polite">
    <h1 class="title">
      Coming Soon
      <span class="dots" aria-hidden="true">
        <span class="dot {dotCount >= 1 ? 'visible' : ''}">.</span>
        <span class="dot {dotCount >= 2 ? 'visible' : ''}">.</span>
        <span class="dot {dotCount >= 3 ? 'visible' : ''}">.</span>
      </span>
    </h1>
  </div>
</div>
