<script lang="ts">
  let selectedCategory = '';
  let selectedUnit = '';
  let targetUnit = '';
  let inputValue = '';
  let conversionResult = '';

  let unitOptions: string[] = [];

  const unitGroups: Record<string, string[]> = {
    Mass: [
      "Kilograms (kg)", 
      "Pounds (lbs)",
      "Slugs (slug)",
      "Grams per Cubic Centimeter (g/cm³)",
      "Pounds per Cubic Foot (lb/ft³)",
      "Kilograms per Cubic Meter (kg/m³)",
    ],
    Length: [
      "Centimeters (cm)",
      "Meters (m)",
      "Inches (in.)",
      "Feet (ft)",
    ],
    Velocity: [
      "Kilometers per Hour (km/h)",
      "Miles per Hour (mile/h)"
    ],
    Volume: [
      "Cubic Centimeters (cm³)",
      "Cubic Meters (m³)",
      "Cubic Inches (in.³)",
      "Cubic Feet (ft³)",
      "Liters (L)",
      "Gallons (gal)",
    ],
    Force: [
      "Newtons (N)",
      "Pound-Force (lbf)",
      "Poundal (lb·ft/s²)"
    ],
    Pressure: [
      "Pascals (Pa)",
      "Bar ",
      "Atmosphere (atm)",
      "Pounds per Square Inch (psi)",
      "Pounds per Square Feet (lbf/ft²)"
    ],
    "Energy": [
      "Joules (J)",
      "Kilojoules (kJ)",
      "British Thermal Unit (BTU)",
      "Foot-Pound Force (ft·lbf)",
      "Kilocalorie (kcal)",
    ],
    "Energy Transfer Rate": [
      "Watts (W)",
      "KiloWatts (kW)",
      "British Thermal Unit per Hour (BTU/hr)",
      "Horsepower (hp)",
      "Foot-Pound Force per Second (ft·lbf/s)"
    ],
    "Specific Heat": [
      "Kilojoules per Kilogram-Kelvin (kJ/kg·K)",
      "Kilocalories per Kilogram-Kelvin (kcal/kg·K)",
      "British Thermal Unit per Pound-Degree Rankine (Btu/lb·°R)"
    ]
  };

  function updateUnitOptions(event: Event) {
    const target = event.target as HTMLSelectElement;
    selectedCategory = target.value;
    unitOptions = unitGroups[selectedCategory] || [];
    selectedUnit = '';
    targetUnit = '';
    conversionResult = '';
  }

  $: targetOptions = unitOptions.filter(u => u !== selectedUnit);

async function calculateConversion() {
  try {
    const payload = {
      inputValue: parseFloat(inputValue),
      fromUnit: selectedUnit,
      toUnit: targetUnit
    };

    const response = await fetch("http://localhost:8000/api/calculate/unitConversion", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Server error: ${response.status} - ${errText}`);
    }

    const data = await response.json();

    if (typeof data.result === 'string' && data.result.startsWith("Error")) {
      conversionResult = data.result;
    } else {
      conversionResult = `${inputValue} ${selectedUnit} = ${data.result} ${targetUnit}`;
    }

  } catch (error) {
    conversionResult = `Conversion failed: ${(error as Error).message}`;
  }
}

</script>

<div class="conversion-table">
  <h2>Conversion Calculator</h2>

  <label for="unitType">Choose a category:</label>
  <select id="unitType" on:change={updateUnitOptions}>
    <option value="">--Select Category--</option>
    {#each Object.keys(unitGroups) as key}
      <option value={key}>{key}</option>
    {/each}
  </select>

  {#if unitOptions.length}
    <label for="unitOption">Choose from unit:</label>
    <select id="unitOption" bind:value={selectedUnit}>
      <option value="">--Select Unit--</option>
      {#each unitOptions as unit}
        <option value={unit}>{unit}</option>
      {/each}
    </select>
  {/if}

  {#if selectedUnit}
    <label for="targetOption">Convert to:</label>
    <select id="targetOption" bind:value={targetUnit}>
      <option value="">--Select Target Unit--</option>
      {#each targetOptions as unit}
        <option value={unit}>{unit}</option>
      {/each}
    </select>

    <label for="valueInput">Enter value:</label>
    <input
      type="number"
      id="valueInput"
      placeholder="Enter a value..."
      bind:value={inputValue}
    />

    {#if targetUnit && inputValue}
      <button
        class="calc-btn"
        on:click={calculateConversion}
      >
        Calculate
      </button>
    {/if}
  {/if}

  {#if conversionResult}
    <div class="result-popup">
      <strong></strong> {conversionResult}
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

  .conversion-table {
    max-width: 800px;
    margin: 40px auto;
    padding: 30px;
    background-color: white;
    color: black;
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
    background-color: #f2f2f2;
    color: black;
    box-sizing: border-box;
  }

  h2 {
    font-size: 1.4rem;      /* Increase size (adjust as needed) */
    font-weight: bold;    /* Ensure it's bold */
    color: #7A0019;       /* Optional: keep your maroon color */
    margin-bottom: 20px;
  }

  .calc-btn {
    background-color: #7A0019;
    color: white;
    border: none;
    padding: 12px 20px;
    font-size: 1rem;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  .calc-btn:hover {
    background-color: #9c0033;
  }

.result-popup {
  margin-top: 20px;
  background-color: #f7f7f7;
  color: #000;
  padding: 14px 20px;
  border-radius: 8px;
  font-size: clamp(0.75rem, 1.8vw, 1rem); /* Slightly smaller */
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: 500;
  white-space: nowrap;     /* Keep on one line */
  overflow-x: auto;        /* Allow scrolling if needed */
  max-width: 100%;         /* Prevents overflow beyond container */
}


</style>
