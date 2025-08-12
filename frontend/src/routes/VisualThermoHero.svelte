<script lang="ts">
  // --- Config ---
  let processType: 'isothermal' | 'adiabatic' | 'isobaric' | 'isochoric' = 'isothermal';
  let playing = true;

  // Diagram bounds (in "physical" units, arbitrary but consistent)
  const Vmin = 0.2, Vmax = 2.0;      // m^3/kg
  const Pmin = 0.0, Pmax = 1.2;      // MPa

  // SVG size (responsive: scales with container)
  export let width = 1000;
  export let height = 420;
  const margin = { top: 24, right: 28, bottom: 48, left: 64 };

  // Simple linear scales
  const sx = (v: number) =>
    margin.left + ( (v - Vmin) / (Vmax - Vmin) ) * (width - margin.left - margin.right);
  const sy = (p: number) =>
    margin.top + (1 - (p - Pmin) / (Pmax - Pmin)) * (height - margin.top - margin.bottom);

  // Curves (all return P for a given V)
  const Tref = 500;      // "temperature" knob for isothermal look
  const R = 0.287;       // kJ/kg·K (air-ish, just for a nice shape)
  const k = 1.4;         // gamma for adiabatic curve

  function P_isothermal(V: number) {
    const C = (R * Tref);           // not physically exact units—visual only
    return Math.min(Pmax, C / V / 4); // scaled for chart framing
  }
  function P_adiabatic(V: number) {
    const C = 0.3 * Math.pow(1.0, k); // scale so it fits nicely
    return Math.min(Pmax, C / Math.pow(V, k));
  }
  const P_isobaric = (V: number) => 0.5; // horizontal line
  const V_isochoric = 0.7;               // vertical line’s V

  // Build polyline points for each curve
  function curvePoints(which: string, samples = 220) {
    const pts: {x:number,y:number}[] = [];
    for (let i = 0; i < samples; i++) {
      const t = i / (samples - 1);
      const V = Vmin + t * (Vmax - Vmin);
      let P =
        which === 'isothermal' ? P_isothermal(V) :
        which === 'adiabatic'  ? P_adiabatic(V)  :
        which === 'isobaric'   ? P_isobaric(V)   :
        // isochoric: we’ll draw as a nearly-vertical polyline
        (Pmin + t * (Pmax - Pmin));

      let VX = which === 'isochoric' ? V_isochoric : V;
      pts.push({ x: sx(VX), y: sy(P) });
    }
    return pts;
  }

  // Animation state
  let t = 0;             // 0..1 position along the curve
  let lastTime = 0;

  function animateFrame(ts: number) {
    if (playing) {
      const dt = lastTime ? (ts - lastTime) : 16;
      t += dt / 4000; // ~4s per loop
      if (t > 1) t = 0;
    }
    lastTime = ts;
    requestAnimationFrame(animateFrame);
  }
  requestAnimationFrame(animateFrame);

  // Map t -> V,P for each process
  function stateAt(which: typeof processType, tau: number) {
    // ease-in-out for nicer motion
    const u = 0.5 - 0.5 * Math.cos(Math.PI * tau);

    if (which === 'isochoric') {
      const V = V_isochoric;
      const P = Pmin + u * (Pmax - Pmin);
      return { V, P };
    }
    if (which === 'isobaric') {
      const V = Vmin + u * (Vmax - Vmin);
      const P = P_isobaric(V);
      return { V, P };
    }
    if (which === 'adiabatic') {
      const V = Vmin + u * (Vmax - Vmin);
      const P = P_adiabatic(V);
      return { V, P };
    }
    // isothermal
    const V = Vmin + u * (Vmax - Vmin);
    const P = P_isothermal(V);
    return { V, P };
  }

  // Tooltip / hover
  let hover = { show: false, x: 0, y: 0, text: '' };
  function fmt(n: number, d = 3) { return Number.isFinite(n) ? n.toFixed(d) : '—'; }

  $: state = stateAt(processType, t);
  $: dot = { x: sx(state.V), y: sy(state.P) };

  // Grid / ticks
  const vticks = [0.4, 0.8, 1.2, 1.6, 2.0];
  const pticks = [0.2, 0.4, 0.6, 0.8, 1.0];
</script>

