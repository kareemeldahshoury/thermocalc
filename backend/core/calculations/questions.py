questions_unitConversion = {
    "q1": {
        "prompt": (
            "<strong>Perform the following unit conversions:\n </strong>"
            "\n"
            "a) 122 in³ → L\n"
            "b) 778.17 ft·lbf → kJ\n"
            "c) 100 hp → kW\n"
            "d) 1000 lb/h → kg/s\n"
            "e) 29.392 lbf/in² → bar\n"
            "f) 2500 ft³/min → m³/s\n"
            "g) 75 mile/h → km/h\n"
            "h) 1 ton (2000 lbf) → N"
        ),
        "answers": [2, 1.055, 74.57, 0.126, 2.03, 1.18, 120.701, 8896.44],
    },
    "q2": {
        "prompt": (
            "A gas enters a compressor that provides a pressure ratio "
            "(exit pressure / inlet pressure) equal to 8. If a gage indicates "
            "the gas pressure at the inlet is 5.5 psig, and Atmospheric Pressure is 14.5 lbf/in² \n\n"
            "<strong>Determine:</strong> \n"
            "a) Absolute Pressure, in psia, of the gas at the exit"
        ),
        "answers": [160],
    },
    "q3": {
        "prompt": (
            "An object with an initial horizontal velocity of 20 ft/s experiences a constant "
            "horizontal acceleration due to the action of a resultant force applied for 10 s. "
            "The work of the resultant force is 10 Btu. The mass of the object is 55 lb.\n\n"
            "<strong>Determine:</strong>\n"

            "a) The constant horizontal acceleration, in ft/s²"
        ),
        "answers": [7.75],
    },

    "q4": {
        "prompt": (
            "An electric motor draws a current of 10 A with a voltage of 110 V.\n"
            "The output shaft develops a torque of 9.7 N·m and a rotational speed of 1000 RPM.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The electric power required, in kW<br>"
            "b) The power developed by the output shaft, in kW<br>"
            "c) The average surface temperature, T<sub>s</sub>, in °C, if heat transfer occurs by convection "
            "to the surroundings at T<sub>f</sub> = 21 °C"
        ),
        "image": "/static/practice/firstLawQ4.png",
        "answers": [-1.1, 1.016, 42.5],
    },

        "q5": {
        "prompt": (
            "A concentrating solar collector system, as shown in image below, provides "
            "energy by heat transfer to a power cycle at a rate of 2 MW. The cycle thermal "
            "efficiency is 36%.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The power developed by the cycle, in MW<br>"
            "b) The work output, in MW∙h, for 4380 hours of steady-state operation<br>"
            "c) The total dollar value of the work output if electricity is valued at $0.08/kW∙h" 
            
        ),
        "image": "/static/practice/firstLawQ5.png",
        "answers": [0.72, 3153.6, 252300],
    },
    "q6": {
        "prompt": (
            "As shown in the figure, a well‐insulated tank fitted with an electrical resistor of negligible "
            "mass holds 2 kg of nitrogen (N₂), initially at 300 K and 1 bar. Over a period of 10 minutes, "
            "electricity is provided to the resistor at a constant voltage of 120 volts and with a constant "
            "current of 1 ampere. Assume ideal gas behavior.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the nitrogen's final temperature, in K\n"
            "b) the nitrogen's final pressure, in bar"
        ),
        "image": "/static/practice/firstLawQ6.png",
        "answers": [348.4, 1.16],
    },

    "q7": {
        "prompt": (
            "Water in a piston-cylinder assembly, initially at a temperature of 99.63°C and a quality of 65%, "
            "is heated at constant pressure to a temperature of 200°C.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the mass of water, in kg, if the work during the process is +300 kJ\n"
            "b) the values of the specific internal energies u₁,\n"
            "c) and u₂\n"
            "d) the heat transfer, in kJ (neglect kinetic and potential energy changes)"
        ),
        "answers": [2.8, 1775.04, 2658.1, 2772.6 ],
    },

    "q8": {
        "prompt": (
            "0.1 kg of oxygen (O₂) gas within a piston-cylinder assembly undergoes an expansion "
            "from a volume V₁ = 0.01 m³ to a volume V₂ = 0.03 m³. The relationship between pressure "
            "and volume during the process is p = A·V⁻¹ + B, where A = 0.06 bar·m³ and B = 3.0 bar. "
            "The O₂ is considered an ideal gas and kinetic and potential energy effects can be ignored.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The initial pressure in bar\n"
            "b) The work, in kJ\n"
            "c) The final temperature in K\n"
            "d) The heat transfer during the process, in kJ"
        ),
        "answers": [9.0, 12.59, 577.3, 28.77],
    },

    "q9": {
        "prompt": (
            "Air contained in a piston-cylinder assembly initially at 4 bar, 600 K, and a volume of 1 L, "
            "undergoes an isothermal (T=const) expansion to a final state where the volume is 2 L. "
            "Assuming the ideal gas model for air.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The mass of air, in grams\n"
            "b) The work, in kJ\n"
            "c) The heat transfer, in kJ"
        ),
        "answers": [2.3, .275, .275],
    },
}


