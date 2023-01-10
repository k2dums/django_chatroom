from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'async_Chatroom/index.html',{})

def room(request,room_name):
    return render(request,'async_Chatroom/room.html',{'room_name':room_name}) 