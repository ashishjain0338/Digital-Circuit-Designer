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
        print(request.POST)
        data  = request.POST
        seq = [int(x) for x in data["seq"].split(',')]
        print(seq)
        return render(request, 'counter.html', {'prev': json.dumps(seq), 'fftype':json.dumps('JK')})
    return render(request, 'counter.html',{'prev' : json.dumps([1,1024]), 'fftype':json.dumps('JK')})
