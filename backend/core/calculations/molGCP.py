from typing import Dict

molGCP_data = {
    "air": ["—", 28.97, 0.2870, 132.5, 3.77, 0.0883],
    "ammonia": ["NH₃", 17.03, 0.4882, 405.5, 11.28, 0.0724],
    "argon": ["Ar", 39.948, 0.2081, 151, 4.86, 0.0749],
    "benzene": ["C₆H₆", 78.115, 0.1064, 562, 4.92, 0.2603],
    "bromine": ["Br₂", 159.808, 0.0520, 584, 10.34, 0.1355],
    "n_butane": ["C₄H₁₀", 58.124, 0.1430, 425.2, 3.80, 0.2547],
    "carbon_dioxide": ["CO₂", 44.01, 0.1889, 304.2, 7.39, 0.0943],
    "carbon_monoxide": ["CO", 28.011, 0.2968, 133, 3.50, 0.0930],
    "carbon_tetrachloride": ["CCl₄", 153.82, 0.05405, 556.4, 4.56, 0.2759],
    "chlorine": ["Cl₂", 70.906, 0.1173, 417, 7.71, 0.1242],
    "chloroform": ["CHCl₃", 119.38, 0.06964, 536.6, 5.47, 0.2403],
    "r12": ["CCl₂F₂", 120.91, 0.06876, 384.7, 4.01, 0.2179],
    "r21": ["CHCl₂F", 102.92, 0.08078, 451.7, 5.17, 0.1973],
    "ethane": ["C₂H₆", 30.070, 0.2765, 305.5, 4.48, 0.1480],
    "ethyl_alcohol": ["C₂H₅OH", 46.07, 0.1805, 516, 6.38, 0.1673],
    "ethylene": ["C₂H₄", 28.054, 0.2964, 282.4, 5.12, 0.1242],
    "helium": ["He", 4.003, 2.0769, 5.3, 0.23, 0.0578],
    "n_hexane": ["C₆H₁₄", 86.179, 0.09647, 507.9, 3.03, 0.3677],
    "hydrogen": ["H₂", 2.016, 4.1240, 33.3, 1.30, 0.0649],
    "krypton": ["Kr", 83.80, 0.09921, 209.4, 5.50, 0.0924],
    "methane": ["CH₄", 16.043, 0.5182, 191.1, 4.64, 0.0993],
    "methyl_alcohol": ["CH₃OH", 32.042, 0.2595, 513.2, 7.95, 0.1180],
    "methyl_chloride": ["CH₃Cl", 50.488, 0.1647, 416.3, 6.68, 0.1430],
    "neon": ["Ne", 20.183, 0.4119, 44.5, 2.73, 0.0417],
    "nitrogen": ["N₂", 28.013, 0.2968, 126.2, 3.39, 0.0899],
    "nitrous_oxide": ["N₂O", 44.013, 0.1889, 309.7, 7.27, 0.0961],
    "oxygen": ["O₂", 31.999, 0.2598, 154.8, 5.08, 0.0780],
    "propane": ["C₃H₈", 44.097, 0.1885, 370, 4.26, 0.1998],
    "propylene": ["C₃H₆", 42.081, 0.1976, 365, 4.62, 0.1810],
    "sulfur_dioxide": ["SO₂", 64.063, 0.1298, 430.7, 7.88, 0.1217],
    "r134a": ["CF₃CH₂F", 102.03, 0.08149, 374.2, 4.059, 0.1993],
    "r11": ["CCl₃F", 137.37, 0.06052, 471.2, 4.38, 0.2478],
    "water": ["H₂O", 18.015, 0.4615, 647.1, 22.06, 0.0560],
    "xenon": ["Xe", 131.30, 0.06332, 289.8, 5.88, 0.1186]
    
}

def molGCPCalculation(substance: str) -> Dict[str, str | float]:
    if substance not in molGCP_data:
        raise ValueError(f"Substance '{substance}' not found in molar gas data.")
    
    formula, M, R, T_crit, P_crit, V_crit = molGCP_data[substance]
    return {
        "Substance": substance.replace("_", " ").title(),
        "Formula": formula,
        "Molar Mass (kg/kmol)": M,
        "Gas Constant R (kJ/kg·K)": R,
        "Critical Temp (K)": T_crit,
        "Critical Pressure (MPa)": P_crit,
        "Critical Volume (m³/kmol)": V_crit
    }
