# I have created this file - Yogesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':"Yogesh", 'place':'MARS'}
    return render(request, 'index.html', params)

def analyze(request):
    
    #get the text
    djtext = request.POST.get('text','default')

    #check checkboxe values
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase','off')
    new_line_remover = request.POST.get('newlineremover','off')
    space_remover = request.POST.get('spaceremover','off')
    count_char = request.POST.get('charcount','off')
    
    #check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        
        djtext = analyzed
        params = {'purpose':'Remove Punctuations', 'analyzed_text':djtext}
        
        # return render(request, 'analyze.html', params)
    
    if (uppercase == "on"):
        analyzed=''
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        djtext = analyzed
        params = {'purpose':'CAPITALIZE TEXT', 'analyzed_text':djtext}

        # return render(request, 'analyze.html', params)
    
    if (new_line_remover == "on"):
        analyzed=''
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        
        djtext = analyzed
        params = {'purpose':'New Line Remover', 'analyzed_text':djtext}

        # return render(request, 'analyze.html', params)
    
    if (space_remover == "on"):
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char
        
        djtext = analyzed
        params = {'purpose':'Extra Space Remover', 'analyzed_text':djtext}

        # return render(request, 'analyze.html', params)
    
    if (count_char == "on"):
        analyzed=''
        counts = 0
        for char in djtext:
            counts = counts + 1
        
        analyzed = counts
        djtext = djtext + " count = " + str(analyzed)
        params = {'purpose':'Count Characters', 'analyzed_text':djtext}

        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and uppercase != "on" and new_line_remover != "on" and space_remover != "on" and count_char != "on"):
        return HttpResponse("Error - select any operation")
    
    return render(request,'analyze.html',params)