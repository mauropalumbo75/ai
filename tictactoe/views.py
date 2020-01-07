from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ai import (Agent, Human, Environment, get_state_hash_and_winner, initialV_x,
            initialV_o, play_game, )

episodes = 100

# Create the agents and a human player for training and playing
p1 = Agent()
p2 = Agent()
human = Human()

# Create the environment
env = Environment()
state_winner_triples = get_state_hash_and_winner(env)

# set initial V for p1 and p2
Vx = initialV_x(env, state_winner_triples)
p1.setV(Vx)
Vo = initialV_o(env, state_winner_triples)
p2.setV(Vo)

# give each player their symbol
p1.set_symbol(env.x)
p2.set_symbol(env.o)
human.set_symbol(env.o)

def train(episodes):
    for t in range(episodes):
        if (t % 200 == 0):
            print(t)
        play_game(p1, p2, Environment())

def play(verbose=True):
    p1.set_verbose(verbose)
    play_game(p1, human, Environment(), draw=2)

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