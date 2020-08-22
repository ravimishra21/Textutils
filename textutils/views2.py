# this file is created by me .
from django.http import HttpResponse
from django.shortcuts import render

def ex1(request):
    nav = '''<h2> Navigation bar <br></h2>
    <a href="https://www.google.com/">google</a><br>
    <a href="https://www.reck.ac.in">reck</a><br>
    <a href="https://www.sarkariresult.com/">job</a><br>
    <a href="https://www.youtube.com/">utube</a><br>
    '''
    return HttpResponse(nav)
def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    caps=request.POST.get('caps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    # check which checkbox is on 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif caps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'write in capitals', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=='on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char                
                params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlineremover=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char                
                params = {'purpose': 'new line remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
        