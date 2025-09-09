<script lang="ts">
  import ConversionTable from "./conversionTable.svelte";
  import ProcessInfo from "./processInfo.svelte";

  let currentView: 'home' | 'conversion' | 'process' = 'home';

  function goToConversionTable() {
    currentView = 'conversion';
  }

  function goToProcessesInfo() {
    currentView = 'process';
  }

  function goHome() {
    currentView = 'home';
  }
</script>

{#if currentView === 'home'}
  <div class="container">
    <h2>Additional Tools</h2>
    <div class="button-group">
      <button class="pagesBtn" on:click={goToConversionTable}>Conversion Table</button>
      <button class="pagesBtn" on:click={goToProcessesInfo}>Processes Information</button>
    </div>
  </div>
{:else if currentView === 'conversion'}
  <ConversionTable />
  <button class="nav-btn" on:click={goHome}>Back</button>
{:else if currentView === 'process'}
  <ProcessInfo />
  <button class="nav-btn" on:click={goHome}>Back</button>
{/if}


<style>
.container {
  max-width: 800px;
  margin: -10px auto;
  padding: 5px 30px 30px 30px; 
  background: #fff;
  color: #000;
  border-radius: 12px;
  box-shadow: 0 0 15px rgba(0,0,0,0.2);
  font-family: system-ui, sans-serif;
}

h2 {
  font-size: 1.4rem;
  font-weight: 700;
  color: #7A0019;
  margin-top: 27px;
  margin-bottom: 20px;
  text-align: center
}

.button-group {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.pagesBtn {
  background-color: #7A0019;
  color: white;
  border: none;
  padding: 12px 20px;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.nav-btn {
  background-color: #7A0019;
  margin-left: 850px;
  color: white;
  border: none;
  padding: 12px 20px;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.nav-btn:hover {
  background-color: #9c0033;
}
</style>
