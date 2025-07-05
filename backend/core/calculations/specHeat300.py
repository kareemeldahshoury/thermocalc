from typing import Dict

idealGas300K_data = {
    "air": ["—", 0.2870, 1.005, 0.718, 1.400],
    "argon": ["Ar", 0.2081, 0.5203, 0.3122, 1.667],
    "butane": ["C₄H₁₀", 0.1433, 1.7164, 1.5734, 1.091],
    "carbon_dioxide": ["CO₂", 0.1889, 0.846, 0.657, 1.289],
    "carbon_monoxide": ["CO", 0.2968, 1.040, 0.744, 1.400],
    "ethane": ["C₂H₆", 0.2765, 1.7662, 1.4897, 1.186],
    "ethylene": ["C₂H₄", 0.2964, 1.5482, 1.2518, 1.237],
    "helium": ["He", 2.0769, 5.1926, 3.1157, 1.667],
    "hydrogen": ["H₂", 4.1240, 14.307, 10.183, 1.405],
    "methane": ["CH₄", 0.5182, 2.2537, 1.7354, 1.299],
    "neon": ["Ne", 0.4119, 1.0299, 0.6179, 1.667],
    "nitrogen": ["N₂", 0.2968, 1.0390, 0.7430, 1.400],
    "octane": ["C₈H₁₈", 0.0729, 1.7113, 1.6385, 1.044],
    "oxygen": ["O₂", 0.2598, 0.918, 0.658, 1.395],
    "propane": ["C₃H₈", 0.1885, 1.7994, 1.4990, 1.126],
    "steam": ["H₂O", 0.4615, 1.8723, 1.4108, 1.327],
}

def idealGas300KCalculation(substance: str) -> Dict[str, str | float]:
    if substance not in idealGas300K_data:
        raise ValueError(f"Substance '{substance}' not found in 300K gas table.")
    
    formula, R, cp, cv, k = idealGas300K_data[substance]
    return {
        "Substance": substance.replace("_", " ").title(),
        "Formula": formula,
        "Gas Constant R (kJ/kg·K)": R,
        "Specific Heat cₚ (kJ/kg·K)": cp,
        "Specific Heat cᵥ (kJ/kg·K)": cv,
        "Ratio of Specific Heats (k)": k
    }
