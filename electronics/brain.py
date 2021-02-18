from BinPy.Algorithms.QuineMcCluskey import QM
from BinPy.Algorithms.ExpressionConvert import convertExpression
import re


def ImplementBooleanFn(variables,Ones,dont_care ):
    ''' An interactive function which takes in templates/maxterms and
    prints the Boolean Function and implementable form.
    Don't Care Conditions can also be provided (optional)
    Eg:
    Enter the list of variables
    A,B,C
    Do you want to enter templates (m) or maxterms(M)?
    m
    Enter list of templates
    1,4,7
    Enter list of Don't Care terms
    Enter X if there are none
    2,5
    The logical expression is (((NOT B) AND C) OR (A AND C) OR (A AND (NOT B)))
    Can be implemented as OR(AND(NOT(B), C), AND(A, C), AND(A, NOT(B)))
    '''
    for i in range(len(Ones)):
        if Ones[i] >= pow(2, len(variables)):
            raise Exception("Error: Invalid Minterm")
    qm = QM(variables)
    if len(dont_care) != 0:
        LogicalExpression = qm.get_function(qm.solve(Ones, dont_care)[1])
    else:
        LogicalExpression = qm.get_function(qm.solve(Ones)[1])
    GateForm = convertExpression(LogicalExpression)

    # print("The logical expression is " + LogicalExpression)
    # print("Can be implemented as " + GateForm)
    return [LogicalExpression, GateForm]

def CleanExp(exp):
    exp = re.sub(r"AND", "*", exp)
    exp = re.sub(r"OR", "+ ", exp)
    exp = re.sub(r"NOT", "!", exp)
    # exp = re.sub(r"\(", "", exp)
    return exp