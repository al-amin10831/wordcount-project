from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')


def count(request):
    fulltext=request.GET['Giventext']

    wordcount=fulltext.split()

    dictionary = {}

    for word in wordcount:
        if word in dictionary :
            dictionary [word]+=1
        else:
            dictionary[word] = 1

    swords=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'wordcount':len(wordcount),'dictionary':swords})

def about(request):
    return render(request,'about.html')