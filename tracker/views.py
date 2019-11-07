from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

# Homepage that is fetched initially
def homepage(request):
    form = NameForm() # Initializes an empty form on inital load
    return render(request,'tracker/index.html', {'form': form})

# Takes input from the search bar and processes the data
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            pass  
    else:
        form = NameForm() 

    return render(request, 'tracker/index.html', {'form': form})