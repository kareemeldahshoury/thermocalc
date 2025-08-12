<script lang="ts">
  import TableCalculation from './tableCalculation.svelte';
  import ConversionCalc from './conversionCalc.svelte';
  import PracticeProblems from './PracticeProblems.svelte';
  import WorkCalculator from './workCalculator.svelte';
  import { onMount } from 'svelte';
  import OtherEquations from './otherEquations.svelte';



  let selectedCalculator = '';
  let query = '';
  let selectedSubject = '';

  let currentSlide = 0;
 const slides = [
  {
    type: 'logo',
    title: '',
    subtitle: '',
    cta: '',
    targetCalculator: ''
  },
  {
    title: 'Search Thermodynamics Tables Instantly',
    subtitle: 'Quick, accurate results for students and engineers',
    cta: 'Try the Tables Calculator',
    targetCalculator: 'calc2'
  },
  {
    title: 'Master Work Equations',
    subtitle: 'Adiabatic, polytropic, isothermal, and more',
    cta: 'Try the Work Calculator',
    targetCalculator: 'calc3'
  }
];

let interval: ReturnType<typeof setInterval> | null = null;

function startCarousel() {
  if (!interval) {
    interval = setInterval(() => {
      if (!selectedSubject && !selectedCalculator) {
        currentSlide = (currentSlide + 1) % slides.length;
      }
    }, 5000);
  }
}

function stopCarousel() {
  if (interval) {
    clearInterval(interval);
    interval = null;
    currentSlide = 0;
  }
}

$: {
  if (selectedSubject || selectedCalculator) {
    stopCarousel();
    currentSlide = 0;
  } else {
    startCarousel();
  }
}

onMount(() => {
  startCarousel();
});
</script>



<div class="carousel-banner">
 {#if slides[currentSlide].type === 'logo'}
  <button
    class="logo-button"
    on:click={() => {
      selectedSubject = '';
      selectedCalculator = '';
      currentSlide = 0;
    }}
  >
    <img src="/images/Logo2.png" alt="Thermo Solver" class="carousel-logo" />
  </button>
{:else}
    <h1>{slides[currentSlide].title}</h1>
    <p>{slides[currentSlide].subtitle}</p>
    {#if slides[currentSlide].cta}
      <button
        class="cta-btn"
        disabled={!!(selectedSubject || selectedCalculator)}
        on:click={() => {
          const calc = slides[currentSlide].targetCalculator;
          if (calc && !selectedCalculator && !selectedSubject) {
            selectedSubject = 'thermo';
            selectedCalculator = calc;
            document.querySelector('.main-content')?.scrollIntoView({ behavior: 'smooth' });
          }
        }}
      >
        {slides[currentSlide].cta}
      </button>
    {/if}
  {/if}
</div>




<div class="subject-bar">
  <button class="subject-tab" on:click={() => { selectedSubject = 'thermo'; selectedCalculator = 'calc1'; }}>Thermodynamics</button>
  <button class="subject-tab" on:click={() => { selectedSubject = 'fluids'; selectedCalculator = ''; }}>Fluids</button>
  <button class="subject-tab" on:click={() => { selectedSubject = 'heat'; selectedCalculator = ''; }}>Heat Transfer</button>
  <button class="subject-tab" on:click={() => { selectedSubject = 'combustion'; selectedCalculator = ''; }}>Combustion</button>
  <button class="subject-tab" on:click={() => { selectedSubject = 'howto'; selectedCalculator = ''; }}>About Us</button>
</div>

<div class="section-divider"></div>


<div class="page">
  <div class="layout">
    {#if selectedSubject === 'thermo'}
      <nav class="sidebar">
        <div class="button-group">
          <button
            class:selected={selectedCalculator === 'calc1'}
            on:click={() => { selectedCalculator = 'calc1'; }}>
            Conversion Calculator
          </button>

          <button
            class:selected={selectedCalculator === 'calc2'}
            on:click={() => { selectedCalculator = 'calc2'; }}>
            Table Search
          </button>

          <button
            class:selected={selectedCalculator === 'calc3'}
            on:click={() => { selectedCalculator = 'calc3'; }}>
            Work Process Calculator
          </button>

          <button
            class:selected={selectedCalculator === 'calc4'}
            on:click={() => { selectedCalculator = 'calc4'; }}>
            General Equations
          </button>

          <button
            class:selected={selectedCalculator === 'calc5'}
            on:click={() => { selectedCalculator = 'calc5'; }}>
            Practice Problems
          </button>

          <button
            class:selected={selectedCalculator === 'calc6'}
            on:click={() => { selectedCalculator = 'calc6'; }}>
            Key Equations
          </button>
        </div>
      </nav>
    {/if}

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
            <li><strong>Work Calculator</strong>: Solve for work from any of the thermodynamic processes.</li>
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
        <WorkCalculator />
      {:else if selectedCalculator === 'calc4'}
        <OtherEquations />
      {:else if selectedCalculator === 'calc5'}
        <PracticeProblems />
      {:else if selectedCalculator === 'calc6'}
      <p> test </p>
      {:else}
        <p></p>
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


.carousel-banner {
  background: linear-gradient(to right, #7A0019, #f78b00);
  padding: 20px 10px;
  text-align: center;
  color: white;
  transition: all 0.6s ease-in-out;
  height: 190px;
  overflow: hidden
}


.carousel-logo {
  height: 110px; 
  max-width: none;     
  margin: 0 auto 20px auto;
  display: block;
  margin-top: 10px;
}



.carousel-banner h1 {
  font-size: clamp(1.25rem, 2vw, 1.75rem);
  font-weight: 800;
  margin-bottom: 12px;
}

.carousel-banner p {
  font-size: clamp(0.95rem, 1.6vw, 1.05rem);
  margin-bottom: 20px;
}

.cta-btn {
  background: white;
  color: #7A0019;
  font-weight: bold;
  border: none;
  padding: 12px 24px;
  font-size: 1rem;
  border-radius: 30px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.cta-btn:hover {
  background: #f3f3f3;
}

.logo-button {
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
}

.logo-button:focus {
  outline: none;
}



</style>
