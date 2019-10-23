

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def readFile(request):
    fr=open('C:\\Users\\Appy\\PycharmProjects\\textutils\\textutils\\textutils\\abcd.txt',"r")
    contents=fr.read()
    return HttpResponse(contents)

def about(request):
    return HttpResponse('<h1>About </h1>')

def removepunc(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse("remove punc <br><a href='/'>Back</a><br>")

def capfirst(request):
    return HttpResponse("capitalize first<br><a href='/'>Back</a><br>")

def newlineremove(request):
    return HttpResponse("new line remove <br><a href='/'>Back</a><br>")

def spaceremove(request):
    return HttpResponse("space remover <br><a href='/'>Back</a><br>")


def charcount(request):
    return HttpResponse("charcount <br><a href='/'>Back</a><br>")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'default')
    fullcaps= request.POST.get('uppercase', 'off')
    newLineRemover= request.POST.get('newLineRemover', 'off')
    ExtraspaceRemover = request.POST.get('ExtraspaceRemover', 'off')
    analyzed = ''
    result=djtext
    purpose=''

    if removepunc == 'on':
        punctuations = '''":;@#$%^&*"(){}[].,'<>/?|!\''''
        for char in result:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        result= analyzed
        purpose += " | Remove Punctuations "
        #return render(request, "analyze.html", params)

    if fullcaps == 'on':
        for char in result:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        #return render(request, "analyze.html", params)
        result = analyzed
        purpose += " | Change to uppercase  "

    if newLineRemover == 'on' :
        for char in result:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char.upper()
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
       # return render(request, "analyze.html", params)
        result = analyzed
        purpose += " | Remove new line  "

    if ExtraspaceRemover == 'on':
        for index, char in enumerate(result):
            if result[index] == ' ' and result[index+1] == ' ':
                pass
            else:
                analyzed = analyzed + char;
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        #return render(request, "analyze.html", params)
        result = analyzed
        purpose += " | Remove extra space  "

    if removepunc == 'on' or fullcaps == 'on' or newLineRemover == 'on' or ExtraspaceRemover == 'on' or CharacterCounter == 'on' :
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('error')


def navigation(request):
    s="<h2>Navigation Bar</h2><br>" \
      "<a href='Google.com'>Google</a><br>" \
      "<a href='https:\www.facebook.com\'>Facebook</a>"

    return HttpResponse(s)