from django.shortcuts import render
from .brain import *
import simplejson as json
# Create your views here.
def home(request):
    return render(request, 'home.html')

def minterms(request):
    if(request.method == 'POST'):
        print(request.POST)
        data = request.POST
        varlist = data['varlist'].split(',')
        dontcare = data['dont-care'].split(',')
        mt = data['minterms'].split(',')
        mt = [int(x) for x in mt]
        if (dontcare[0] == ''):
            dontcare = []
        else:
            dontcare = [int(x) for x in dontcare]

        print(varlist, mt, dontcare)
        save_varlist = varlist[:]
        varlist.reverse()
        reduced = ImplementBooleanFn(varlist, mt, dontcare)
        print(reduced[0])
        return render(request, 'minterms.html', {'exp': CleanExp(reduced[0]), 'problem' : json.dumps({'varlist':save_varlist,
                                                                                                      'minterms':mt,'dontcare': dontcare }),
                                                 'var':save_varlist,'dont':dontcare,'min':mt})
    else:
        return render(request, 'minterms.html',{'exp':""})

def counter(request):
    if (request.method == 'POST'):
        data  = request.POST
        seq = [int(x) for x in data["seq"].split(',')]
        fftype = data['fftype']
        print(seq,type(fftype),fftype)
        table = solve(seq, fftype,False)
        # print(table)
        solution = [t.soln for t in table[0]]
        # for t in table[0]:
        #     print(t.name, t.soln)
        return render(request, 'counter.html', {'response':json.dumps('post'),'prev': json.dumps(seq), 'fftype':json.dumps(fftype), 'solution' : solution, 'truthtable':json.dumps(table[1])})
    intial = [0,1,2,3,4,5,6,7,0]
    intial = []
    return render(request, 'counter.html',{'response':json.dumps('get'),'prev' : json.dumps(intial), 'fftype':json.dumps('JK'), 'truthtable': json.dumps('')})


def flip_flop(request):
    e1 = "T = ((NOT G) AND (NOT Q)) OR ((NOT L) AND G AND Q)"
    if(request.method == 'POST'):
        data = request.POST
        print(data)
        num = int(data['num'])
        datlist = [num]
        for i in range(0, num):
            varkey = 'var' + str(i)
            datlist.append(data[varkey])
        for i in range(0, 2**(num + 1)):
            datkey = 'dat' + str(i)
            datlist.append(data[datkey])
        datlist.append(data['fftype'])
        print(datlist)
        # print(num, datlist[1:1 + num], datlist[-1], datlist[1 + num: -1])
        table = solveff(num, datlist[1:1 + num], datlist[-1], datlist[1 + num: -1])

        # print(table)
        solution = [t.soln for t in table[0]]
        print(solution)

        return render(request, 'flipflop.html' ,{'response':json.dumps('post'),'inputlist' : json.dumps(datlist), 'solution' : solution, 'truthtable':json.dumps(table[1])})

    return render(request, 'flipflop.html' ,{'response':json.dumps('get'),'inputlist' : json.dumps([0]), 'truthtable': json.dumps('')})
