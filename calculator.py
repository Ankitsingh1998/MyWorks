#calculator
expression = " 10**2 * (10-2*4.5) "

"""
Modify the expression above with numbers and operators.
You can include: + - * / ** ^
You can include floating-point numbers (use .)
Any whitespaces are ok. 
Some common problems will be checked before computation.
"""

my_sum = lambda x,y : x+y
my_dif = lambda x,y : x-y
my_mult = lambda x,y : x*y
my_divi = lambda x,y : x/y
my_power = lambda x,y : x**y

def clear_input(inp):
    inp = inp.replace(" ", "")
    inp = inp.replace("**", "^")
    return inp
    
def check_input(inp):
    for char in inp:
        if char not in "1234567890+-*/^().":
            raise TypeError("BAD CHARACTER: {}".format(char))
    
def organize_input(inp):
    inp_list = [inp[0]]
    for char in inp[1:]:
        if char in "1234567890." and all([c in "1234567890." for c in inp_list[-1]]):
            inp_list[-1] += char
        else:
            inp_list += char
    return inp_list
    
def check_list(inp_list):
    if inp_list.count("(") != inp_list.count(")"):
        raise TypeError("BAD PARENTHESIS")
    
def compute_input(inp_list):
    
    my_operands = []
    my_operators = []
    operators = ["+", "-", "*", "/", "^"]
    operators_precedence = {"+":0, "-":0, "*":1, "/":1, "^":2, "(":-1, ")":-1}
    
    for term in inp_list:
        if all([c in "1234567890." for c in term]):
            my_operands.append(float(term))
        elif term in operators and my_operators==[]:
            my_operators.append(term)
        elif term in operators and operators_precedence[term]>=operators_precedence[my_operators[-1]]:
            my_operators.append(term)
        elif term == "(":
            my_operators.append(term)
        elif term == ")":
            while my_operators[-1] != "(":
                my_operands, my_operators = go_back(my_operands, my_operators)
            my_operators.pop()
        else:
            my_operands, my_operators = go_back(my_operands, my_operators)
            my_operators.append(term)
            
    while my_operators != []:
        my_operands, my_operators = go_back(my_operands, my_operators)
        
    return my_operands
            
def go_back(my_operands, my_operators):
    value1 = float(my_operands.pop())
    operator = my_operators.pop()
    value2 = float(my_operands.pop())
    print("Computing:", value2, operator, value1)
    if operator == "+":
        my_operands.append( my_sum(value2, value1) )
    elif operator == "-":
        my_operands.append( my_dif(value2, value1) )
    elif operator == "*":
        my_operands.append( my_mult(value2, value1) )
    elif operator == "/":
        my_operands.append( my_divi(value2, value1) )
    elif operator == "^":
        my_operands.append( my_power(value2, value1) )
    return my_operands, my_operators

inp = expression
inp = clear_input(inp)
print("Input:", inp, "\n")
check_input(inp)
inp_list = organize_input(inp)
check_list(inp_list)
result = compute_input(inp_list)
print("\nResult:", result[0])

expression = input('Enter a valid expression: ')
