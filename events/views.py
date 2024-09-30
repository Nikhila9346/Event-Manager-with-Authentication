from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def home(request):

    if request.method == 'POST':

        event = request.POST.get('event')
        location = request.POST.get('location')
        date = request.POST.get('date')

        Event.objects.create(
            event = event,
            location = location,
            date = date,
            user = request.user
        )
        return redirect('home')

    event_details = Event.objects.filter(user = request.user).order_by('-id')
    print(event_details)
    context = {
        'event': event_details,
        'user' : request.user
    }
    return render(request, 'home.html', context)

def edit_event(request, id):
    e_update = Event.objects.get(id=id)

    #taking the upadated values from user
    if request.method == 'POST':
        event = request.POST['event']
        location = request.POST['location']
        date = request.POST['date']

        #update values
        e_update.event = event
        e_update.location = location
        e_update.date = date
        
        e_update.save()
        return redirect('home')
    
    context = {
        'details': e_update
    }
    return render(request, 'event.html', context)

def event_delete(request, id):
    del_event = Event.objects.get(id=id)
    del_event.delete()
    return redirect('home')

def event_details(request, id):
    event = Event.objects.get(id=id)

    context = {
        'details': event
    }
    return render(request, 'event_details.html', context)