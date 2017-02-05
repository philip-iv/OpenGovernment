from django.shortcuts import render
from .models import Senator, Representative

def index(request):
    return render(request, 'us/congress/index.html', {'chamber': 'congress'})

def senate_index(request):
    return render(request, 'us/congress/index.html', {'chamber': 'senate'})
    
def house_index(request):
    return render(request, 'us/congress/index.html', {'chamber': 'house'})
    
def senate_state(request, state):
    context = {}
    context['state'] = state.upper()
    senior = Senator.objects.get(state=state.upper(), in_office=1, seniority='S')
    junior = Senator.objects.get(state=state.upper(), in_office=1, seniority='J')
    for sen in (senior, junior):
        context[sen.seniority + '_name'] = sen.first_name + ((' %s ' % sen.middle_name) if sen.middle_name != '' else ' ') + sen.last_name + ((' %s' % sen.suffix) if sen.suffix != '' else '')
    print context
    return render(request, 'us/congress/senate_state.html', context)