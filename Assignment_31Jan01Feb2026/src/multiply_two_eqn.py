## Start: Function to multiple two polynomials/equations
def elementwise_mult(eqn1, eqn2):
    # eqn1 = [1, 2, 3]
    # eqn2 = [3, 4, 5]
    # result = [1*3, 2*4, 3*5]
    result = []
    for i, x in enumerate(eqn1):
        result.append(x * eqn2[i])
    return result

## End: Function to multiple two polynomials/equations