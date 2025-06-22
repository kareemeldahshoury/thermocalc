<script lang="ts">
  type FluidType = 'satWaterP' | 'satWaterT' | 'superheatedH20' | 'compLiqWat' | 'satIceWat' | 'satR134T' | 'satR134P' | 'superheatedR134' | 'idealAir' | 'idealN2' | 'idealO2'
  | 'idealCO2' | 'idealCO' | 'idealH2' | 'idealH2O' | 'idealO' | 'molGCP' | 'specHeat300' | 'specHeat';

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



  const fluidInputs: Record<FluidType, Array<{id: string, label: string}>> = {

    molGCP: [],

    specHeat300: [],

    specHeat: [
      { id: 'temperature', label: 'Temperature'}
    ],

    satWaterP: [
      { id: 'quality', label: 'Quality' },
      { id: 'pressure', label: 'Pressure' }
    ],
    satWaterT: [
      { id: 'quality', label: 'Quality' },
      { id: 'temperature', label: 'Temperature' }
    ],
    superheatedH20: [
      { id: 'temperature', label: 'Temperature' },
      { id: 'pressure', label: 'Pressure' }
    ],
    compLiqWat: [
      { id: 'temperature', label: 'Temperature' },
      { id: 'pressure', label: 'Pressure' }
    ],
    satIceWat: [
      { id: 'quality', label: 'Quality' },
      { id: 'temperature', label: 'Temperature' }
  ],
  satR134T: [
      { id: 'quality', label: 'Quality' },
      { id: 'temperature', label: 'Temperature' }
    ],
    satR134P: [
      { id: 'quality', label: 'Quality' },
      { id: 'pressure', label: 'Pressure' }
    ],
    superheatedR134: [
      { id: 'temperature', label: 'Temperature' },
      { id: 'pressure', label: 'Pressure' }
    ],
    idealAir: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealN2: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealO2: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealCO2: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealCO: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealH2: [
      { id: 'temperature', label: 'Temperature' },
  ],
    idealH2O: [
      { id: 'temperature', label: 'Temperature' },
  ],
  idealO: [
      { id: 'temperature', label: 'Temperature' },
  ],


  };
</script>

<label for="fluidDropdown">Calculate for:</label>
<select id="fluidDropdown" bind:value={selectedFluid}>
  <option value="">-- Select --</option>
  <option value="molGCP">Molar-Specific Gas Properties</option>
  <option value="specHeat300">Ideal Gas Specific Heat @ 300 K</option>
  <option value="specHeat">Ideal Gas Specific Heat (Temperature)</option>
  <option value="satWaterP">Saturated Water (Pressure)</option>
  <option value="satWaterT">Saturated Water (Temperature)</option>
  <option value="superheatedH20">Superheated Water</option>
  <option value="compLiqWat">Compressed Liq. Water</option>
  <option value="satIceWat">Saturated Ice-Water Vapor</option>
  <option value="satR134T">Saturated Refrigerant-134a (Temperature)</option>
  <option value="satR134P">Saturated Refrigerant-134a (Pressure)</option>
  <option value="superheatedR134">Superheated Refrigerant-134a</option>
  <option value="idealAir">Ideal-Gas Properties of Air</option>
  <option value="idealN2">Ideal-Gas Properties of Nitrogen (N₂)</option>
  <option value="idealO2">Ideal-Gas Properties of Oxygen (O₂)</option>
  <option value="idealCO2">Ideal-Gas Properties of Carbon Dioxide (CO₂)</option>
  <option value="idealCO">Ideal-Gas Properties of Carbon Monoxide (CO)</option>
  <option value="idealH2">Ideal-Gas Properties of Hydrogen (H₂)</option>
  <option value="idealH2O">Ideal-Gas Properties of Water Vapor (H₂O)</option>
  <option value="idealO">Ideal-Gas Properties of Monatomic Oxygen (O)</option>
</select>

{#if selectedFluid === 'molGCP'}
  <div style="margin-top: 10px;">
    <label for="substanceDropdown">Select Gas:</label>
    <select id="substanceDropdown" bind:value={selectedSubstance}>
      <option value="">-- Choose Gas --</option>
      {#each molGCPSubstances as substance}
        <option value={substance.id}>{substance.name}</option>
      {/each}
    </select>
  </div>
{:else if selectedFluid === 'specHeat300'}
  <div style="margin-top: 10px;">
    <label for="substanceDropdown">Select Gas:</label>
    <select id="substanceDropdown" bind:value={selectedSubstance}>
      <option value="">-- Choose Gas --</option>
      {#each specHeat300Substances as substance}
        <option value={substance.id}>{substance.name}</option>
      {/each}
    </select>
  </div>
  {:else if selectedFluid === 'specHeat'}
  <div style="margin-top: 10px; display: flex; flex-direction: column; gap: 10px;">
    <!-- Gas selection dropdown -->
    <div>
      <label for="specHeatGas">Select Gas:</label>
      <select id="specHeatGas" bind:value={selectedSubstance}>
        <option value="">-- Choose Gas --</option>
        {#each specHeat as gas}
          <option value={gas.id}>{gas.name}</option>
        {/each}
      </select>
    </div>
    <div>
      <label for="specHeatTemp">Temperature (K):</label>
      <input 
        id="specHeatTemp" 
        type="number" 
        min="250" 
        max="1000" 
        placeholder="250-1000 K"
      />
    </div>
  </div>
{:else if selectedFluid && fluidInputs[selectedFluid]}
  <!-- This shows inputs for other fluid types -->
  <div style="margin-top: 10px;">
    {#each fluidInputs[selectedFluid] as input}
      <label for={input.id}>{input.label}:</label>
      <input id={input.id} type="text" />
    {/each}
  </div>
{/if}