questions_sysProperties = {
        "q1": {
        "prompt": (
            "A closed system consists of 0.3 kmol of octane occupying a volume of 5 m³.\n"
            "Let g = 9.81 m/s². \n\n"
            "<strong>Determine: </strong>\n"
            "a) the weight of the system, in N, and\n"
            "b) the molar- and mass-based specific volumes, in m³/kmol and m³/kg respectively\n"
            
        ),
        "answers": [231.4, 16.67],
    },

     "q2": {
        "prompt": (
            "The picture below shows a tank within a tank, each containing air. Pressure gage A, which "
            "indicates pressure inside tank A, is located inside tank B and reads 5 psig (vacuum). The U-tube "
            "manometer connected to tank B contains water with a column length of 10 in. Using data on the"
            "diagram, determine the absolute pressure of the air inside tank B and inside tank A, both in psia. "
            "The atmospheric pressure surrounding tank B is 14.7 psia. The acceleration of gravity is g = 32.2 ft/s² \n\n"
            
            "<strong>Determine:</strong><br>"
            "a) Absolute pressure inside Tank B (psia)<br>"
            "b) Absolute pressure inside Tank A (psia)"
        ),
        "image": "/static/practice/sysQ3.png",
        "answers": [15.1, 10.1],
    },

        "q3": {
        "prompt": (
            "A closed, rigid tank is filled with a gas modeled as an ideal gas, initially at 27 °C "
            "and a gage pressure of 300 kPa. The gas is heated, and the gage pressure at the final "
            "state is 367 kPa. The local atmospheric pressure is 1 atm.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the final temperature, in °C"
        ),
        "answers": [71.85],
    },

    "q4": {
        "prompt": (
            "Refrigerant 134a enters the evaporator of a system operating at steady state "
            "at –4°C and quality of 20% with a velocity of 7 m/s. At the exit, the refrigerant is a "
            "saturated vapor at –4°C. The evaporator flow channel has constant diameter. "
            "The mass flow rate of the entering refrigerant is 0.1 kg/s.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the diameter of the evaporator flow channel, in cm\n"
            "b) the velocity at the exit, in m/s"
        ),
        "answers": [1.732, 33.7],
    },

        "q5": {
        "prompt": (
            "The figure below shows a mixing tank initially containing 2000 lb of liquid water. "
            "The tank has two inlet pipes: one delivering hot water at a mass flow rate of 0.8 lb/s, "
            "and the other delivering cold water at a mass flow rate of 1.2 lb/s. "
            "Water exits through a single pipe at a mass flow rate of 2.5 lb/s.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The mass of water, in lb, in the tank after 30 minutes"
        ),
        "image": "/static/practice/sysQ5.png",
        "answers": [1100],
    },

    "q6": {
        "prompt": (
            "As shown in the figure below, air with a volumetric flow rate of 15,000 ft³/min enters "
            "an air-handling unit at 35°F, 1 atm. The air-handling unit delivers air at 80°F, 1 atm "
            "to a duct system with three branches consisting of two 26-in.-diameter ducts and one "
            "50-in. duct. The velocity in each 26-in. duct is 10 ft/s.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the mass flow rate of air entering the air-handling unit, in lb/s\n"
            "b) the volumetric flow rate in each 26-in. duct, in ft³/min\n"
            "c) the velocity in the 50-in. duct, in ft/s"
        ),
        "image": "/static/practice/sysQ6.png",
        "answers": [20.05, 2212.2, 14.6],
    },

    "q7": {
        "prompt": (
            "At steady state, air at 200 kPa, 325 K, and mass flow rate of 0.5 kg/s enters "
            "an insulated duct having differing inlet and exit cross-sectional areas. "
            "The inlet cross-sectional area is 6 cm². At the duct exit, the pressure of the air is "
            "100 kPa and the velocity is 250 m/s. Neglecting potential energy effects and modeling "
            "air as an ideal gas with constant c<sub>p</sub> = 1.008 kJ/kg·K.\n\n"
            "<strong>Determine:</strong>\n"
            "a) the velocity of the air at the inlet, in m/s\n"
            "b) the temperature of the air at the exit, in K\n"
            "c) the exit cross-sectional area, in cm²"
        ),
        "answers": [388.6, 368.9, 21.2],
    },

    "q9": {
        "prompt": (
            "100-kg of Refrigerant 134a at 200 kPa are contained in a piston-cylinder device whose "
            "volume is 12.311 m³. The piston is now moved until the volume is one-half its original size. "
            "This is done such that the pressure of the Refrigerant 134a does not change.\n\n"
            "<strong>Determine:</strong>\n"
            "a) The final temperature of Refrigerant 134a (°C)\n"
            "b) The change in the total internal energy of the Refrigerant 134a (kJ/kg)"
        ),
        "answers": [-10.09, -110.6],
    },
}

