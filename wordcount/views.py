from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionry = {}
    for word in wordlist:
        if word in worddictionry:
            #Increment
            worddictionry[word] +=1
        else:
            #New Word
            worddictionry[word] = 1
    sortedwords = sorted(worddictionry.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionry':worddictionry.items(), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')
