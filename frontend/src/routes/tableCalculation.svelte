<script lang="ts">

function formatLabel(label: string): string {
  const [main, parens] = label.split('<br>');
  return `${main}<br><span style="font-size: 0.8em;">${parens}</span>`;
}

function getFluidLabel(id: string): string {
  const option = fluidOptions.find(opt => opt.id === id);
  return option ? option.label : id;
}


function getPlaceholder(inputId: string, fluid: FluidType): string {
  if (inputId === 'quality') return 'Enter value between 0 and 1';

  if (inputId === 'pressure') {
    switch (fluid) {
      case 'pressureSatWater':
        return 'Enter a value from 0.01 to 220.64 bar';
      case 'pressureSatR134':
        return 'Enter a value from 0.06 to 40 bar';
      case 'superheatedH20':
        return 'Enter a value from 1 to 100 bar';
      case 'superheatedR134':
        return 'Enter a value from 0.06 to 40 bar';
      case 'compLiqWat':
        return 'Enter a value from 1 to 300 bar';
      default:
        return 'Enter pressure in bar';
    }
  }

  if (inputId === 'temperature') {
    switch (fluid) {
      case 'temperatureSatWater':
        return 'Enter a value from 0 to 373.95 °C';
      case 'superheatedH20':
        return 'Enter a value from 100 to 800 °C';
      case 'superheatedR134':
        return 'Enter a value from 20 to 160 °C';
      case 'temperatureSatR134':
        return 'Enter a value from -40 to 100 °C';
      case 'compLiqWat':
        return 'Enter a value from 0 to 300 °C';
      case 'idealN2':
        return 'Enter a value from 220 to 3250 K';
      case 'idealO2':
        return 'Enter a value from 220 to 3250 K';
      case 'idealCO2':
        return 'Enter a value from 220 to 3250 K';
      case 'idealCO':
        return 'Enter a value from 220 to 3250 K';
      case 'idealH2':
        return 'Enter a value from 260 to 3250 K';
      case 'idealH2O':
        return 'Enter a value from 220 to 3250 K';
      case 'idealO':
        return 'Enter a value from 298 to 3500 K';
      case 'idealOH':
        return 'Enter a value from 298 to 3500 K';
      default:
        return 'Enter temperature';
    }
  }

  return '';
}

let searchText = '';

type FluidOption = { id: FluidType; label: string };

