from typing import Union


class UnitConverter:
    # Define conversion to base unit for each category
    to_base = {
        # Mass and Density (base: kg or kg/m³)
        "Kilograms (kg)": 1,
        "Pounds (lbs)": 0.453592,
        "Slugs (slug)": 14.5939,
        "Grams per Cubic Centimeter (g/cm³)": 1000,
        "Pounds per Cubic Foot (lb/ft³)": 16.0185,
        "Kilograms per Cubic Meter (kg/m³)": 1,

        # Length (base: meter)
        "Meters (m)": 1,
        "Centimeters (cm)": 0.01,
        "Inches (in.)": 0.0254,
        "Feet (ft)": 0.3048,

        # Velocity (base: m/s)
        "Kilometers per Hour (km/h)": 1 / 3.6,
        "Miles per Hour (mile/h)": 0.44704,

        # Volume (base: m³)
        "Cubic Meters (m³)": 1,
        "Cubic Centimeters (cm³)": 1e-6,
        "Cubic Inches (in.³)": 1.6387e-5,
        "Cubic Feet (ft³)": 0.0283168,
        "Liters (L)": 0.001,
        "Gallons (gal)": 0.00378541,

        # Force (base: N)
        "Newtons (N)": 1,
        "Pound-Force (lbf)": 4.44822,
        "Poundal (lb·ft/s²)": 0.138255,

        # Pressure (base: Pa)
        "Pascals (Pa)": 1,
        "Bar ": 1e5,
        "Atmosphere (atm)": 101325,
        "Pounds per Square Inch (psi)": 6894.76,
        "Pounds per Square Feet (lbf/ft²)": 47.8803,

        # Energy and Specific Energy (base: J or J/kg)
        "Joules (J)": 1,
        "Kilojoules (kJ)": 1000,
        "British Thermal Unit (BTU)": 1055.06,
        "Kilojoules per Kilogram (kJ/kg)": 1000,
        "British Thermal Units per Pound (BTU/lb)": 2326,
        "Foot-Pound Force (ft·lbf)": 1.35582,
        "Kilocalorie (kcal)": 4184,

        # Energy Transfer Rate (base: W)
        "Watts (W)": 1,
        "KiloWatts (kW)": 1000,
        "British Thermal Unit per Hour (BTU/hr)": 0.293071,
        "Horsepower (hp)": 745.7,
        "Foot-Pound Force per Second (ft·lbf/s)": 1.35582,

        # Specific Heat (base: J/kg·K)
        "Kilojoules per Kilogram-Kelvin (kJ/kg·K)": 1000,
        "Kilocalories per Kilogram-Kelvin (kcal/kg·K)": 4184,
        "British Thermal Unit per Pound-Degree Rankine (Btu/lb·°R)": 4184 / 1.8,
    }

    from_base = {unit: 1 / factor for unit, factor in to_base.items()}

    @classmethod
    def convert(cls, value: Union[int, float], from_unit: str, to_unit: str) -> float:
        if from_unit == to_unit:
            return round(value, 3)
        if from_unit not in cls.to_base or to_unit not in cls.from_base:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")

        base_value = value * cls.to_base[from_unit]
        return round(base_value * cls.from_base[to_unit], 3)
