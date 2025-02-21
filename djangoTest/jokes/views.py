from django.shortcuts import render
import pyjokes

# Create your views here.
def joke(request):
    return render(request, 'jokes/joke.html', {
        'joke': pyjokes.get_joke()            
    })

# tady jsem skončil, běž do html a dopiš to tam