<style>
  .hero {
    display: grid;
    grid-template-columns: 1fr;
    gap: 18px;
    padding: 12px 20px 32px;
  }
  .toolbar {
    display: flex;
    gap: 10px;
    align-items: center;
    flex-wrap: wrap;
  }
  .btn {
    border: 1px solid #ccc;
    padding: 8px 12px;
    border-radius: 10px;
    cursor: pointer;
    background: #fff;
  }
  .btn.active { border-color: #f97316; box-shadow: 0 0 0 2px rgba(249,115,22,.15); }
  .legend {
    display: flex; gap: 16px; font-size: 0.9rem; color: #555; align-items: center;
  }
  .swatch { width: 14px; height: 3px; background: currentColor; display: inline-block; }
  .panel {
    display: flex; gap: 18px; align-items: center; justify-content: space-between;
  }
  .cta { display: flex; gap: 10px; }
  .cta .btn { background: #f97316; color: #fff; border-color: #f97316; }
  .tooltip {
    position: absolute; pointer-events: none;
    background: rgba(0,0,0,.8); color: #fff; padding: 6px 8px;
    border-radius: 8px; font-size: 12px; transform: translate(-50%, -120%);
    white-space: nowrap;
  }
  .wrap {
    position: relative; /* for tooltip */
    background: linear-gradient(180deg, #ffffff, #fbfbfb);
    border-radius: 14px; border: 1px solid #eee;
    padding: 6px;
  }
</style>

<div class="hero">
  <div class="panel">
    <div class="legend">
      <span style="color:#111;">
        <span class="swatch" style="color:#111"></span> Isothermal
      </span>
      <span style="color:#1f6feb;">
        <span class="swatch" style="color:#1f6feb"></span> Adiabatic (k≈1.4)
      </span>
      <span style="color:#16a34a;">
        <span class="swatch" style="color:#16a34a"></span> Isobaric
      </span>
      <span style="color:#a21caf;">
        <span class="swatch" style="color:#a21caf"></span> Isochoric
      </span>
    </div>

    <div class="cta">
      <button class="btn" on:click={() => playing = !playing}>
        {playing ? 'Pause' : 'Play'}
      </button>
      <button class="btn" on:click={() => t = 0}>Restart</button>
      <a class="btn" href="/practice" >Try a Sample Problem</a>
    </div>
  </div>

  <div class="toolbar">
    <button class="btn {processType==='isothermal' ? 'active' : ''}" on:click={() => processType='isothermal'}>Isothermal</button>
    <button class="btn {processType==='adiabatic' ? 'active' : ''}"  on:click={() => processType='adiabatic'}>Adiabatic</button>
    <button class="btn {processType==='isobaric' ? 'active' : ''}"   on:click={() => processType='isobaric'}>Isobaric</button>
    <button class="btn {processType==='isochoric' ? 'active' : ''}"  on:click={() => processType='isochoric'}>Isochoric</button>
  </div>

  <div class="wrap" style="width:100%; overflow:hidden;">
    <svg {width} {height} viewBox={`0 0 ${width} ${height}`} role="img" aria-label="PV diagram">
      <!-- Grid -->
      <g stroke="#eaeaea">
        {#each vticks as v}
          <line x1={sx(v)} y1={sy(Pmin)} x2={sx(v)} y2={sy(Pmax)} />
        {/each}
        {#each pticks as p}
          <line x1={sx(Vmin)} y1={sy(p)} x2={sx(Vmax)} y2={sy(p)} />
        {/each}
      </g>

      <!-- Axes -->
      <g stroke="#333" stroke-width="1.2">
        <line x1={sx(Vmin)} y1={sy(Pmin)} x2={sx(Vmax)} y2={sy(Pmin)} />
        <line x1={sx(Vmin)} y1={sy(Pmin)} x2={sx(Vmin)} y2={sy(Pmax)} />
      </g>

      <!-- Tick labels -->
      <g font-size="12" fill="#333">
        {#each vticks as v}
          <text x={sx(v)} y={sy(Pmin)+20} text-anchor="middle">{v.toFixed(1)}</text>
        {/each}
        {#each pticks as p}
          <text x={sx(Vmin)-10} y={sy(p)+4} text-anchor="end">{p.toFixed(1)}</text>
        {/each}
        <text x={sx(Vmax)} y={sy(Pmin)+36} text-anchor="end">V (m³/kg)</text>
        <text x={sx(Vmin)-44} y={sy(Pmax)-8} text-anchor="start" transform={`rotate(-90 ${sx(Vmin)-44},${sy(Pmax)-8})`}>P (MPa)</text>
      </g>

      <!-- Curves -->
      <polyline fill="none" stroke="#111"     stroke-width="2" points={curvePoints('isothermal').map(p=>`${p.x},${p.y}`).join(' ')} />
      <polyline fill="none" stroke="#1f6feb"  stroke-width="2" points={curvePoints('adiabatic').map(p=>`${p.x},${p.y}`).join(' ')} />
      <polyline fill="none" stroke="#16a34a"  stroke-width="2" points={curvePoints('isobaric').map(p=>`${p.x},${p.y}`).join(' ')} />
      <polyline fill="none" stroke="#a21caf"  stroke-width="2" points={curvePoints('isochoric').map(p=>`${p.x},${p.y}`).join(' ')} />

      <!-- Animated dot -->
      <g>
        <circle cx={dot.x} cy={dot.y} r="5.5" fill="#f97316" />
        <circle cx={dot.x} cy={dot.y} r="12" fill="none" stroke="#f97316" stroke-opacity="0.35" />
      </g>

      <!-- Hover capture -->
      <rect
  role="presentation"
  x="0" y="0" width="100%" height="100%" fill="transparent"
  on:mousemove={(e) => {
    const bb = (e.currentTarget as SVGRectElement).getBoundingClientRect();
    hover.x = e.clientX - bb.left;
    hover.y = e.clientY - bb.top;
    hover.text = `V=${fmt(state.V,3)} m³/kg • P=${fmt(state.P,3)} MPa`;
    hover.show = true;
  }}
  on:mouseleave={() => hover.show = false}
/>

    </svg>

    {#if hover.show}
      <div class="tooltip" style={`left:${hover.x}px; top:${hover.y}px;`}>
        {hover.text}
      </div>
    {/if}
  </div>
</div>
