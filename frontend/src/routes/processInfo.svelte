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
        "Work: W = P ( V₂ − V₁ )",
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
        'Work: W = nRT · ln( <span class="frac"><span class="num">V₂</span><span class="den">V₁</span></span> )',
        "Q = W"
      ]
    },
    {
      title: "Adiabatic (No Heat Transfer)",
      properties: [
        "Q = 0",
        "Entropy may change (irreversible) or stay constant (reversible)",
        'Work: W = <span class="frac"><span class="num">P₂V₂ − P₁V₁</span><span class="den">1 − γ</span></span> = <span class="frac"><span class="num">nR(T₁ − T₂)</span><span class="den">γ − 1</span></span>',
        "For ideal gases: PV^γ = constant"
      ]
    },
    {
      title: "Isentropic (Adiabatic + Reversible)",
      properties: [
        "Q = 0, ΔS = 0",
        'Work: W = <span class="frac"><span class="num">P₂V₂ − P₁V₁</span><span class="den">1 − γ</span></span>',
        'Also: W = <span class="frac"><span class="num">mR (T₁ − T₂)</span><span class="den">γ − 1</span></span>',
        "PV<sup>γ</sup> = constant, TV<sup>γ−1</sup> = constant"
      ]
    },
    {
      title: "Polytropic",
      properties: [
        "PVⁿ = constant",
        'Work: W = <span class="frac"><span class="num">P₂V₂ − P₁V₁</span><span class="den">1 − n</span></span>',
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

  :global(.frac) {
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    line-height: 1;
    vertical-align: middle;
    font-size: 0.95em;
  }

  :global(.frac .num) {
    display: block;
    padding: 0 .15em;
  }

  :global(.frac .den) {
    display: block;
    border-top: 1px solid currentColor;
    margin-top: .1em;
    padding: .1em .15em 0;
  }

  :global(sup) {
    font-size: 0.75em;
    vertical-align: super;
  }
</style>

<div class="container">
  {#each processes as group}
    <div class="group">
      <h3>{group.title}</h3>
      <ul>
        {#each group.properties as item}
          <li>{@html item}</li>
        {/each}
      </ul>
    </div>
  {/each}
</div>