const fluidOptions: FluidOption[] = [
  { id: 'airData', label: 'Ideal-Gas Properties of Air' },
  { id: 'idealCO', label: 'Ideal-Gas Properties of Carbon Monoxide (CO)' },
  { id: 'idealCO2', label: 'Ideal-Gas Properties of Carbon Dioxide (CO₂)' },
  { id: 'idealH2', label: 'Ideal-Gas Properties of Hydrogen (H₂)' },
  { id: 'idealH2O', label: 'Ideal-Gas Properties of Water Vapor (H₂O)' },
  { id: 'idealN2', label: 'Ideal-Gas Properties of Nitrogen (N₂)' },
  { id: 'idealO', label: 'Ideal-Gas Properties of Monatomic Oxygen (O)' },
  { id: 'idealO2', label: 'Ideal-Gas Properties of Oxygen (O₂)' },
  { id: 'idealOH', label: 'Ideal-Gas Properties of Hydroxyl (OH)' },
  { id: 'specHeat', label: 'Ideal Gas Specific Heat (Temperature)' },
  { id: 'specHeat300', label: 'Ideal Gas Specific Heat @ 300 K' },
  { id: 'molGCP', label: 'Molar-Specific Gas Properties' },
  { id: 'compLiqWat', label: 'Compressed Liq. Water' },
  { id: 'pressureSatR134', label: 'Saturated Refrigerant-134a (Pressure)' },
  { id: 'temperatureSatR134', label: 'Saturated Refrigerant-134a (Temperature)' },
  { id: 'SatIceWat', label: 'Saturated Ice-Water Vapor' },
  { id: 'pressureSatWater', label: 'Saturated Water (Pressure)' },
  { id: 'temperatureSatWater', label: 'Saturated Water (Temperature)' },
  { id: 'superheatedH20', label: 'Superheated Water' },
  { id: 'superheatedR134', label: 'Superheated Refrigerant-134a' }
];



  type FluidType = 'pressureSatWater' | 'temperatureSatWater' | 'superheatedH20' | 'compLiqWat' | 'SatIceWat' | 'temperatureSatR134' | 'pressureSatR134' | 'superheatedR134' | 'airData' | 'idealN2' | 'idealO2'
  | 'idealCO2' | 'idealCO' | 'idealH2' | 'idealH2O' | 'idealO' | 'molGCP' | 'specHeat300' | 'specHeat' | 'idealOH';

  const molGCPSubstances = [
  { id: 'air', name: 'Air' },
  { id: 'ammonia', name: 'Ammonia (NH₃)' },
  { id: 'argon', name: 'Argon (Ar)' },
  { id: 'benzene', name: 'Benzene (C₆H₆)' },
  { id: 'bromine', name: 'Bromine (Br₂)' },
  { id: 'n_butane', name: 'n-Butane (C₄H₁₀)' },
  { id: 'carbon_dioxide', name: 'Carbon dioxide (CO₂)' },
  { id: 'carbon_monoxide', name: 'Carbon monoxide (CO)' },
  { id: 'carbon_tetrachloride', name: 'Carbon tetrachloride (CCl₄)' },
  { id: 'chlorine', name: 'Chlorine (Cl₂)' },
  { id: 'chloroform', name: 'Chloroform (CHCl₃)' },
  { id: 'r12', name: 'Dichlorodifluoromethane (R-12)' },
  { id: 'r21', name: 'Dichlorofluoromethane (R-21)' },
  { id: 'ethane', name: 'Ethane (C₂H₆)' },
  { id: 'ethyl_alcohol', name: 'Ethyl alcohol (C₂H₅OH)' },
  { id: 'ethylene', name: 'Ethylene (C₂H₄)' },
  { id: 'helium', name: 'Helium (He)' },
  { id: 'n_hexane', name: 'n-Hexane (C₆H₁₄)' },
  { id: 'hydrogen', name: 'Hydrogen (H₂)' },
  { id: 'krypton', name: 'Krypton (Kr)' },
  { id: 'methane', name: 'Methane (CH₄)' },
  { id: 'methyl_alcohol', name: 'Methyl alcohol (CH₃OH)' },
  { id: 'methyl_chloride', name: 'Methyl chloride (CH₃Cl)' },
  { id: 'neon', name: 'Neon (Ne)' },
  { id: 'nitrogen', name: 'Nitrogen (N₂)' },
  { id: 'nitrous_oxide', name: 'Nitrous oxide (N₂O)' },
  { id: 'oxygen', name: 'Oxygen (O₂)' },
  { id: 'propane', name: 'Propane (C₃H₈)' },
  { id: 'propylene', name: 'Propylene (C₃H₆)' },
  { id: 'sulfur_dioxide', name: 'Sulfur dioxide (SO₂)' },
  { id: 'r134a', name: 'Tetrafluoroethane (R-134a)' },
  { id: 'r11', name: 'Trichlorofluoromethane (R-11)' },
  { id: 'water', name: 'Water (H₂O)' },
  { id: 'xenon', name: 'Xenon (Xe)' }
];


const specHeat300Substances = [
  { id: 'air', name: 'Air' },
  { id: 'argon', name: 'Argon (Ar)' },
  { id: 'butane', name: 'Butane (C₄H₁₀)' },
  { id: 'carbon_dioxide', name: 'Carbon dioxide (CO₂)' },
  { id: 'carbon_monoxide', name: 'Carbon monoxide (CO)' },
  { id: 'ethane', name: 'Ethane (C₂H₆)' },
  { id: 'ethylene', name: 'Ethylene (C₂H₄)' },
  { id: 'helium', name: 'Helium (He)' },
  { id: 'hydrogen', name: 'Hydrogen (H₂)' },
  { id: 'methane', name: 'Methane (CH₄)' },
  { id: 'neon', name: 'Neon (Ne)' },
  { id: 'nitrogen', name: 'Nitrogen (N₂)' },
  { id: 'octane', name: 'Octane (C₈H₁₈)' },
  { id: 'oxygen', name: 'Oxygen (O₂)' },
  { id: 'propane', name: 'Propane (C₃H₈)' },
  { id: 'steam', name: 'Steam (H₂O)' }
];

const specHeat = [
    { id: 'air', name: 'Air' },
    { id: 'co2', name: 'Carbon dioxide (CO₂)' },
    { id: 'co', name: 'Carbon monoxide (CO)' },
    { id: 'h2', name: 'Hydrogen (H₂)' },
    { id: 'n2', name: 'Nitrogen (N₂)' },
    { id: 'o2', name: 'Oxygen (O₂)' }
  ];

  let selectedFluid: FluidType | '' = '';
  let selectedSubstance = '';
  let previousFluid = '';
$: if (selectedFluid !== previousFluid) {
  inputValues = {};
  resultMessage = '';
  if (!selectedFluid.startsWith('ideal') && selectedFluid !== 'specHeat') {
    selectedSubstance = '';
  }
  previousFluid = selectedFluid;
}

  let inputValues: Record<string, string> = {};

 
  let resultMessage = '';

    $: if (selectedFluid.startsWith('ideal')) {
    selectedSubstance = selectedFluid.replace('ideal', '').toLowerCase();
  }

