from backend.core.calculations.superHeatedWater import SuperheatedSteam

def sh_water(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    steam = SuperheatedSteam(inputs=inputs)
    result = steam.calculate()
    return result