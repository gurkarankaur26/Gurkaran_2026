from multiply_scalar_eqn import multiply_eqn
from subtract_two_eqn import subtract_eqn
from solve_one_var_eqn import solve1
from eliminate_one_var_linear_eqn import solve_x
from solve_two_var_linear_eqn import solve2
from solve_n_var_linear_eqn import solven

## Start: Function to solve n varaibles in a linear equation

def solven(eqns): 
    n_vars=[]
    x=[]    
    if len(eqns) == 1:
        a, b = eqns[0]
        return [(b / a)]
    eqn1 = eqns[0]
    # eliminate x by subtracting first eqn from rows below after mult coefficients    
    new_eqns = []
    for eqn2 in eqns[1:]:
        mult = eqn2[0]/eqn1[0]
        eqn11 = multiply_eqn(eqn1, mult)
        neweqn = subtract_eqn(eqn2, eqn11)[1:]
        new_eqns.append(neweqn)
    n_vars = solven(new_eqns)
    x =solve_x(eqn1,n_vars)
    return [x] + n_vars

## End: Function to solve n varaibles in a linear equation
    