const fluidInputs: Record<FluidType, Array<{ id: string, label: string }>> = {
  molGCP: [],
  specHeat300: [],
  specHeat: [
    { id: 'temperature', label: 'Temperature <i>(T, K)</i>' }
  ],
  pressureSatWater: [
    { id: 'quality', label: 'Quality <i>(x)</i>' },
    { id: 'pressure', label: 'Pressure <i>(bar)</i>' }
  ],
  temperatureSatWater: [
    { id: 'quality', label: 'Quality <i>(x)</i>' },
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' }
  ],
  superheatedH20: [
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' },
    { id: 'pressure', label: 'Pressure <i>(bar)</i>' }
  ],
  compLiqWat: [
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' },
    { id: 'pressure', label: 'Pressure <i>(bar)</i>' }
  ],
  SatIceWat: [
    { id: 'quality', label: 'Quality <i>(x)</i>' },
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' }
  ],
  temperatureSatR134: [
    { id: 'quality', label: 'Quality <i>(x)</i>' },
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' }
  ],
  pressureSatR134: [
    { id: 'quality', label: 'Quality <i>(x)</i>' },
    { id: 'pressure', label: 'Pressure <i>(bar)</i>' }
  ],
  superheatedR134: [
    { id: 'temperature', label: 'Temperature <i>(°C)</i>' },
    { id: 'pressure', label: 'Pressure <i>(bar)</i>' }
  ],
  airData: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealN2: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealO2: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealCO2: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealCO: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealH2: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealH2O: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealO: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ],
  idealOH: [
    { id: 'temperature', label: 'Temperature <i>(K)</i>' }
  ]
};




 
  async function calculate() {
  const payload = {
    fluidType: selectedFluid,
    substance: selectedSubstance,
    inputs: inputValues
  };

  console.log(payload); 

  try {
let endpoint = '';

if (selectedFluid.includes('Sat')) {
  endpoint = 'http://localhost:8000/api/calculate/satFluid';
} else if (selectedFluid === 'superheatedH20') {
  endpoint = 'http://localhost:8000/api/calculate/superHeatedWater';
} else if (selectedFluid === 'superheatedR134') {
  endpoint = 'http://localhost:8000/api/calculate/superheatedR134';
} else if (selectedFluid === 'airData') {
  endpoint = 'http://localhost:8000/api/calculate/airData';
} else if (selectedFluid === 'molGCP') {
  endpoint = 'http://localhost:8000/api/calculate/molGCP';
} else if (selectedFluid === 'specHeat300') {
  endpoint = 'http://localhost:8000/api/calculate/specHeat300';
} else if (selectedFluid === 'specHeat') {
  endpoint = 'http://localhost:8000/api/calculate/specHeat';
} else if (selectedFluid.startsWith('ideal')) {
  endpoint = 'http://localhost:8000/api/calculate/idealGas';
}

  const payload: any = {
    fluidType: selectedFluid,
    inputs: inputValues
  };

  // ✅ Add substance only when needed
  if (
    selectedFluid.includes('ideal') ||
    selectedFluid === 'molGCP' ||
    selectedFluid === 'specHeat300' ||
    selectedFluid === 'specHeat'
  ) {
    payload.substance = selectedSubstance;
  }


const response = await fetch(endpoint, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(payload)
  });

  

    if (!response.ok) throw new Error('Server error');

    const result = await response.json();
    resultMessage = result.result;

  } catch (error: unknown) {
    if (error instanceof Error) {
      resultMessage = `Error: ${error.message}`;
    } else {
      resultMessage = 'An unknown error occurred';
    }
  }
}

</script>


<div class="container">
<label for="fluidDropdown">Calculate for:</label>
<input
  list="fluidOptions"
  id="fluidDropdown"
  bind:value={searchText}
  placeholder="Type or choose a fluid..."
  on:change={() => {
    const match = fluidOptions.find(f => f.label === searchText);
    if (match) selectedFluid = match.id;
  }}
/>

