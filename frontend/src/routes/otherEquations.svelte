<script lang="ts">

  type VarDef = { id: string; label: string; placeholder?: string };
  type EqDef = { id: string; title: string; variables: VarDef[] };

  let useWorkInstead = false;
  let searchText = "";
  let gammaMode: "TP" | "PV" | "TV" = "TP";


  const EQUATIONS: EqDef[] = [
    {
      id: 'carnotEfficiency',
      title: 'Ideal Carnot Cycle Efficiency',
      variables: [
        { id: 'ccEff', label: 'Carnot Efficiency', placeholder: 'e.g., 0.5' },
        { id: 'TH', label: 'High Temperature Reservoir', placeholder: 'e.g., 600' },
        { id: 'TL', label: 'Low Temperature Reservoir', placeholder: 'e.g., 300' },
      ]
    },
    {
      id: 'heatPumpEfficiency',
      title: 'Heat Pump COP',
      variables: [
        { id: 'COP', label: 'Coefficient of Performance', placeholder: 'e.g., 4.0' },
        { id: 'Qh',  label: 'Heat Delivered', placeholder: 'e.g., 800' },
        { id: 'Qc',  label: 'Cooling Load', placeholder: 'e.g., 500' },
        { id: 'Wnet', label: 'Net Work', placeholder: 'e.g., 300' },
      ]
    },
    {
      id: 'refEfficency',
      title: 'Refrigeration COP',
      variables: [
        { id: 'COP', label: 'Coefficient of Performance', placeholder: 'e.g., 2.5' },
        { id: 'Qc',  label: 'Cooling Load',  placeholder: 'e.g., 500' },
        { id: 'Qh',  label: 'Heat Rejected', placeholder: 'e.g., 800' },
        { id: 'Wnet', label: 'Net Work', placeholder: 'e.g., 800' },
      ]
    },
    {
      id: 'massFlowRate',
      title: 'Mass Flow Rate from Specific Volume',
      variables: [
        { id: 'mdot', label: 'Mass Flow Rate', placeholder: 'e.g., 2.5' },
        { id: 'V', label: 'Velocity', placeholder: 'e.g., 0.01' },
        { id: 'A', label: 'Area', placeholder: 'e.g., 4.2'},
        { id: 'v',    label: 'Specific Volume', placeholder: 'e.g., 0.005' },
      ]
    },
    {
      id: 'erb1SteadyState',
      title: 'Energy Rate Balance at Steady State (1 inlet/1 outlet)',
      variables: [
        { id: 'Qdot', label: 'Heat Transfer Rate', placeholder: 'e.g., 50' },
        { id: 'Wdot', label: 'Work Rate',   placeholder: 'e.g., 20' },
        { id: 'mdot', label: 'Mass Flow Rate', placeholder: 'e.g., 1.2' },
        { id: 'h1',   label: 'Inlet Enthalpy',  placeholder: 'e.g., 3200' },
        { id: 'h2',   label: 'Exit Enthalpy',   placeholder: 'e.g., 2600' },
        { id: 'V1',   label: 'Inlet Velocity',    placeholder: 'e.g., 30' },
        { id: 'V2',   label: 'Exit Velocity',     placeholder: 'e.g., 10' },
        { id: 'z1',   label: 'Inlet Elevation',   placeholder: 'e.g., 12' },
        { id: 'z2',   label: 'Exit Elevation',    placeholder: 'e.g., 3' }
      ]
    },
    {
      id: 'idealGasLaw',
      title: 'Ideal Gas Law',
      variables: [
        { id: 'P', label: 'Pressure', placeholder: 'e.g., 101325' },
        { id: 'V', label: 'Volume', placeholder: 'e.g., 0.1' },
        { id: 'T', label: 'Temperature', placeholder: 'e.g., 300' },
        { id: 'n', label: 'Moles', placeholder: 'e.g., 2' },
        { id: 'm', label: 'Mass', placeholder: 'e.g., 0.058' },
        { id: 'M', label: 'Molar Mass', placeholder: 'e.g., 0.029' }
      ]
    },
    {
  id: 'isentropicRelations',
  title: 'Isentropic Relations',
  variables: [
    { id: 'P1', label: 'Initial Pressure', placeholder: 'e.g., 101325' },
    { id: 'P2', label: 'Final Pressure', placeholder: 'e.g., 202650' },
    { id: 'T1', label: 'Initial Temperature', placeholder: 'e.g., 300' },
    { id: 'T2', label: 'Final Temperature', placeholder: 'e.g., 400' },
    { id: 'V1', label: 'Initial Volume', placeholder: 'e.g., 0.1' },
    { id: 'V2', label: 'Final Volume', placeholder: 'e.g., 0.05' },
    { id: 'gamma', label: 'Heat Capacity Ratio', placeholder: 'e.g., 1.4' }
  ]
}


      
  ];

  const UNITS: Record<string, Record<string, string>> = {
    refEfficency: { COP: '', Qc: 'kW', Qh: 'kW', Wnet: 'kW' },
    heatPumpEfficiency: { COP: '', Qc: 'kW', Qh: 'kW', Wnet: 'kW' },
    erb1SteadyState: {
      Qdot: 'kW', Wdot: 'kW', mdot: 'kg/s',
      h1: 'kJ/kg', h2: 'kJ/kg', V1: 'm/s', V2: 'm/s', z1: 'm', z2: 'm'
    },
    carnotEfficiency: { TH: 'K', TL: 'K', ccEff: '' },
    massFlowRate: {
      mdot: 'kg/s',
      V: 'm/s',
      A: 'm²',
      v: 'm³/kg'
    },
    idealGasLaw: {
      P: 'Pa',
      V: 'm³',
      T: 'K',
      n: 'mol',
      m: 'kg',
      M: 'kg/mol'
    },
    isentropicRelations: {
      P1: 'Pa', P2: 'Pa',
      T1: 'K', T2: 'K',
      V1: 'm³', V2: 'm³',
      gamma: ''
    }


  };

  const SYMBOLS: Record<string, Record<string, string>> = {
    refEfficency: {
      COP: 'COP<sub>R</sub>',
      Qc: 'Q<sub>c</sub>',
      Qh: 'Q<sub>h</sub>',
      Wnet: 'W<sub>net</sub>'
    },
    heatPumpEfficiency: {
      COP: 'COP<sub>HP</sub>',
      Qc: 'Q<sub>c</sub>',
      Qh: 'Q<sub>h</sub>',
      Wnet: 'W<sub>net</sub>'
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
    },
    carnotEfficiency: { TH: 'T<sub>H</sub>', TL: 'T<sub>L</sub>', ccEff: 'η' },
    massFlowRate: {
      mdot: 'ṁ',
      V: 'V',
      A: 'A',
      v: 'v̅'
    },
    idealGasLaw: {
      P: 'P',
      V: 'V',
      T: 'T',
      n: 'n',
      m: 'm',
      M: 'M'
    },
    isentropicRelations: {
      P1: 'P₁', P2: 'P₂',
      T1: 'T₁', T2: 'T₂',
      V1: 'V₁', V2: 'V₂',
      gamma: 'γ'
    }



  };

  function symbolFor(eqId: string, varId: string): string {
    return SYMBOLS[eqId]?.[varId] ?? varId;
  }

  function labelFor(eqId: string, varId: string): string {
    const eq = EQUATIONS.find(e => e.id === eqId);
    const variable = eq?.variables.find(v => v.id === varId);
    return variable?.label ?? varId;
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

  $: activeVariables = currentEq?.variables ?? [];

  function resetForm(eq: EqDef) {
    solveFor = '';
    inputs = {};
    resultMessage = '';
    errorMsg = '';
    useWorkInstead = false;
  }

  function requiredInputs(eqId: string, solveFor: string): string[] {
  if (eqId === "refEfficency") {
    if (solveFor === "COP") return ["Qc", useWorkInstead ? "Wnet" : "Qh"];
    if (solveFor === "Qc") return ["COP", useWorkInstead ? "Wnet" : "Qh"];
    if (solveFor === "Qh") return ["COP", "Qc"];
    if (solveFor === "Wnet") return ["COP", "Qc"];
  }

  if (eqId === "heatPumpEfficiency") {
  if (solveFor === "COP") return ["Qh", useWorkInstead ? "Wnet" : "Qc"];
  if (solveFor === "Qh") return ["COP", useWorkInstead ? "Wnet" : "Qc"];
  if (solveFor === "Qc") return ["COP", "Qh"];
  if (solveFor === "Wnet") return ["COP", "Qh"];
}
if (eqId === "idealGasLaw") {
  if (solveFor === "P") return ["V", "T", useWorkInstead ? "m" : "n", ...(useWorkInstead ? ["M"] : [])];
  if (solveFor === "V") return ["P", "T", useWorkInstead ? "m" : "n", ...(useWorkInstead ? ["M"] : [])];
  if (solveFor === "T") return ["P", "V", useWorkInstead ? "m" : "n", ...(useWorkInstead ? ["M"] : [])];

  if (solveFor === "n") return ["P", "V", "T"];
  if (solveFor === "m") return ["P", "V", "T", "M"];
  if (solveFor === "M") return ["P", "V", "T", "m"];
}

if (eqId === "isentropicRelations") {
  if (solveFor === "T1") {
    if (useWorkInstead) return ["T2", "V1", "V2", "gamma"];
    else return ["T2", "P1", "P2", "gamma"];                
  }
  if (solveFor === "T2") {
    if (useWorkInstead) return ["T1", "V1", "V2", "gamma"];
    else return ["T1", "P1", "P2", "gamma"];
  }

  if (solveFor === "P1") {
    if (useWorkInstead) return ["P2", "V1", "V2", "gamma"];
    else return ["P2", "T1", "T2", "gamma"];
  }
  if (solveFor === "P2") {
    if (useWorkInstead) return ["P1", "V1", "V2", "gamma"];
    else return ["P1", "T1", "T2", "gamma"];
  }

  if (solveFor === "V1") {
    if (useWorkInstead) return ["V2", "T1", "T2", "gamma"];
    else return ["V2", "P1", "P2", "gamma"];
  }
  if (solveFor === "V2") {
    if (useWorkInstead) return ["V1", "T1", "T2", "gamma"];
    else return ["V1", "P1", "P2", "gamma"];
  }

  if (solveFor === "gamma") {
    if (gammaMode === "TP") return ["T1", "T2", "P1", "P2"];
    if (gammaMode === "PV") return ["P1", "P2", "V1", "V2"];
    if (gammaMode === "TV") return ["T1", "T2", "V1", "V2"];
  }
}



  if (eqId === "erb1SteadyState" || eqId === "carnotEfficiency" || eqId == "massFlowRate") {
    return activeVariables.map(v => v.id).filter(id => id !== solveFor);
  }

  return [];
}


  async function calculate() {
    errorMsg = '';
    resultMessage = '';

    const eq = currentEq;
    if (!eq) { errorMsg = 'Choose a calculation.'; return; }
    if (!solveFor) { errorMsg = 'Choose what to solve for.'; return; }

    const payloadInputs: Record<string, number> = {};
    const needed = requiredInputs(eq.id, solveFor);

    for (const id of needed) {
      const raw = inputs[id];
      if (!raw) { errorMsg = `Missing input: ${id}`; return; }
      const num = Number(raw);
      if (!Number.isFinite(num)) {
        errorMsg = `Invalid number for ${id}`; return;
      }
      payloadInputs[id] = num;
    }

    const payload = { equationId: eq.id, solveFor, inputs: payloadInputs };

    try {
      const res = await fetch('http://localhost:8000/api/calculate/general', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });

      const raw = await res.text();
      let data: any = null;
      try { data = raw ? JSON.parse(raw) : null; } catch {}

      if (!res.ok) {
        const msg = (data && (data.detail || data.error || data.message)) || raw || 'Server error';
        errorMsg = msg;
        return;
      }

      if (typeof data === 'number') { resultMessage = data; return; }
      if (data && typeof data.value === 'number') { resultMessage = data; return; }
      if (data && typeof data.result === 'number') { resultMessage = data.result; return; }
      if (data && data.result && typeof data.result === 'object') { resultMessage = data.result; return; }

      if (typeof data === 'string') { errorMsg = data; return; }
      if (data && typeof data.result === 'string') {
        const msg = String(data.result).trim().replace(/^"|"$/g, '').replace(/^Error:\s*/i, '');
        errorMsg = `Error: ${msg}`; resultMessage = ''; return;
      }

      errorMsg = (data && (data.detail || data.error || data.message)) || 'An error occurred';
      resultMessage = '';
    } catch (e: any) {
      errorMsg = e?.message ?? 'Unknown error';
    }
  }
