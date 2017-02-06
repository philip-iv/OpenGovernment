from django.shortcuts import render
from django.http import Http404, HttpResponse
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
        context[sen.seniority + '_first_name'] = sen.first_name
        context[sen.seniority + '_last_name'] = sen.last_name
    print context
    return render(request, 'us/congress/senate_state.html', context)
    
def senate_individual(request, state, first, last):
    context = {}
    try:
        sen = Senator.objects.get(state=state.upper(),first_name=first.title(),last_name=last.title())
    except:
        raise Http404("Senator does not exist")
    context['name'] = sen.first_name + ((' %s ' % sen.middle_name) if sen.middle_name != '' else ' ') + sen.last_name + ((' %s' % sen.suffix) if sen.suffix != '' else '')
    context['state'] = state.upper()
    context['id'] = sen.bioguide_id
    return render(request, 'us/congress/individual.html', context)

def senate_committees(request):
    return HttpResponse("Committees info")