<datalist id="fluidOptions">
  {#each fluidOptions as fluid}
    <option value={fluid.label}>{fluid.label}</option>
  {/each}
</datalist>


  {#if selectedFluid === 'molGCP'}
    <div>
      <label for="substanceDropdown">Select Gas:</label>
      <select id="substanceDropdown" bind:value={selectedSubstance}>
        <option value="">-- Choose Gas --</option>
        {#each molGCPSubstances as substance}
          <option value={substance.id}>{substance.name}</option>
        {/each}
      </select>
    </div>

  {:else if selectedFluid === 'specHeat300'}
    <div>
      <label for="substanceDropdown">Select Gas:</label>
      <select id="substanceDropdown" bind:value={selectedSubstance}>
        <option value="">-- Choose Gas --</option>
        {#each specHeat300Substances as substance}
          <option value={substance.id}>{substance.name}</option>
        {/each}
      </select>
    </div>

{:else if selectedFluid === 'specHeat'}
  <div>
    <label for="specHeatGas">Select Gas:</label>
    <select id="specHeatGas" bind:value={selectedSubstance}>
      <option value="">-- Choose Gas --</option>
      {#each specHeat as gas}
        <option value={gas.id}>{gas.name}</option>
      {/each}
    </select>

    <label for="temperature">Temperature (K):</label>
    <input
      id="temperature"
      type="number"
      min="250"
      max="1000"
      placeholder="250 - 1000 K"
      bind:value={inputValues.temperature}
    />
  </div>

{:else if selectedFluid && selectedFluid in fluidInputs}
  <div>
    {#each fluidInputs[selectedFluid as FluidType] as input}
      <label for={input.id}>{@html input.label}:</label>
      <input
        id={input.id}
        type="text"
        bind:value={inputValues[input.id]}
        placeholder={getPlaceholder(input.id, selectedFluid as FluidType)}
      />
    {/each}
  </div>

{:else if selectedFluid && fluidInputs[selectedFluid]}
  <div>
    {#each fluidInputs[selectedFluid] as input}
      <label for={input.id}>{@html input.label}:</label>
      <input
        id={input.id}
        type="text"
        bind:value={inputValues[input.id]}
        placeholder={getPlaceholder(input.id, selectedFluid as FluidType)}
      />
    {/each}
  </div>
{/if}


  {#if selectedFluid}
    <button on:click={calculate}>Calculate</button>
  {/if}

{#if resultMessage}
  <div style="margin-top: 20px;">
<strong>
  Result: {getFluidLabel(selectedFluid)}
  {#if inputValues.temperature || inputValues.pressure || inputValues.quality}
    &nbsp;(
    {#if inputValues.temperature}
      T = {inputValues.temperature} {selectedFluid.includes('ideal') ? 'K' : '°C'}{(inputValues.pressure || inputValues.quality) ? ', ' : ''}
    {/if}
    {#if inputValues.pressure}
      P = {inputValues.pressure} bar{inputValues.quality ? ', ' : ''}
    {/if}
    {#if inputValues.quality}
      x = {inputValues.quality}
    {/if}
    )
  {/if}
</strong>




    {#if typeof resultMessage === 'object' && resultMessage !== null}
      <table>
        <thead>
          <tr>
            {#each Object.entries(resultMessage) as [key, _]}
              <th>
                <div style="font-weight: bold;">{@html key.split('<br>')[0]}</div>
                <div style="font-size: 0.8rem; color: #444; line-height: 1.1; white-space: nowrap;">{@html key.split('<br>')[1]}</div>
              </th>

            {/each}
          </tr>
        </thead>
        <tbody>
          <tr>
            {#each Object.entries(resultMessage) as [_, value]}
              <td>
                {typeof value === 'number' ? value.toLocaleString() : value}
              </td>
            {/each}
          </tr>
        </tbody>
      </table>
    {:else}
      <p style="color: white; background-color: #b00020; padding: 10px; border-radius: 6px; max-width: 600px; margin: 0 auto;">
        {resultMessage}
      </p>
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
    margin: 40px auto;
    padding: 20px;
    background-color: white;
    color: #000;
    border-radius: 12px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
  }

  label {
    font-weight: bold;
    display: block;
    margin-top: 20px;
    margin-bottom: 6px;
  }

  select,
  input {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border-radius: 6px;
    border: 1px solid #ccc;
    margin-bottom: 16px;
    color: black;
    background-color: #f0f4ff;
  }

  button {
    background-color: #FFCC33; /* U of M Gold */
    color: #7A0019;
    border: none;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.2s ease;
  }

  button:hover {
    background-color: #e6b800;
  }

  strong {
    font-size: 1.2rem;
    display: block;
    margin-top: 20px;
  }

  table {
    width: 100%;
    margin: 20px auto;
    border-collapse: collapse;
    text-align: center;
  }

th {
  padding: 10px;
  border: 1px solid #ddd;
  text-align: center;
  max-width: 150px;
  white-space: normal;
  word-wrap: break-word;
}

  td {
    border: 1px solid #ddd;
    padding: 12px;
  }

  thead {
    background-color: #f7f7f7;
  }
</style>
