from multiply_scalar_eqn import multiply_eqn
from subtract_two_eqn import subtract_eqn
from solve_one_var_eqn import solve1
from eliminate_one_var_linear_eqn import solve_x
from solve_two_var_linear_eqn import solve2

## Start: Function to solve three varaibles in a linear equation

def solve3(eqns): 
    if len(eqns) == 1:
         return solve1(eqns)
    eqn1 = eqns[0]
    # eliminate x by subtracting first eqn from second and third after mult coefficients
    new_eqns = []
    for eqn2 in eqns[1:]:
        mult = eqn2[0]/eqn1[0]
        eqn11 = multiply_eqn(eqn1, mult)
        neweqn = subtract_eqn(eqn2, eqn11)[1:]
        new_eqns.append(neweqn)
    # # we will be left 2 eqns and 2 var -> solve2()
    n_1_vars = solve2(new_eqns)
    x = solve_x(eqn1, n_1_vars) # y = 1, [1, 1, 10], x = 10-1*
    return [x] + n_1_vars


## End: Function to solve three varaibles in a linear equation