from multiply_two_eqn import elementwise_mult
## Start:Function to eliminate a variable from an equations

# x + 3*y + 2*z = 20
# y, z = [5, -5]
# x = 20 - (3*5 + 2*-5)

#solve_x([4,3,2,7, 20], [5, -5, 8])
# 4x + 3*y + 2*z + 7u = 20
# y, z, u = [5, -5, 8]
# 4x = 20 - (3*5 + 2*-5 + 7*8)
# x = (20 - (3*5 + 2*-5 + 7*8))/4
def solve_x(eqn1, n_1_vars):
    eqn11 = eqn1[1:-1]
    rhs = eqn1[-1] - sum(elementwise_mult(eqn11, n_1_vars))
    return rhs / eqn11[0]

## End: Function to eliminate a variable from an equations