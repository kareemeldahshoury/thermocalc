<script lang="ts">
  import TableCalculation from './tableCalculation.svelte';
  import ConversionCalc from './conversionCalc.svelte';
  let selectedCalculator = '';
  let query = '';
</script>

<nav class="topbar">
  <div class="nav-buttons">
    <button class="mode-btn">Login</button>
    <button class="mode-btn secondary">Learning Center</button>
  </div>
</nav>

<div class="logo-bar">
  <img src="/images/Logo.png" alt="Thermo Solver" class="center-logo" />
</div>

<div class="page">
  <div class="layout">
    <nav class="sidebar">
      <div class="button-group">
        <button
          class:selected={selectedCalculator === 'calc1'}
          on:click={() => selectedCalculator = 'calc1'}>
          Conversion Calculator
        </button>

        <button
          class:selected={selectedCalculator === 'calc2'}
          on:click={() => selectedCalculator = 'calc2'}>
          Table Search
        </button>

        <button
          class:selected={selectedCalculator === 'calc3'}
          on:click={() => selectedCalculator = 'calc3'}>
          Calculator 3
        </button>

        <button
          class:selected={selectedCalculator === 'calc4'}
          on:click={() => selectedCalculator = 'calc4'}>
          Calculator 4
        </button>

        <button
          class:selected={selectedCalculator === 'calc5'}
          on:click={() => selectedCalculator = 'calc5'}>
          Learning Center
        </button>
      </div>
    </nav>

    <main class="main-content">
      {#if selectedCalculator === 'calc1'}
        <ConversionCalc />
      {:else if selectedCalculator === 'calc2'}
        <TableCalculation />
      {:else if selectedCalculator === 'calc3'}
        <p>Calculator 3 coming soon...</p>
      {:else if selectedCalculator === 'calc4'}
        <p>Calculator 4 coming soon...</p>
      {:else if selectedCalculator === 'calc5'}
        <p>Calculator 5 coming soon...</p>
      {:else}
        <p>Select a calculator from the left.</p>
      {/if}
    </main>
  </div>
</div>

<style>
:global(body, html) {
  margin: 0;
  padding: 0;
  background-color: #f2f2f2;
  font-family: system-ui, sans-serif;
  height: 100%;
}

.page {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
  padding: 0 24px;
  background: #7A0019;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo-bar {
  background-color: #7A0019;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 16px 0;
}

.center-logo {
  height: 80px;
  width: auto;
  max-width: 100%;
  object-fit: contain;
  display: block;
}

.nav-buttons {
  display: flex;
  gap: 8px;
}

.mode-btn {
  background: #ffeed6;
  border: 1px solid #f78b00;
  padding: 6px 12px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 600;
}

.mode-btn.secondary {
  border-color: #888;
  background: #f3f3f3;
}

.layout {
  display: flex;
  flex-grow: 1;
  background-color: #f2f2f2;
  margin-top: 24px;
}

.sidebar {
  width: 200px;
  height: 100%;
  padding: 0;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  margin-top: 16px;
}

.button-group {
  display: flex;
  flex-direction: column;
  width: 100%;           /* important to make buttons align fully */
  background-color: transparent;
  margin-top: 70px
}

.sidebar button {
  background-color: #e0e0e0;
  border: none;
  padding: 14px 10px;
  text-align: left;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #333;
  display: flex;
  align-items: center;
  gap: 8px;
}

.sidebar button.selected {
  background-color: #ffffff;
  font-weight: bold;
  border-left: 4px solid #7A0019;
  border-top: 1.5px solid #7A0019;
  border-bottom: 1.5px solid #7A0019;
}

.main-content {
  flex-grow: 1;
  padding: 40px;
  background-color: #ffffff;
  color: #333;
  overflow-y: auto;
  margin-top: 16px;
}
</style>
