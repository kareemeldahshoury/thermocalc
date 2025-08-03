<script lang="ts">
  let selectedProcess: string = '';
  let selectedEquation: string = '';
  let inputValues: Record<string, string> = {};
  let resultMessage: string | Record<string, number> = '';
  let lastInputs: Record<string, string> = {};
  let lastProcess: string = '';

  const processOptions = [
    { id: 'Isobaric', label: 'Isobaric Process' },
    { id: 'Isothermal', label: 'Isothermal Process' },
    { id: 'Adiabatic', label: 'Adiabatic Process' },
    { id: 'Polytropic', label: 'Polytropic Process' },
  ];

  const processEquations: Record<string, Array<{ id: string; label: string }>> = {
    Isobaric: [
      { id: 'basic', label: 'W = P(V₂ - V₁)' },
    ],
    Isothermal: [
      { id: 'nRT', label: 'W = nRT ln(V₂ / V₁)' },
      { id: 'P1V1', label: 'W = P₁V₁ ln(V₂ / V₁)' },
    ],
    Adiabatic: [
      { id: 'PV', label: 'W = [P₂V₂ - P₁V₁] / (1 - γ)' },
      { id: 'TV', label: 'W = nR(T₂ - T₁) / (1 - γ)' },
      { id: 'VV', label: 'W = P₁V₁ / (γ - 1) * [1 - (V₁/V₂)<sup>γ-1</sup>]' },
    ],
    Polytropic: [
      { id: 'PV', label: 'W = [P₂V₂ - P₁V₁] / (1 - n)' },
      { id: 'TV', label: 'W = mR(T₂ - T₁) / (1 - n)' },
    ]
  };

  const equationInputs: Record<string, Record<string, Array<{ id: string; label: string }>>> = {
    Isobaric: {
      basic: [
        { id: 'P', label: 'Pressure <i>(P, bar)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
      ]
    },
    Isothermal: {
      nRT: [
        { id: 'n', label: 'Moles <i>(n)</i>' },
        { id: 'T', label: 'Temperature <i>(T, K)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
      ],
      P1V1: [
        { id: 'P1', label: 'Initial Pressure <i>(P<sub>1</sub>, bar)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
      ]
    },
    Adiabatic: {
      PV: [
        { id: 'P1', label: 'Initial Pressure <i>(P<sub>1</sub>, bar)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'P2', label: 'Final Pressure <i>(P<sub>2</sub>, bar)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
        { id: 'gamma', label: 'γ' }
      ],
      TV: [
        { id: 'n', label: 'Moles <i>(n)</i>' },
        { id: 'T1', label: 'Initial Temperature <i>(T<sub>1</sub>, K)</i>' },
        { id: 'T2', label: 'Final Temperature <i>(T<sub>2</sub>, K)</i>' },
        { id: 'gamma', label: 'γ' }
      ],
      VV: [
        { id: 'P1', label: 'Initial Pressure <i>(P<sub>1</sub>, bar)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
        { id: 'gamma', label: 'γ' }
      ]
    },
    Polytropic: {
      PV: [
        { id: 'P1', label: 'Initial Pressure <i>(P<sub>1</sub>, bar)</i>' },
        { id: 'V1', label: 'Initial Volume <i>(V<sub>1</sub>, m³)</i>' },
        { id: 'P2', label: 'Final Pressure <i>(P<sub>2</sub>, bar)</i>' },
        { id: 'V2', label: 'Final Volume <i>(V<sub>2</sub>, m³)</i>' },
        { id: 'n', label: 'n' }
      ],
      TV: [
        { id: 'm', label: 'Mass <i>(kg)</i>' },
        { id: 'T1', label: 'Initial Temperature <i>(T<sub>1</sub>, K)</i>' },
        { id: 'T2', label: 'Final Temperature <i>(T<sub>2</sub>, K)</i>' },
        { id: 'n', label: 'n' }
      ]
    }
  };

  function tryParse(val: string): number | null {
    const num = parseFloat(val);
    return isNaN(num) ? null : num;
  }

  function calculateFrontend() {
    const inputs = inputValues;
    let result: Record<string, number> = {};

    try {
      switch (selectedProcess) {
        case 'Isobaric':
          if (selectedEquation === 'basic') {
            const P = tryParse(inputs.P);
            const V1 = tryParse(inputs.V1);
            const V2 = tryParse(inputs.V2);
            if (P == null || V1 == null || V2 == null) throw new Error('Invalid input');
            result.Work = Number((P * 1e5 * (V2 - V1)).toFixed(2));
          }
          break;

        case 'Isothermal':
          if (selectedEquation === 'nRT') {
            const n = tryParse(inputs.n);
            const T = tryParse(inputs.T);
            const V1 = tryParse(inputs.V1);
            const V2 = tryParse(inputs.V2);
            if (n == null || T == null || V1 == null || V2 == null) throw new Error('Invalid input');
            result.Work = Number((n * 8.314 * T * Math.log(V2 / V1)).toFixed(2));
          } else if (selectedEquation === 'P1V1') {
            const P1 = tryParse(inputs.P1);
            const V1 = tryParse(inputs.V1);
            const V2 = tryParse(inputs.V2);
            if (P1 == null || V1 == null || V2 == null) throw new Error('Invalid input');
            result.Work = Number((P1 * 1e5 * V1 * Math.log(V2 / V1)).toFixed(2));
          }
          break;

        case 'Adiabatic':
          if (selectedEquation === 'PV') {
            const P1 = tryParse(inputs.P1);
            const V1 = tryParse(inputs.V1);
            const P2 = tryParse(inputs.P2);
            const V2 = tryParse(inputs.V2);
            const gamma = tryParse(inputs.gamma);
            if (P1 == null || V1 == null || P2 == null || V2 == null || gamma == null) throw new Error('Invalid input');
            result.Work = Number(((P2 * 1e5 * V2 - P1 * 1e5 * V1) / (1 - gamma)).toFixed(2));
          } else if (selectedEquation === 'TV') {
            const n = tryParse(inputs.n);
            const T1 = tryParse(inputs.T1);
            const T2 = tryParse(inputs.T2);
            const gamma = tryParse(inputs.gamma);
            if (n == null || T1 == null || T2 == null || gamma == null) throw new Error('Invalid input');
            result.Work = Number((n * 8.314 * (T2 - T1) / (1 - gamma)).toFixed(2));
          } else if (selectedEquation === 'VV') {
            const P1 = tryParse(inputs.P1);
            const V1 = tryParse(inputs.V1);
            const V2 = tryParse(inputs.V2);
            const gamma = tryParse(inputs.gamma);
            if (P1 == null || V1 == null || V2 == null || gamma == null) throw new Error('Invalid input');
            result.Work = Number(((P1 * 1e5 * V1) / (gamma - 1) * (1 - Math.pow(V1 / V2, gamma - 1))).toFixed(2));
          }
          break;

        case 'Polytropic':
          if (selectedEquation === 'PV') {
            const P1 = tryParse(inputs.P1);
            const V1 = tryParse(inputs.V1);
            const P2 = tryParse(inputs.P2);
            const V2 = tryParse(inputs.V2);
            const n = tryParse(inputs.n);
            if (P1 == null || V1 == null || P2 == null || V2 == null || n == null) throw new Error('Invalid input');
            result.Work = Number(((P2 * 1e5 * V2 - P1 * 1e5 * V1) / (1 - n)).toFixed(2));
          } else if (selectedEquation === 'TV') {
            const m = tryParse(inputs.m);
            const T1 = tryParse(inputs.T1);
            const T2 = tryParse(inputs.T2);
            const n = tryParse(inputs.n);
            if (m == null || T1 == null || T2 == null || n == null) throw new Error('Invalid input');
            result.Work = Number((m * 287 * (T2 - T1) / (1 - n)).toFixed(2));
          }
          break;

        default:
          throw new Error('Unknown process');
      }

      resultMessage = result;
      lastInputs = { ...inputValues };
      lastProcess = selectedProcess;
    } catch (error) {
      resultMessage = 'Error: ' + (error as Error).message;
    }
  }

  function formatPlaceholder(id: string): string {
  const subscriptMap: Record<string, string> = {
    V1: 'V₁',
    V2: 'V₂',
    P1: 'P₁',
    P2: 'P₂',
    T1: 'T₁',
    T2: 'T₂',
    n: 'n',
    m: 'm',
    T: 'T',
    P: 'P',
    V: 'V',
    gamma: 'γ'
  };

  return subscriptMap[id] || id;
}

</script>

<div class="container">
  <div class="header-row">
  <h2>Thermodynamic Work Calculator</h2>
</div>

<div class="button-wrapper">
  <button class="top-right-button">Processes Information</button>
</div>


  <label for="process">Select Thermodynamic Process:</label>
  <select
  id="process"
  bind:value={selectedProcess}
  on:change={() => {
    selectedEquation = '';
    resultMessage = '';
    lastInputs = {};
    lastProcess = '';
    inputValues = {};
  }}
>
    <option value="">-- Select a process --</option>
    {#each processOptions as process}
      <option value={process.id}>{process.label}</option>
    {/each}
  </select>

  {#if selectedProcess}
    <label for="equation">Select Equation:</label>
    <div class="equation-buttons">
      {#each processEquations[selectedProcess] as equation}
        <button
  type="button"
  class:selected={selectedEquation === equation.id}
  on:click={() => {
    selectedEquation = equation.id;
    resultMessage = '';
    lastInputs = {};
    lastProcess = '';
  }}
>
          {@html equation.label}
        </button>
      {/each}
    </div>
  {/if}

  {#if selectedEquation && equationInputs[selectedProcess]?.[selectedEquation]}
    {#each equationInputs[selectedProcess][selectedEquation] as input}
      <label for={input.id}>{@html input.label}:</label>
      <input
        id={input.id}
        type="text"
        bind:value={inputValues[input.id]}
        placeholder={`Enter ${formatPlaceholder(input.id)}`}
      />
    {/each}

    <button class="calculate-btn" on:click={calculateFrontend}>Calculate Work</button>
  {/if}

  {#if resultMessage}
    <div class="result-info">
      <strong>Result for {lastProcess} Process:</strong>
      {#if typeof resultMessage === 'object' && resultMessage !== null}
        <table>
          <thead>
            <tr>
              {#each Object.entries(resultMessage) as [key, _]}
                <th>{key}</th>
              {/each}
            </tr>
          </thead>
          <tbody>
            <tr>
              {#each Object.entries(resultMessage) as [_, value]}
                <td>{(value / 1000).toFixed(4)} kJ</td>
              {/each}
            </tr>
          </tbody>
        </table>
      {:else}
        <p class="error-message">{resultMessage}</p>
      {/if}
    </div>
  {/if}
</div>


<style>
  :global(body) {
  background-color: #7A0019;
    margin: 0;
    font-family: 'Latin Modern Math', 'STIX Two Math', 'Cambria Math', serif;
    color: white;
  }

.container {
  max-width: 800px;
    margin: -10px auto;
    padding: 5px 30px 30px 30px;
    background-color: white;
    color: #000;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    font-family: system-ui, sans-serif;
}

h2 {
  font-size: 1.4rem;
  color: #800000; /* maroon */
  font-weight: 700;
  margin-top: 27px;
  text-align: left;
}

label {
  display: block;
  font-size: 1.05rem;
  margin-top: 34px;
  color: #222;
  font-weight: 700
}

select,
input {
  width: 100%;
  padding: 12px;
  font-size: 1rem;
  border-radius: 8px;
  border: 1px solid #ccc;
  box-sizing: border-box;
  background-color: #f2f2f2;
  color: #333;
  margin-top: 6px;
}

input::placeholder {
  color: #888;
}

input:disabled {
  background-color: #f2f2f2;
  color: #888;
  cursor: not-allowed;
}

.equation-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 16px;
}

.equation-buttons :global(button.selected) {
  background-color: #7A0019;
  color: white;
  border-color: #0077cc;
}

.equation-buttons button {
  background-color: #f2f2f2;
  border: 1px solid #ccc;
  padding: 8px 14px;
  font-size: 0.95rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
  color: #333;
}

.calculate-btn {
  background-color: #7A0019;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease;
    margin-top: 40px;
}

.calculate-btn:hover {
  background-color: #9c0033;
}

.result-info {
  margin-top: 12px;
  padding: 16px 20px;
  border-radius: 6px;
}

.result-info strong {
  font-size: 1.1rem;
  color: #333;
}

table {
  width: 100%;
  margin-top: 14px;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ddd;
  padding: 10px;
  font-size: 0.95rem;
  text-align: center;
}

th {
  background-color: #f5f5f5;
  font-weight: bold;
  color: #333;
}

.error-message {
  color: #c00;
  font-weight: 600;
  margin-top: 10px;
  text-align: center;
}

.button-wrapper {
  display: flex;
  justify-content: flex-end;
}

.top-right-button {
  background-color: #7A0019;
  color: white;
  border: none;
  padding: 8px 16px;
  font-size: 0.95rem;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-top: -32px
}



</style>