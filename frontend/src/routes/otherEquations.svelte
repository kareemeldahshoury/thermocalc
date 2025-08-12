<script lang="ts">
  // ---------- Types ----------
  type VarDef = { id: string; label: string; placeholder?: string };
  type EqDef = { id: string; title: string; variables: VarDef[] };

  // ---------- Equations list (UI only) ----------
  const EQUATIONS: EqDef[] = [
    {
      id: 'refEfficency',
      title: 'Refrigeration COP',
      variables: [
        { id: 'COP', label: 'Coefficient of Performance <i>(COP)</i>', placeholder: 'e.g., 2.5' },
        { id: 'Qc',  label: 'Cooling Load <i>(Q<sub>c</sub>, kW)</i>',  placeholder: 'e.g., 500' },
        { id: 'Qh',  label: 'Heat Rejected <i>(Q<sub>h</sub>, kW)</i>', placeholder: 'e.g., 800' }
      ]
    },
    {
      id: 'erb1SteadyState',
      title: 'Energy Rate Balance at Steady State (1 inlet/1 outlet)',
      variables: [
        { id: 'Qdot', label: 'Heat Transfer Rate <i>(Q̇<sub>cv</sub>, kW)</i>', placeholder: 'e.g., 50' },
        { id: 'Wdot', label: 'Work Rate (out) <i>(Ẇ<sub>cv</sub>, kW)</i>',   placeholder: 'e.g., 20' },
        { id: 'mdot', label: 'Mass Flow Rate <i>(ṁ, kg/s)</i>',              placeholder: 'e.g., 1.2' },
        { id: 'h1',   label: 'Inlet Enthalpy <i>(h<sub>1</sub>, kJ/kg)</i>',  placeholder: 'e.g., 3200' },
        { id: 'h2',   label: 'Exit Enthalpy <i>(h<sub>2</sub>, kJ/kg)</i>',   placeholder: 'e.g., 2600' },
        { id: 'V1',   label: 'Inlet Velocity <i>(V<sub>1</sub>, m/s)</i>',    placeholder: 'e.g., 30' },
        { id: 'V2',   label: 'Exit Velocity <i>(V<sub>2</sub>, m/s)</i>',     placeholder: 'e.g., 10' },
        { id: 'z1',   label: 'Inlet Elevation <i>(z<sub>1</sub>, m)</i>',     placeholder: 'e.g., 12' },
        { id: 'z2',   label: 'Exit Elevation <i>(z<sub>2</sub>, m)</i>',      placeholder: 'e.g., 3' }
      ]
    }
  ];


  const UNITS: Record<string, Record<string, string>> = {
    refEfficency: { COP: '', Qc: 'kW', Qh: 'kW' },
    erb1SteadyState: {
      Qdot: 'kW', Wdot: 'kW', mdot: 'kg/s',
      h1: 'kJ/kg', h2: 'kJ/kg', V1: 'm/s', V2: 'm/s', z1: 'm', z2: 'm'
    }
  };

  const SYMBOLS: Record<string, Record<string, string>> = {
  refEfficency: {
    COP: 'COP',
    Qc: 'Q<sub>c</sub>',
    Qh: 'Q<sub>h</sub>'
  },
  erb1SteadyState: {
    Qdot: 'Q̇<sub>cv</sub>',
    Wdot: 'Ẇ<sub>cv</sub>',
    mdot: 'ṁ',
    h1: 'h<sub>1</sub>',
    h2: 'h<sub>2</sub>',
    V1: 'V<sub>1</sub>',
    V2: 'V<sub>2</sub>',
    z1: 'z<sub>1</sub>',
    z2: 'z<sub>2</sub>'
  }
};

