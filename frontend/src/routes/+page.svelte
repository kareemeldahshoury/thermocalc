<script lang="ts">
  import TableCalculation from './tableCalculation.svelte';
  let selectedCalculator = '';
  let query = '';
</script>

<nav class="topbar">
  <div class="nav-buttons">
    <button class="mode-btn">Login</button>
    <button class="mode-btn secondary">About Us</button>
  </div>
</nav>


<div class="logo-bar">
  <img src="/images/Logo.png" alt="Thermo Solver" class="center-logo" />
</div>



<div class="layout">
  <nav class="sidebar">
    <div class="button-group">
      <button
        class:selected={selectedCalculator === 'calc1'}
        on:click={() => selectedCalculator = 'calc1'}>
        Table Search
      </button>

      <button
        class:selected={selectedCalculator === 'calc2'}
        on:click={() => selectedCalculator = 'calc2'}>
        Calculator 2
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
      <TableCalculation />
    {:else if selectedCalculator === 'calc2'}
      <p>Calculator 2 coming soon...</p>
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

<style>

.layout {
  display: flex;
}

.sidebar {
  width: 200px;
  padding: 40px 20px;
  box-shadow: 1px 0 3px rgba(0,0,0,0.05);
}

.button-group {
  display: flex;
  flex-direction: column;
  background-color: #FFCC33;
  gap: 15px;
  margin-top: 120px; /* lowered spacing */
}

.sidebar button {
  background-color: transparent;
  border: none;
  border-left: 5px solid transparent;
  padding: 12px 10px;
  text-align: left;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  color: #333;
}

.sidebar button:hover {
  background-color: #e0e0e0;
}

.sidebar button.selected {
  border-left: 5px solid #FF3366;
  font-weight: bold;
  background-color: #ffffff;
}

.main-content {
  flex-grow: 1;
  padding: 40px;
  background-color: #7A0019;
  color: white;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px; /* fixed height for top bar */
  padding: 0 24px;
  background: #7A0019;
  position: sticky;
  top: 0;
  z-index: 100;
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

.logo-bar {
  background-color: #7A0019;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px 0;
}


.center-logo {
  height: 80px;           /* Sets a fixed height to control topbar size */
  width: auto;            /* Maintains aspect ratio */
  max-width: 100%;        /* Prevents overflow on small screens */
  object-fit: contain;
  display: block;
}



</style>
