<script lang="ts">
  interface ProcessGroup {
    title: string;
    properties: string[];
  }

  const processes: ProcessGroup[] = [
    {
      title: "Isobaric (Constant Pressure)",
      properties: [
        "Pressure (P) = constant",
        "Heat added goes into changing internal energy and doing boundary work",
        "Work: W = P(V₂ − V₁)",
        "Q ≠ 0, ΔU ≠ 0, W ≠ 0"
      ]
    },
    {
      title: "Isochoric (Constant Volume)",
      properties: [
        "Volume (V) = constant",
        "No boundary work is done",
        "Work: W = 0",
        "Q = ΔU"
      ]
    },
    {
      title: "Isothermal (Constant Temperature)",
      properties: [
        "Temperature (T) = constant",
        "ΔU = 0 for ideal gases",
        "Work: W = nRT ln(V₂ / V₁)",
        "Q = W"
      ]
    },
    {
      title: "Adiabatic (No Heat Transfer)",
      properties: [
        "Q = 0",
        "Entropy may change (irreversible) or stay constant (reversible)",
        "Work: W = (P₂V₂ − P₁V₁) / (1 − γ) = (nR(T₁ − T₂)) / (γ − 1)",
        "For ideal gases: PV^γ = constant"
      ]
    },
    {
      title: "Isentropic (Adiabatic + Reversible)",
      properties: [
        "Q = 0, ΔS = 0",
        "Work: W = (P₂V₂ − P₁V₁)/(1 - γ)",
        "Also: W = (m * R * (T₁ − T₂)) / (γ − 1)",
        "PV^γ = constant, TV^{γ−1} = constant"
      ]
    },
    {
      title: "Polytropic",
      properties: [
        "PVⁿ = constant",
        "Work: W = (P₂V₂ − P₁V₁) / (1 − n)",
        "n ≠ 1: Use polytropic formula",
        "n = 1: Reduces to isothermal"
      ]
    },
    {
      title: "Throttling (Joule-Thomson Expansion)",
      properties: [
        "h₁ = h₂ (Enthalpy is constant)",
        "Q = 0, W = 0",
        "No significant work or heat transfer",
        "Irreversible and adiabatic"
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
    color: #7A0019;
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
  {#each processes as group}
    <div class="group">
      <h3>{group.title}</h3>
      <ul>
        {#each group.properties as item}
          <li>{item}</li>
        {/each}
      </ul>
    </div>
  {/each}
</div>
