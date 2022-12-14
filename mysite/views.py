from django.http import HttpResponse
from django.shortcuts import render



def result(request):
    mainstring =  request.GET.get('mainstring')
    cap = request.GET.get('cap')
    lower = request.GET.get('lower')
    remove = request.GET.get('rmvspaces')
  
    if cap == 'on':
        purpose = "CAPTILIAZE THE STRING"
        mainstring = str(mainstring).upper
    elif lower == 'on':
        purpose = "change the cgaracters in lower form"
        mainstring = str(mainstring).lower
    elif remove == 'on':
        purpose = "RemoveTheSpacesIntheString"
        mainstring = str(mainstring).replace(" ","")
    analyzed = mainstring
    params = {'purpose' : purpose,'analyzed_text' : analyzed}
    return render(request,'result.html',params)



def home(request):
    return render(request,'Home.html')