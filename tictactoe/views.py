from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

episodes = 100

# Create your views here.
#@csrf_exempt
def tictactoe(request):
    global episodes
    print (request)
    print (request.POST)
    if request.POST.get('training_episodes'):
        episodes = int(request.POST.get('training_episodes'))

    my_dict = {'training_episodes':str(episodes)}
    return render(request,'tictactoe/tictactoe.html',context=my_dict)