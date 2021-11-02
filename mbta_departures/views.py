from django.shortcuts import render
from .forms import BoardViewForm
from .station import Station

def home(request):
    if 'name' in request.POST:
        form = BoardViewForm(request.POST)
        if form.is_valid():
            station = Station(form.cleaned_data['name'])
            return render(request, 'home.html',
                          {'form': form, 'station': station})
    else:
        form = BoardViewForm()
    return render(request, 'home.html',
                  {'form': form})
