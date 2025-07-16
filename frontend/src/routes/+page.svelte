<script lang="ts">
  import TableCalculation from './tableCalculation.svelte';
  import ConversionCalc from './conversionCalc.svelte';
  import PracticeProblems from './practiceProblems.svelte';




  let selectedCalculator = '';
  let query = '';
  let selectedSubject = '';
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

<div class="subject-bar">
  <button class="subject-tab">Thermodynamics</button>
  <button class="subject-tab">Fluids</button>
  <button class="subject-tab">Heat Transfer</button>
  <button class="subject-tab">Combustion</button>
  <button
    class="subject-tab"
    on:click={() => {
      selectedSubject = 'howto';
      selectedCalculator = '';
    }}>
    About Us
  </button>
</div>

<div class="section-divider"></div>

<div class="page">
  <div class="layout">
    <nav class="sidebar">
      <div class="button-group">
        <button
          class:selected={selectedCalculator === 'calc1'}
          on:click={() => {
            selectedCalculator = 'calc1';
            selectedSubject = '';
          }}>
          Conversion Calculator
        </button>

        <button
          class:selected={selectedCalculator === 'calc2'}
          on:click={() => {
            selectedCalculator = 'calc2';
            selectedSubject = '';
          }}>
          Table Search
        </button>

        <button
          class:selected={selectedCalculator === 'calc3'}
          on:click={() => {
            selectedCalculator = 'calc3';
            selectedSubject = '';
          }}>
          Calculator 3
        </button>

        <button
          class:selected={selectedCalculator === 'calc4'}
          on:click={() => {
            selectedCalculator = 'calc4';
            selectedSubject = '';
          }}>
          Calculator 4
        </button>

        <button
          class:selected={selectedCalculator === 'calc5'}
          on:click={() => {
          selectedCalculator = 'calc5';
          selectedSubject = '';
        }}>
        Practice Problems
      </button>

      </div>
    </nav>

    <main class="main-content">
      {#if selectedSubject === 'howto'}
        <div class="howto-content">
  <h2>About Us</h2>
  <p>
    Thermo Solver was created with one mission: to make the lives of students and engineers easier.
    We know how frustrating it can be to flip through tables, switch between unit systems, and calculate
    thermodynamic properties by hand. Our goal is to centralize everything into one easy-to-use platform,
    built by students, for students.
  </p>

  <h2>How to Use</h2>
  <p>
    Thermo Solver is a toolkit for engineering thermodynamics, fluid mechanics, and heat transfer calculations.
    Here's how to get started:
  </p>
  <ul>
    <li><strong>Sidebar Tools</strong>: Use the panel on the left to access calculators and property tables.</li>
    <li><strong>Conversion Calculator</strong>: Convert between common units quickly and accurately.</li>
    <li><strong>Table Search</strong>: Look up thermodynamic properties of fluids using real data.</li>
    <li><strong>Calculator 3 & 4</strong>: These sections will offer advanced tools in future updates.</li>
    <li><strong>Practice Problems</strong>: Improve and test your knowledge on various thermodynamics subjects.</li>
  </ul>
  <p>
    You can also use the subject tabs at the top to filter tools by topic — such as Thermodynamics, Fluids, or Combustion —
    to help tailor the experience to your coursework or project.
  </p>
</div>

      {:else if selectedCalculator === 'calc1'}
        <ConversionCalc />
      {:else if selectedCalculator === 'calc2'}
        <TableCalculation />
      {:else if selectedCalculator === 'calc3'}
        <p>Calculator 3 coming soon...</p>
      {:else if selectedCalculator === 'calc4'}
        <p>Calculator 4 coming soon...</p>
      {:else if selectedCalculator === 'calc5'}
      <PracticeProblems />
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
  background-color: #ffffff;
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
  background-color: #ffffff;
  margin-top: 24px;
}

.sidebar {
  width: 300px;
  height: 110%;
  padding: 0;
  display: flex;
  flex-direction: column;
  background: #f9f9f9;
  margin-top: -25px;
  max-width: 300px;
}

.button-group {
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: transparent;
  margin-top: 1px;
  gap: 2px;
  margin-right: 0px;
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
  width: 100%;
  box-sizing: border-box;
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

.subject-bar {
  background-color: #f3f3f3;
  padding: 8px 24px;
  display: flex;
  gap: 20px;
  border-bottom: 2px solid #ccc;
  align-items: center;
  justify-content: space-evenly;
}

.subject-tab {
  background: none;
  border: none;
  font-size: 1rem;
  font-weight: 600;
  padding: 8px 12px;
  color: #000000;
  cursor: pointer;
  border-bottom: 3px solid transparent;
  transition: border-color 0.2s ease, color 0.2s ease;
}

.subject-tab:hover {
  color: #7A0019;
  border-color: #7A0019;
}

.section-divider {
  width: 100%;
  height: 25px;
  background-color: #f9f9f9;
}

.howto-content {
  max-width: 800px;
    margin: -10px auto;
    padding: 30px 30px 30px 30px;
    background-color: white;
    color: #000;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
}

.howto-content h2 {
  color: #7A0019;
  font-weight: 800;
  font-size: 1.6rem;
  margin-bottom: 16px;
  border-bottom: 2px solid #eee;
  padding-bottom: 6px;
}

.howto-content p {
  margin-bottom: 20px;
  font-size: 1rem;
}

.howto-content ul {
  padding-left: 24px;
  margin-bottom: 20px;
}

.howto-content li {
  margin-bottom: 10px;
  font-size: 0.98rem;
}

</style>
