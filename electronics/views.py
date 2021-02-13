from django.shortcuts import render
from .brain import *
import simplejson as json
# Create your views here.
def minterms(request):
    if(request.method == 'POST'):
        print(request.POST)
        data = request.POST
        varlist = data['varlist'].split(',')
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
        varlist.reverse()
        reduced = ImplementBooleanFn(varlist, mt, dontcare)
        print(reduced[0])
        return render(request, 'minterms.html', {'exp': CleanExp(reduced[0])})
    else:
        varlist = ['A', 'B', 'C', 'D']
        mt = [2, 3, 5, ]
        dontcare = [10, 13]
        varlist.reverse()
        reduced = ImplementBooleanFn(varlist, mt, dontcare)
        return render(request, 'minterms.html',{'exp':CleanExp(reduced[0])})