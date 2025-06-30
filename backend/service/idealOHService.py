from backend.core.calculations.idealOH import HydroxylOHProperties

def idealOHCalculation(fluid_type: str, inputs: dict):
    print("fluid_type: ", fluid_type)
    print("inputs: ", inputs)
    OH = HydroxylOHProperties(inputs=inputs)
    result = OH.calculate()
    return result