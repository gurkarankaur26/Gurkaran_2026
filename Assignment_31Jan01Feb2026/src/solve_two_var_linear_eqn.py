from multiply_scalar_eqn import multiply_eqn
from subtract_two_eqn import subtract_eqn
from solve_one_var_eqn import solve1
from eliminate_one_var_linear_eqn import solve_x

## Start: Function to solve two varaibles in a linear equation

# x + y = 10
# 2x + y = 15
eqns = [[1, 1, 10], [2, 1, 15]]

def solve2(eqns): 
    eqn1 = eqns[0] # First Equation
    eqn2 = eqns[1] # Second Equation
    mult = eqn2[0]/eqn1[0]
    eqn11 = multiply_eqn(eqn1, mult)
    eqn21 = subtract_eqn(eqn2, eqn11)[1:] # Subract both equations and remove x as it is 0
    n_1_vars = solve1([eqn21])
    x = solve_x(eqn1, n_1_vars) # y = 1, [1, 1, 10], x = 10-1*
    return [x] + n_1_vars

## End: Function to solve two variables in a linear equation