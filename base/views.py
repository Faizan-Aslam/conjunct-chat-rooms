from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets Learn Python'},
    {'id':2, 'name': 'Front-end developers'},
    {'id':3, 'name': 'Design with me'}
]
def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = None 
    for i in rooms:
        if i["id"] == int(pk):
            room = i 
    context = {'room': room}
    return render(request, 'base/room.html', context)

