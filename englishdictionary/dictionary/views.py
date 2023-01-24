from django.shortcuts import render
from ..dist.PyDictionary import PyDictionary

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonyms(search)
    antonyms = dictionary.antonyms(search)
    context = {
        'meaning': meaning,
        'antonyms': antonyms,
        'synonyms': synonyms
    }
    return render(request, 'word.html', context)