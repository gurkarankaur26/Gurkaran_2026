
'''  Write a function solve_expression(expr) that takes an expression (in this special array format) and returns its value.

💡 Hint: Use recursion to handle nested expressions.'''

def solve_expression(exp):
    try:
        # If exp is a number, just return it
        if isinstance(exp, int) or isinstance(exp, float):
            return exp
        if len(exp) != 3:
            raise ValueError("Expression must be [operator, operand1, operand2]")

        operator, left, right = exp

        if not isinstance(operator, str):
            raise ValueError("First element must be an operator")    

        # Solve left and right first (recursion)        
        left_value = solve_expression(left)
        right_value = solve_expression(right)
        # Do the operation
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        elif operator == '/':
            if right_value == 0:
                raise ZeroDivisionError("Division by zero")
            return left_value / right_value
    except(ValueError,ZeroDivisionError) as e:
        print('Error:'+str(e))

