from BinPy.Algorithms.QuineMcCluskey import QM
from BinPy.Algorithms.ExpressionConvert import convertExpression
import re
import pandas as pd

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


J = ['0', '1', 'X', 'X']
K = ['X', 'X', '1', '0']
T = ['0', '1', '1', '0']
D = ['0','1','0','1']
db = {"J":J, "K":K, "T":T, "D":D}

class Table():
    def __init__(self,name, type, vars):
        self.name = name
        self.code = ['X' for i in range(0,2**vars)]
        self.type = type
        self.vars = vars
        self.soln = ""
        self.varlist = []
        for i in range(0,vars):
            self.varlist.append(chr(ord('A') + i))
        self.varlist.reverse()

    def get_index(self, a, b):
        if (a == '0' and b == '0'):
            return 0
        elif (a == '0' and b == '1'):
            return 1
        elif (a == '1' and b == '0'):
            return 2
        else:
            return 3

    def setvarlist(self, variablelist):
        if(self.vars == len(variablelist)):
            variablelist.reverse()

            self.varlist = variablelist
        else:
            print("Number of Variables dont match")

    def fill_code(self, pos,present,next):
        excitation_table = db[self.type]
        self.code[pos] = excitation_table[self.get_index(present, next)]

    def get_minterms(self):
        ones = []
        dcare = []
        for i in range(0, len(self.code)):
            if(self.code[i] == '1'):
                ones.append(i)
            elif(self.code[i] == 'X'):
                dcare.append(i)

        return ones,dcare

    def solve(self):
        ones, dcare = self.get_minterms()
        # print(ones, dcare, self.name)
        self.soln = self.name +  " = " +  ImplementBooleanFn(self.varlist, ones, dcare)[0]
        return self.soln

    def get_soln(self):
        return self.soln

    def __str__(self):
        return self.type + " --> " + self.name + "\tCode -->"+str(self.code)


def create_table(table, code, precision, seq):
    df = pd.DataFrame()
    count = 1
    # ---------- Adding present States -----------------
    vars = table[0].varlist
    inter = []
    for i in range(0, len(vars)):
        inter.append([])

    for lists in inter:
        added = 0
        add = False
        for i in range(0,2**precision):
            if(added == count):
                add = not add
                added = 0
            lists.append(int(add))
            added = added + 1
        count = count * 2
    for i in range(0,len(vars)):
        df[vars[len(vars) - i - 1]] = inter[len(inter) - 1 - i]

    # -------- Adding Next States -------
    inter = []
    for i in range(0, len(vars)):
        inter.append(['X' for i in range(0, 2**precision)])
    for seq_index in range(1, len(seq)):
        index = seq[seq_index - 1]

        next_state = code[seq_index]
        for codeword_iterater in range(0, precision):
            inter[codeword_iterater][index] = next_state[codeword_iterater]

    for i in range(0,len(vars)):
        df[vars[len(vars) - i - 1] + '+'] = inter[i]

    for t in table:
        df[t.name] = t.code
    return df


def binary(num, out):
    if num >= 1:
        out = binary(num // 2, out)
    out = out + str(num % 2)
    return out

def get_binary(num, precision):
    bin = binary(num, "")
    bin = bin[1:]
    if(len(bin) == precision):
        return bin
    elif(len(bin) < precision):
        precision-=len(bin)
        zeroes = ""
        while(precision):
            zeroes+='0'
            precision = precision - 1
        bin = zeroes + bin
    return bin

def get_max_bits(seq):
    maximum = max(seq)
    max_binary =  binary(maximum, "")
    max_binary = max_binary[1:]
    return len(max_binary)

def fill_table(code,type, precision, seq):
    table = []
    var = 'A'
    if(type == "JK"):
        # Creating Table Objects
        for x in range(0,len(code[0])):
            name = "J" + var
            obj1 = Table(name, 'J', precision)
            table.append(obj1)
            name = "K" + var
            obj2 = Table(name, 'K', precision)
            table.append(obj2)
            var = chr(ord(var) + 1)

        # Filling the table
        for i in range(0, len(code) - 1):
            first = code[i]
            second = code[i + 1]
            table_ind = 0
            for j in range(0, len(first)):
                table[table_ind].fill_code(seq[i], first[j],second[j])
                table[table_ind + 1].fill_code(seq[i], first[j], second[j])
                table_ind = table_ind + 2

        for t in table:
            t.solve()

    elif(type == "T" or type =="D"):
        for x in range(0,len(code[0])):
            name = type + var
            obj1 = Table(name, type, precision)
            table.append(obj1)
            var = chr(ord(var) + 1)

        # Filling the table
        for i in range(0, len(code) - 1):
            first = code[i]
            second = code[i + 1]
            table_ind = 0
            for j in range(0, len(first)):
                table[table_ind].fill_code(seq[i],first[j],second[j])
                table_ind = table_ind + 1

        for t in table:
            t.solve()
    return table


def solve(seq, fftype,show = False, getdf = True):
    precision = get_max_bits(seq)
    code = [get_binary(num, precision) for num in seq]
    # Solving the Counters problem
    table = fill_table(code, fftype, precision, seq)
    if (getdf or show):
        truth_table = create_table(table, code, precision, seq)
    if (show):
        for t in table:
            print(t, t.get_soln())
        print(truth_table)
    return [table, truth_table.to_html(classes="table table-hover")]


def create_table_ff(table, Qnext, precision):
    df = pd.DataFrame()
    count = 1
    vars = table[0].varlist
    inter = []
    for i in range(0, len(vars)):
        inter.append([])

    for lists in inter:
        added = 0
        add = False
        for i in range(0, 2 ** precision):
            if (added == count):
                add = not add
                added = 0
            lists.append(int(add))
            added = added + 1
        count = count * 2
    for i in range(0, len(vars)):
        df[vars[len(vars) - i - 1]] = inter[len(inter) - 1 - i]
    df['Q+'] = Qnext
    for t in table:
        df[t.name] = t.code
    return df


def fill_tableff(num, varlist,fftype, next):
    table = []
    varlist.append('Q')
    if(fftype == 'JK'):
        name = "J"
        obj1 = Table(name, 'J', num + 1)
        obj1.setvarlist(varlist[:])

        table.append(obj1)
        name = "K"
        obj2 = Table(name, 'K', num + 1)
        obj2.setvarlist(varlist[:])
        table.append(obj2)
    elif(fftype == 'T' or fftype == 'D'):
        name = fftype
        obj1 = Table(name, fftype, num + 1)
        obj1.setvarlist(varlist[:])
        table.append(obj1)

    for t in table:
        present = '0'
        for i in range(0, 2**(num + 1)):
            t.fill_code(i, present, str(next[i]))
            if(present == '0'):
                present = '1'
            else:
                present = '0'

    for t in table:
        t.solve()
    return table


def solveff(num, varlist,fftype, next,show = False, getdf = True):
    table = fill_tableff(num , varlist, fftype, next)
    if (getdf or show):
        truth_table = create_table_ff(table, next, num + 1)
    if (show):
        for t in table:
            print(t, t.get_soln())
        print(truth_table)
    return [table, truth_table.to_html(classes="table table-hover")]

# table = solveff(2, ['P', 'D'], 'JK', [1,1,0,0,0,1,1,0])
# create_table_ff(table, [1,1,0,0,0,1,1,0], 3)

# solveff(2, ['P', 'D'], 'JK', [1,1,0,0,0,1,1,0], show=True)