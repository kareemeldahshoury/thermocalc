from typing import Callable, Dict, Any


from .ref_cop import solve_ref_cop
from .erbSteadyState import solve_erb_steady_state
from .ccEff import solve_carnot_efficiency
from .hp_cop import solve_hp_cop
from .massFlowRate import solve_mass_flow_rate
from .idealGasLaw import solve_ideal_gas_law
from .isentropicRelations import solve_isentropic_relations



GENERAL_SOLVERS: Dict[str, Callable[[str, Dict[str, float]], Any]] = {
    "refEfficency": solve_ref_cop,
    "erb1SteadyState": solve_erb_steady_state,
    "carnotEfficiency": solve_carnot_efficiency,
    "heatPumpEfficiency" : solve_hp_cop,
    "massFlowRate" : solve_mass_flow_rate,
    "idealGasLaw" : solve_ideal_gas_law,
    "isentropicRelations" : solve_isentropic_relations

}

def get_general_solver(equation_id: str):
    if not equation_id:
        raise ValueError("Missing equationId")
    key_exact = equation_id
    key_lower = equation_id.lower()
    if key_exact in GENERAL_SOLVERS:
        return GENERAL_SOLVERS[key_exact]
    if key_lower in GENERAL_SOLVERS:
        return GENERAL_SOLVERS[key_lower]
    raise ValueError(f"Unknown equationId: {equation_id!r}")
