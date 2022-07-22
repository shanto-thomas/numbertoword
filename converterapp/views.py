from django.shortcuts import render
from num2words import num2words
# Create your views here.
import re


def landingpage(request):
    return render(request, "landingpage.html")


def converter(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        if not re.match('^[1-9]\d*$', str(number)):
            return render(request, "landingpage.html", {"result": "INVALID NUMBER"})

        print(num2words(int(number)))

        return render(request, "landingpage.html", {"result": num2words(int(number)).upper()})

    return render(request, "landingpage.html")