function symbolFor(eqId: string, varId: string): string {
  return SYMBOLS[eqId]?.[varId] ?? varId;
}


  function unitFor(eqId: string, varId: string): string {
    return UNITS[eqId]?.[varId] ?? '';
  }

  function formatNumber(n: number) {
    return n.toLocaleString(undefined, { maximumFractionDigits: 2 });
  }


  let selectedEqId = '';
  let solveFor = '';
  let inputs: Record<string, string> = {};
  let resultMessage: number | string | Record<string, unknown> = '';
  let errorMsg = '';

  let currentEq: EqDef | null = null;
  $: currentEq = EQUATIONS.find((e) => e.id === selectedEqId) ?? null;

  const main = (html: string) => (html.includes('<i>') ? html.split('<i>')[0] : html);
  const small = (html: string) => (html.includes('<i>') ? html.split('<i>')[1].replace('</i>', '') : '');

  function symbolHTML(v: VarDef): string {
    const s = small(v.label);
    if (!s) return v.id;
    const inside = s.trim().replace(/^\(|\)$/g, '');
    const first = inside.split(',')[0]?.trim();
    return first || v.id;
  }

  function resetForm(eq: EqDef) {
    solveFor = '';
    inputs = {};
    resultMessage = '';
    errorMsg = '';
  }


  async function calculate() {
    errorMsg = '';
    resultMessage = '';

    const eq = currentEq;
    if (!eq) { errorMsg = 'Choose a calculation.'; return; }
    if (!solveFor) { errorMsg = 'Choose what to solve for.'; return; }

    const payloadInputs: Record<string, number> = {};
    for (const v of eq.variables) {
      if (v.id === solveFor) continue;
      const raw = inputs[v.id];
      if (raw == null || raw === '') {
        errorMsg = `Missing input: ${v.id}`;
        return;
      }
      const num = Number(raw);
      if (!Number.isFinite(num)) {
        errorMsg = `Invalid number for ${v.id}`;
        return;
      }
      payloadInputs[v.id] = num;
    }

    const payload = {
      equationId: eq.id,
      solveFor,
      inputs: payloadInputs
    };

    try {
      const res = await fetch('http://localhost:8000/api/calculate/general', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error((await res.text()) || 'Server error');

      const data = await res.json();

      if (typeof data === 'number') {
        resultMessage = data;
      } else if ('value' in (data as any)) {
        const v = (data as any).value;
        const u = (data as any).unit ? ` ${(data as any).unit}` : '';
        resultMessage = `${v}${u}`;
      } else if ('result' in (data as any)) {
        resultMessage = (data as any).result;
      } else {
        resultMessage = data;
      }
    } catch (e: any) {
      errorMsg = e?.message ?? 'Unknown error';
    }
  }
</script>

<div class="container">
  <h2>General Equations Calculator</h2>

  <label for="eq">Select Calculation:</label>
  <select
    id="eq"
    bind:value={selectedEqId}
    on:change={() => {
      const eq = EQUATIONS.find(e => e.id === selectedEqId);
      if (eq) resetForm(eq);
    }}
  >
    <option value="">-- Choose --</option>
    {#each EQUATIONS as eq}
      <option value={eq.id}>{eq.title}</option>
    {/each}
  </select>

  {#if currentEq}
    <span id="solvefor-label" class="group-label">What do you want to solve for?</span>
    <div class="var-buttons" role="group" aria-labelledby="solvefor-label">
      {#each currentEq.variables as v}
        <button
          type="button"
          class:active={solveFor === v.id}
          on:click={() => { solveFor = v.id; resultMessage = ''; errorMsg = ''; }}
          aria-pressed={solveFor === v.id}
        >
          {@html symbolHTML(v)}
        </button>
      {/each}
    </div>

    {#if solveFor}
      {#each currentEq.variables.filter(v => v.id !== solveFor) as v (v.id)}
        <label for={`var-${v.id}`}>
          {@html main(v.label)}
          <span class="small">{@html small(v.label)}</span>
        </label>
        <input
          id={`var-${v.id}`}
          type="text"
          bind:value={inputs[v.id]}
          placeholder={v.placeholder ?? ''} />
      {/each}

      <button class="calculate-btn" on:click={calculate}>Calculate</button>
    {/if}

    {#if errorMsg}
      <p class="error">{errorMsg}</p>
    {/if}

    {#if resultMessage && !errorMsg}
      <div class="result-info">
        <strong>Result:</strong>

        {#if typeof resultMessage === 'object'}
          <table>
 <thead>
  <tr>
    {#each Object.entries(resultMessage) as [key, _]}
      <th>{@html symbolFor(selectedEqId, key)}</th>
    {/each}
  </tr>
</thead>
<tbody>
  <tr>
    {#each Object.entries(resultMessage) as [key, val]}
      <td>
        {#if typeof val === 'number'}
          {formatNumber(val)} {unitFor(selectedEqId, key)}
        {:else}
          {val}
        {/if}
      </td>
    {/each}
  </tr>
</tbody>

          </table>
        {:else}
          <table>
<thead>
  <tr>
    <th>{@html symbolFor(selectedEqId, solveFor)}</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>{formatNumber(Number(resultMessage))} {unitFor(selectedEqId, solveFor)}</td>
  </tr>
</tbody>

          </table>
        {/if}
      </div>
    {/if}
  {/if}
</div>

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
    color: #7A0019;
    font-weight: 700;
    margin-top: 27px;
    margin-bottom: 6px;
  }

  label {
    display: block;
    font-size: 1rem;
    margin-top: 28px;
    color: #222;
    font-weight: 700;
  }

  .small { font-size: .85em; color: #555; }

  select, input {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    background: #f2f2f2;
    color: #333;
    margin-top: 6px;
  }

  .group-label {
    display: block;
    font-size: 1rem;
    margin-top: 28px;
    margin-bottom: 6px;
    color: #222;
    font-weight: 700;
  }

  .var-buttons {
    display: flex;
    gap: 8px;
    margin-top: 10px;
    flex-wrap: wrap;
  }

  .var-buttons button {
    background: #f2f2f2;
    color: #333;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 8px 12px;
    cursor: pointer;
    transition: transform .05s ease, background .2s;
  }
  .var-buttons button.active,
  .var-buttons button[aria-pressed="true"] {
    background: #7A0019;
    color: #fff;
    border-color: #7A0019;
  }
  .var-buttons button:focus-visible {
    outline: 2px solid #7A0019;
    outline-offset: 2px;
    box-shadow: 0 0 0 2px #fff;
  }
  .var-buttons button:active { transform: translateY(1px); }

  .calculate-btn {
    background: #7A0019;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background .2s ease;
    margin-top: 35px;
  }
  .calculate-btn:hover { background: #9c0033; }

  .error {
    color: #fff;
    background:#b00020;
    padding: 10px;
    border-radius: 6px;
    max-width: 600px;
    margin-top: 14px;
  }

  .result-info {
    margin-top: 18px;
  }

  table {
    width: 100%;
    margin-top: 14px;
    border-collapse: collapse;
  }
  th, td {
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
</style>
