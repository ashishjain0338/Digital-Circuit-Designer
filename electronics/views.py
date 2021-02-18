from django.shortcuts import render
from .brain import *
import simplejson as json
# Create your views here.
def minterms(request):
    if(request.method == 'POST'):
        print(request.POST)
        data = request.POST
        varlist = data['varlist'].split(',')
        while(' ' in  varlist):
            varlist.remove(' ')
        dontcare = data['dont-care'].split(',')
        mt = data['minterms'].split(',')
        if (mt[0] == 'X'):
            mt = []
        else:
            mt = [int(x) for x in mt]
        if (dontcare[0] == 'X'):
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
        varlist = ['A', 'B', 'C', 'D']
        mt = [2, 3, 5, ]
        dontcare = [10, 13]
        varlist.reverse()
        reduced = ImplementBooleanFn(varlist, mt, dontcare)
        return render(request, 'minterms.html',{'exp':CleanExp(reduced[0])})