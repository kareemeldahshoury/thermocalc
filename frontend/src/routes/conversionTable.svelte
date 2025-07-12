<script lang="ts">
  interface UnitGroup {
    title: string;
    items: string[];
  }

  const units: UnitGroup[] = [
    {
      title: "Mass and Density",
      items: [
        "1 kg = 2.2046 lb",
        "1 g/cm³ = 10³ kg/m³",
        "1 g/cm³ = 62.428 lb/ft³",
        "1 lb = 0.4536 kg",
        "1 lb/ft³ = 0.016018 g/cm³",
        "1 lb/ft³ = 16.018 kg/m³"
      ]
    },
    {
      title: "Length",
      items: [
        "1 cm = 0.3937 in.",
        "1 m = 3.2808 ft",
        "1 in. = 2.54 cm",
        "1 ft = 0.3048 m"
      ]
    },
    {
      title: "Velocity",
      items: [
        "1 km/h = 0.62137 mile/h",
        "1 mile/h = 1.6093 km/h"
      ]
    },
    {
      title: "Volume",
      items: [
        "1 cm³ = 0.061024 in.³",
        "1 m³ = 35.315 ft³",
        "1 L = 10⁻³ m³",
        "1 L = 0.0353 ft³",
        "1 in.³ = 16.387 cm³",
        "1 ft³ = 0.028317 m³",
        "1 gal = 0.13368 ft³",
        "1 gal = 3.7854 × 10⁻³ m³"
      ]
    },
    {
      title: "Force",
      items: [
        "1 N = 1 kg · m/s²",
        "1 N = 0.22481 lbf",
        "1 lbf = 32.174 lb · ft/s²",
        "1 lbf = 4.4482 N"
      ]
    },
    {
      title: "Pressure",
      items: [
        "1 Pa = 1 N/m²",
        "1 Pa = 1.4504 × 10⁻⁴ lbf/in.²",
        "1 bar = 10⁵ N/m²",
        "1 atm = 1.01325 bar",
        "1 atm = 6894.8 Pa",
        "1 lbf/in.² = 144 lbf/ft²",
        "1 atm = 14.696 lbf/in.²"
      ]
    },
    {
      title: "Energy and Specific Energy",
      items: [
        "1 J = 1 N · m = 0.73756 ft · lbf",
        "1 kJ = 737.56 ft · lbf",
        "1 kJ = 0.9478 Btu",
        "1 kJ/kg = 0.42992 Btu/lb",
        "1 ft · lbf = 1.35582 J",
        "1 Btu = 778.17 ft · lbf",
        "1 Btu = 1.0551 kJ",
        "1 Btu/lb = 2.326 kJ/kg",
        "1 kcal = 4.1868 kJ"
      ]
    },
    {
      title: "Energy Transfer Rate",
      items: [
        "1 W = 1 J/s = 3.413 Btu/h",
        "1 kW = 1.341 hp",
        "1 Btu/h = 0.293 W",
        "1 hp = 2545 Btu/h",
        "1 hp = 550 ft · lbf/s",
        "1 hp = 0.7457 kW"
      ]
    },
    {
      title: "Specific Heat",
      items: [
        "1 kJ/kg · K = 0.238846 Btu/lb · °R",
        "1 kcal/kg · K = 1 Btu/lb · °R",
        "1 Btu/lb · °R = 4.1868 kJ/kg · K"
      ]
    },
    {
      title: "Others",
      items: [
        "1 ton of refrigeration = 200 Btu/min = 211 kJ/min",
        "1 volt = 1 watt per ampere"
      ]
    },

    {
  title: "Universal Gas Constant (R̅)",
  items: [
    "R̅ = 8.314 kJ/kmol·K",
    "R̅ = 1545 ft·lbf/lbmol·°R",
    "R̅ = 1.986 Btu/lbmol·°R"
  ]
},
{
  title: "Standard Acceleration of Gravity",
  items: [
    "g = 9.80665 m/s²",
    "g = 32.174 ft/s²"
  ]
},
{
  title: "Standard Atmospheric Pressure",
  items: [
    "1 atm = 1.01325 bar",
    "1 atm = 14.696 lbf/in.²",
    "760 mm Hg = 29.92 in. Hg"
  ]
},
{
  title: "Temperature Relations",
  items: [
    "T(°R) = 1.8 × T(K)",
    "T(°C) = T(K) − 273.15",
    "T(°F) = T(°R) − 459.67"
  ]
}

  ];
</script>

<style>
  .container {
    background-color: #fff;
    color: black;
    padding: 20px;
    max-width: 1200px;
    margin: auto;
    font-family: 'Segoe UI', sans-serif;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
  }

  .group h3 {
    color: #F58220;
    font-size: 1.2rem;
    margin-bottom: 10px;
  }

  ul {
    padding-left: 20px;
    margin: 0;
  }

  li {
    list-style: none;
    padding: 2px 0;
  }
</style>

<div class="container">
  {#each units as group}
    <div class="group">
      <h3>{group.title}</h3>
      <ul>
        {#each group.items as item}
          <li>{item}</li>
        {/each}
      </ul>
    </div>
  {/each}
</div>