questions_heatTransfer = {
    "q1": {
        "prompt": (
            "A 6-in. insulated frame wall of a house has an average thermal conductivity of 0.04 Btu/h·ft·°R."
            "The inner surface of the wall is at 68°F and the outer surface is at 40°F.\n\n"
            "<strong>Determine:</strong>\n"
            "a) At steady state, the rate of heat transfer through the wall (Btu/h)"
            "b) If the wall is 20 ft × 10 ft, the total amount of energy transfer in 10 hours (Btu)"
        ),
        "answers": [448, 4480],
    },

        "q2": {
        "prompt": (
            "A half-gallon container of milk at 65 °F is placed in a refrigerator. "
            "The milk cools to 40 °F after 25 minutes have elapsed. "
            "If energy is removed from the milk by heat transfer at a constant rate:\n\n"
            "<strong>Determine:</strong>\n"
            "a) the rate of heat transfer, in Btu/s, during the cooling process.\n\n"
            "The specific heat and density of the milk are 0.94 Btu/lb·°R and 64 lb/ft³, respectively. "
            "Kinetic and potential energy effects can be neglected."
        ),
        "answers": [-0.067],
    },
}

questions_by_unit = {
    "unitConversion": questions_unitConversion,
    "sysProperties": questions_sysProperties,
}


import random

def get_random_question(unit: str):
    if unit not in questions_by_unit:
        return {"error": f"Unknown unit category: {unit}"}

    questions = questions_by_unit[unit]
    key = random.choice(list(questions.keys()))
    q = questions[key]

    result = {
        "id": key,
        "num_answers": len(q["answers"]),
    }

    if "prompt" in q:
        result["prompt"] = q["prompt"]
    if "image" in q:
        result["image"] = q["image"]

    return result