</script>

<div class="container">
  <h2>General Equations Calculator</h2>

<label for="eqDropdown">Select Calculation:</label>
<select
  id="eqDropdown"
  bind:value={selectedEqId}
  on:change={() => {

    solveFor = "";
    inputs = {};
    resultMessage = "";  
    errorMsg = "";
    useWorkInstead = false;

    const match = EQUATIONS.find(e => e.id === selectedEqId);
    if (!match) {
      selectedEqId = "";
    }
  }}
>
  <option value="" disabled selected>Select an option...</option>
  {#each EQUATIONS as eq}
    <option value={eq.id}>{eq.title}</option>
  {/each}
</select>




  {#if currentEq}
    <span id="solvefor-label" class="group-label">What do you want to solve for?</span>
    <div class="var-buttons" role="group" aria-labelledby="solvefor-label">
  {#each activeVariables as v}
    <button
      type="button"
      class:active={solveFor === v.id}
      on:click={() => {
        solveFor = v.id;
        resultMessage = '';
        errorMsg = '';
        useWorkInstead = false;
        inputs = {}; 
      }}
    >
      {@html symbolFor(selectedEqId, v.id)}
    </button>
  {/each}
</div>
{#if solveFor}
  {#if selectedEqId === 'refEfficency'}
    {#if solveFor === 'COP'}
      <label for="var-Qc">Cooling Load <span class="small">(Q<sub>c</sub>, kW)</span></label>
      <input id="var-Qc" type="text" bind:value={inputs.Qc} placeholder="e.g., 500" />

      <div class="label-row">
        <label for="var-Qh">
          {#if useWorkInstead}
            Net Work <span class="small">(W<sub>net</sub>, kW)</span>
          {:else}
            Heat Rejected <span class="small">(Q<sub>h</sub>, kW)</span>
          {/if}
        </label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = !useWorkInstead; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          {@html useWorkInstead ? 'Use Q<sub>h</sub>' : 'Use W<sub>net</sub>'}
        </button>
      </div>
      <input id="var-Qh" type="text" bind:value={inputs[useWorkInstead ? 'Wnet' : 'Qh']} placeholder={useWorkInstead ? 'e.g., 150' : 'e.g., 800'} />

    {:else if solveFor === 'Qc'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 2.5" />

      <div class="label-row">
        <label for="var-Qh">
          {#if useWorkInstead}
            Net Work <span class="small">(W<sub>net</sub>, kW)</span>
          {:else}
            Heat Rejected <span class="small">(Q<sub>h</sub>, kW)</span>
          {/if}
        </label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = !useWorkInstead; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          {@html useWorkInstead ? 'Use Q<sub>h</sub>' : 'Use W<sub>net</sub>'}
        </button>
      </div>
      <input id="var-Qh" type="text" bind:value={inputs[useWorkInstead ? 'Wnet' : 'Qh']} placeholder={useWorkInstead ? 'e.g., 150' : 'e.g., 800'} />

    {:else if solveFor === 'Qh'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 2.5" />
      <label for="var-Qc">Cooling Load <span class="small">(Q<sub>c</sub>, kW)</span></label>
      <input id="var-Qc" type="text" bind:value={inputs.Qc} placeholder="e.g., 500" />

    {:else if solveFor === 'Wnet'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 2.5" />
      <label for="var-Qc">Cooling Load <span class="small">(Q<sub>c</sub>, kW)</span></label>
      <input id="var-Qc" type="text" bind:value={inputs.Qc} placeholder="e.g., 500" />
    {/if}

  {:else if selectedEqId === 'heatPumpEfficiency'}
    {#if solveFor === 'COP'}
      <label for="var-Qh">Heat Delivered <span class="small">(Q<sub>h</sub>, kW)</span></label>
      <input id="var-Qh" type="text" bind:value={inputs.Qh} placeholder="e.g., 800" />

      <div class="label-row">
        <label for="var-Qc">
          {#if useWorkInstead}
            Net Work <span class="small">(W<sub>net</sub>, kW)</span>
          {:else}
            Cooling Load <span class="small">(Q<sub>c</sub>, kW)</span>
          {/if}
        </label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = !useWorkInstead; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          {@html useWorkInstead ? 'Use Q<sub>c</sub>' : 'Use W<sub>net</sub>'}
        </button>
      </div>
      <input id="var-Qc" type="text" bind:value={inputs[useWorkInstead ? 'Wnet' : 'Qc']} placeholder={useWorkInstead ? 'e.g., 500' : 'e.g., 300'} />

    {:else if solveFor === 'Qc'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP<sub>HP</sub>)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 4.0" />
      <label for="var-Qh">Heat Delivered <span class="small">(Q<sub>h</sub>, kW)</span></label>
      <input id="var-Qh" type="text" bind:value={inputs.Qh} placeholder="e.g., 800" />

    {:else if solveFor === 'Qh'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP<sub>HP</sub>)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 4.0" />

      <div class="label-row">
        <label for="var-Qc">
          {#if useWorkInstead}
            Net Work <span class="small">(W<sub>net</sub>, kW)</span>
          {:else}
            Cooling Load <span class="small">(Q<sub>c</sub>, kW)</span>
          {/if}
        </label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = !useWorkInstead; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          {@html useWorkInstead ? 'Use Q<sub>c</sub>' : 'Use W<sub>net</sub>'}
        </button>
      </div>
      <input id="var-Qc" type="text" bind:value={inputs[useWorkInstead ? 'Wnet' : 'Qc']} placeholder={useWorkInstead ? 'e.g., 500' : 'e.g., 300'} />

    {:else if solveFor === 'Wnet'}
      <label for="var-COP">Coefficient of Performance <span class="small">(COP<sub>HP</sub>)</span></label>
      <input id="var-COP" type="text" bind:value={inputs.COP} placeholder="e.g., 4.0" />
      <label for="var-Qh">Heat Delivered <span class="small">(Q<sub>h</sub>, kW)</span></label>
      <input id="var-Qh" type="text" bind:value={inputs.Qh} placeholder="e.g., 800" />
    {/if}




 {:else if selectedEqId === 'idealGasLaw'}
  {#if solveFor === 'n'}
    <label for="var-P">Pressure <span class="small">(P, Pa)</span></label>
    <input id="var-P" type="text" bind:value={inputs.P} placeholder="e.g., 101325" />

    <label for="var-V">Volume <span class="small">(V, m³)</span></label>
    <input id="var-V" type="text" bind:value={inputs.V} placeholder="e.g., 0.1" />

    <label for="var-T">Temperature <span class="small">(T, K)</span></label>
    <input id="var-T" type="text" bind:value={inputs.T} placeholder="e.g., 300" />


  {:else if solveFor === 'm'}
    <label for="var-P">Pressure <span class="small">(P, Pa)</span></label>
    <input id="var-P" type="text" bind:value={inputs.P} placeholder="e.g., 101325" />

    <label for="var-V">Volume <span class="small">(V, m³)</span></label>
    <input id="var-V" type="text" bind:value={inputs.V} placeholder="e.g., 0.1" />

    <label for="var-T">Temperature <span class="small">(T, K)</span></label>
    <input id="var-T" type="text" bind:value={inputs.T} placeholder="e.g., 300" />

    <label for="var-M">Molar Mass <span class="small">(M, kg/mol)</span></label>
    <input id="var-M" type="text" bind:value={inputs.M} placeholder="e.g., 0.029" />

  {:else if solveFor === 'M'}
    <label for="var-P">Pressure <span class="small">(P, Pa)</span></label>
    <input id="var-P" type="text" bind:value={inputs.P} placeholder="e.g., 101325" />

    <label for="var-V">Volume <span class="small">(V, m³)</span></label>
    <input id="var-V" type="text" bind:value={inputs.V} placeholder="e.g., 0.1" />

    <label for="var-T">Temperature <span class="small">(T, K)</span></label>
    <input id="var-T" type="text" bind:value={inputs.T} placeholder="e.g., 300" />

    <label for="var-m">Mass <span class="small">(m, kg)</span></label>
    <input id="var-m" type="text" bind:value={inputs.m} placeholder="e.g., 0.058" />


  {:else}
    {#if !useWorkInstead}
      <div class="label-row">
        <label for="var-n">Moles <span class="small">(n, mol)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = true; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Mass
        </button>
      </div>
      <input id="var-n" type="text" bind:value={inputs.n} placeholder="e.g., 2" />
    {:else}
      <div class="label-row">
        <label for="var-m">Mass <span class="small">(m, kg)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = false; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Moles
        </button>
      </div>
      <input id="var-m" type="text" bind:value={inputs.m} placeholder="e.g., 0.058" />

      <label for="var-M">Molar Mass <span class="small">(M, kg/mol)</span></label>
      <input id="var-M" type="text" bind:value={inputs.M} placeholder="e.g., 0.029" />
    {/if}

    {#if solveFor !== 'P'}
      <label for="var-P">Pressure <span class="small">(P, Pa)</span></label>
      <input id="var-P" type="text" bind:value={inputs.P} placeholder="e.g., 101325" />
    {/if}

    {#if solveFor !== 'V'}
      <label for="var-V">Volume <span class="small">(V, m³)</span></label>
      <input id="var-V" type="text" bind:value={inputs.V} placeholder="e.g., 0.1" />
    {/if}

    {#if solveFor !== 'T'}
      <label for="var-T">Temperature <span class="small">(T, K)</span></label>
      <input id="var-T" type="text" bind:value={inputs.T} placeholder="e.g., 300" />
    {/if}
  {/if}

  {:else if selectedEqId === 'isentropicRelations'}
  {#if solveFor === 'T1' || solveFor === 'T2'}
    {#if !useWorkInstead}
      <div class="label-row">
        <label for="var-P1">Initial Pressure <span class="small">(P₁, Pa)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = true; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Volume Instead
        </button>
      </div>
      <input id="var-P1" type="text" bind:value={inputs.P1} placeholder="e.g., 101325" />

      <label for="var-P2">Final Pressure <span class="small">(P₂, Pa)</span></label>
      <input id="var-P2" type="text" bind:value={inputs.P2} placeholder="e.g., 202650" />

    {:else}
      <div class="label-row">
        <label for="var-V1">Initial Volume <span class="small">(V₁, m³)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = false; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Pressure Instead
        </button>
      </div>
      <input id="var-V1" type="text" bind:value={inputs.V1} placeholder="e.g., 0.1" />

      <label for="var-V2">Final Volume <span class="small">(V₂, m³)</span></label>
      <input id="var-V2" type="text" bind:value={inputs.V2} placeholder="e.g., 0.05" />
    {/if}

    {#if solveFor !== 'T1'}
      <label for="var-T1">Initial Temperature <span class="small">(T₁, K)</span></label>
      <input id="var-T1" type="text" bind:value={inputs.T1} placeholder="e.g., 300" />
    {:else}
      <label for="var-T2">Final Temperature <span class="small">(T₂, K)</span></label>
      <input id="var-T2" type="text" bind:value={inputs.T2} placeholder="e.g., 300" />
    {/if}

    <label for="var-gamma">Heat Capacity Ratio <span class="small">(γ)</span></label>
    <input id="var-gamma" type="text" bind:value={inputs.gamma} placeholder="e.g., 1.4" />



  {:else if solveFor === 'P1' || solveFor === 'P2'}
    {#if !useWorkInstead}
      <div class="label-row">
        <label for="var-T1">Initial Temperature <span class="small">(T₁, K)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = true; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Volume Instead
        </button>
      </div>
      <input id="var-T1" type="text" bind:value={inputs.T1} placeholder="e.g., 300" />

      <label for="var-T2">Final Temperature <span class="small">(T₂, K)</span></label>
      <input id="var-T2" type="text" bind:value={inputs.T2} placeholder="e.g., 600" />

    {:else}
      <div class="label-row">
        <label for="var-V1">Initial Volume <span class="small">(V₁, m³)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = false; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Temperature Instead
        </button>
      </div>
      <input id="var-V1" type="text" bind:value={inputs.V1} placeholder="e.g., 0.1" />

      <label for="var-V2">Final Volume <span class="small">(V₂, m³)</span></label>
      <input id="var-V2" type="text" bind:value={inputs.V2} placeholder="e.g., 0.05" />
    {/if}

    {#if solveFor !== 'P1'}
      <label for="var-P1">Initial Pressure <span class="small">(P₁, Pa)</span></label>
      <input id="var-P1" type="text" bind:value={inputs.P1} placeholder="e.g., 101325" />
    {:else}
      <label for="var-P2">Final Pressure <span class="small">(P₂, Pa)</span></label>
      <input id="var-P2" type="text" bind:value={inputs.P2} placeholder="e.g., 202650" />
    {/if}

    <label for="var-gamma">Heat Capacity Ratio <span class="small">(γ)</span></label>
    <input id="var-gamma" type="text" bind:value={inputs.gamma} placeholder="e.g., 1.4" />

  {:else if solveFor === 'V1' || solveFor === 'V2'}
    {#if !useWorkInstead}
      <div class="label-row">
        <label for="var-P1">Initial Pressure <span class="small">(P₁, Pa)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = true; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Temperature Instead
        </button>
      </div>
      <input id="var-P1" type="text" bind:value={inputs.P1} placeholder="e.g., 101325" />

      <label for="var-P2">Final Pressure <span class="small">(P₂, Pa)</span></label>
      <input id="var-P2" type="text" bind:value={inputs.P2} placeholder="e.g., 202650" />

    {:else}
      <div class="label-row">
        <label for="var-T1">Initial Temperature <span class="small">(T₁, K)</span></label>
        <button
          type="button"
          class="swap-btn"
          on:click={() => { useWorkInstead = false; inputs = {}; resultMessage = ''; errorMsg = ''; }}
        >
          Use Pressure Instead
        </button>
      </div>
      <input id="var-T1" type="text" bind:value={inputs.T1} placeholder="e.g., 300" />

      <label for="var-T2">Final Temperature <span class="small">(T₂, K)</span></label>
      <input id="var-T2" type="text" bind:value={inputs.T2} placeholder="e.g., 600" />
    {/if}

    {#if solveFor !== 'V1'}
      <label for="var-V1">Initial Volume <span class="small">(V₁, m³)</span></label>
      <input id="var-V1" type="text" bind:value={inputs.V1} placeholder="e.g., 0.1" />
    {:else}
      <label for="var-V2">Final Volume <span class="small">(V₂, m³)</span></label>
      <input id="var-V2" type="text" bind:value={inputs.V2} placeholder="e.g., 0.05" />
    {/if}

    <label for="var-gamma">Heat Capacity Ratio <span class="small">(γ)</span></label>
    <input id="var-gamma" type="text" bind:value={inputs.gamma} placeholder="e.g., 1.4" />

  {:else if solveFor === 'gamma'}
  {#if gammaMode === 'TP'}
    <!-- T–P relation -->
    <div class="label-row">
      <label for="var-T1">Initial Temperature <span class="small">(T₁, K)</span></label>
      <button
        type="button"
        class="swap-btn"
        on:click={() => { 
          gammaMode = "PV"; 
          inputs = {}; resultMessage = ''; errorMsg = ''; 
        }}
      >
        Use Pressure/Volume Instead
      </button>
    </div>
    <input id="var-T1" type="text" bind:value={inputs.T1} placeholder="e.g., 300" />

    <label for="var-T2">Final Temperature <span class="small">(T₂, K)</span></label>
    <input id="var-T2" type="text" bind:value={inputs.T2} placeholder="e.g., 600" />

    <label for="var-P1">Initial Pressure <span class="small">(P₁, Pa)</span></label>
    <input id="var-P1" type="text" bind:value={inputs.P1} placeholder="e.g., 101325" />

    <label for="var-P2">Final Pressure <span class="small">(P₂, Pa)</span></label>
    <input id="var-P2" type="text" bind:value={inputs.P2} placeholder="e.g., 202650" />

  {:else if gammaMode === 'PV'}
    <div class="label-row">
      <label for="var-P1">Initial Pressure <span class="small">(P₁, Pa)</span></label>
      <button
        type="button"
        class="swap-btn"
        on:click={() => { 
          gammaMode = "TV"; 
          inputs = {}; resultMessage = ''; errorMsg = ''; 
        }}
      >
        Use Temperature/Volume Instead
      </button>
    </div>
    <input id="var-P1" type="text" bind:value={inputs.P1} placeholder="e.g., 101325" />

    <label for="var-P2">Final Pressure <span class="small">(P₂, Pa)</span></label>
    <input id="var-P2" type="text" bind:value={inputs.P2} placeholder="e.g., 202650" />

    <label for="var-V1">Initial Volume <span class="small">(V₁, m³)</span></label>
    <input id="var-V1" type="text" bind:value={inputs.V1} placeholder="e.g., 0.1" />

    <label for="var-V2">Final Volume <span class="small">(V₂, m³)</span></label>
    <input id="var-V2" type="text" bind:value={inputs.V2} placeholder="e.g., 0.05" />

  {:else if gammaMode === 'TV'}
    <div class="label-row">
      <label for="var-T1">Initial Temperature <span class="small">(T₁, K)</span></label>
      <button
        type="button"
        class="swap-btn"
        on:click={() => { 
          gammaMode = "TP"; 
          inputs = {}; resultMessage = ''; errorMsg = ''; 
        }}
      >
        Use Temperature/Pressure Instead
      </button>
    </div>
    <input id="var-T1" type="text" bind:value={inputs.T1} placeholder="e.g., 300" />

    <label for="var-T2">Final Temperature <span class="small">(T₂, K)</span></label>
    <input id="var-T2" type="text" bind:value={inputs.T2} placeholder="e.g., 600" />

    <label for="var-V1">Initial Volume <span class="small">(V₁, m³)</span></label>
    <input id="var-V1" type="text" bind:value={inputs.V1} placeholder="e.g., 0.1" />

    <label for="var-V2">Final Volume <span class="small">(V₂, m³)</span></label>
    <input id="var-V2" type="text" bind:value={inputs.V2} placeholder="e.g., 0.05" />
  {/if}
{/if}




  {:else}
    {#each activeVariables as v}
      {#if v.id !== solveFor}
        <label for={"var-" + v.id}>
          {v.label}
          <span class="small">
            ({@html symbolFor(selectedEqId, v.id)}{unitFor(selectedEqId, v.id) ? `, ${unitFor(selectedEqId, v.id)}` : ''})
          </span>
        </label>
        <input id={"var-" + v.id} type="text" bind:value={inputs[v.id]} placeholder={v.placeholder} />
      {/if}
    {/each}
  {/if}

  {#if selectedEqId}
    <button class="calculate-btn" on:click={calculate}>Calculate</button>
  {/if}
{/if}



    {#if errorMsg}
  <p class="error-bar">{errorMsg}</p>
{/if}

{#if resultMessage !== "" && !errorMsg}
  <div class="result-info">
    {#if typeof resultMessage === 'object' && resultMessage !== null && !Array.isArray(resultMessage)}
      <table>
        <thead>
          <tr>
            {#each Object.entries(resultMessage) as [key, _]}
              <th>
                {@html labelFor(selectedEqId, key)}
                <span class="small">({@html symbolFor(selectedEqId, key)})</span>
              </th>
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
    {:else if typeof resultMessage === 'number'}
      <table>
        <thead>
          <tr>
            <th>
              {@html labelFor(selectedEqId, solveFor)}
              <span class="small">({@html symbolFor(selectedEqId, solveFor)})</span>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{formatNumber(resultMessage)} {unitFor(selectedEqId, solveFor)}</td>
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
    font-size: 1.05rem;
    margin-top: 42px;
    color: #222;
    font-weight: 700;
  }
  .small { font-size: .85em; color: #555; }

  select, input {
    width: 100%; padding: 10px; font-size: 1rem;
    border-radius: 6px; border: 1px solid #ccc;
    background: #f2f2f2; color: #333; margin-top: 6px;
    margin-bottom: 16px
  }

  .group-label { display: block; font-size: 1rem; margin-top: 28px; margin-bottom: 6px; color: #222; font-weight: 700; }


  .var-buttons { display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap; }


  .var-buttons button {
    background: #f2f2f2; color: #333; border: 1px solid #ccc;
    border-radius: 8px; padding: 8px 12px; cursor: pointer;
    transition: transform .05s ease, background .2s;
  }


  .var-buttons button.active, .var-buttons button:focus-visible {
    outline: 2px solid #7A0019; outline-offset: 2px; box-shadow: 0 0 0 2px #fff;
  }

  .var-buttons button:active { transform: translateY(1px); }


  .calculate-btn {
    background: #7A0019; color: #fff; border: none; padding: 10px 20px;
    font-weight: bold; font-size: 1rem; border-radius: 6px;
    cursor: pointer; transition: background .2s ease; margin-top: 35px;
  }


  .calculate-btn:hover { background: #9c0033; }

  .error-bar {
    color: #fff; background-color: #b00020; padding: 10px;
    border-radius: 6px; max-width: 600px; margin: 14px auto 0; text-align: center;
  }

  .result-info { margin-top: 18px; }

  table { width: 100%; margin-top: 14px; border-collapse: collapse; }

  th, td { border: 1px solid #ddd; padding: 10px; font-size: 0.95rem; text-align: center; }

  th { background-color: #f5f5f5; font-weight: bold; color: #333;}

  .swap-btn {
    background: #eee; color: #333; border: 1px solid #ccc;
    padding: 6px 10px; border-radius: 6px; cursor: pointer;
    font-size: 0.85rem; white-space: nowrap;
  }

  .swap-btn:hover { background: #ddd; }

  .label-row {
  display: flex;
  justify-content: space-between;
  align-items: center;     
  margin-top: 33px;

}

.label-row label {
  margin: 0;
  margin-bottom: -9px
}

</style>
