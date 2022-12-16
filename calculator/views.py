from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "input.html")

def addition(request):
    num1 = request.POST['num1'] #100
    num2 = request.POST['num2'] #200

    if num1.isdigit() and num2.isdigit():
        a=int(num1)
        b=int(num2)
        res=a+b #300

        return render(request, "result.html", {"result":res})
    else:
        res="Only digits are allowed"
        return render(request, "request.html", {"result":res})

def substraction(request):
    num1 = request.POST['num1'] #100
    num2 = request.POST['num2'] #200

    if num1.isdigit() and num2.isdigit():
        a=int(num1)
        b=int(num2)
        res=a-b #300

        return render(request, "result.html", {"result":res})
    else:
        res="Only digits are allowed"
        return render(request, "request.html", {"result":res})

def multiplication(request):
    num1 = request.POST['num1'] #100
    num2 = request.POST['num2'] #200

    if num1.isdigit() and num2.isdigit():
        a=int(num1)
        b=int(num2)
        res=a*b #300

        return render(request, "result.html", {"result":res})
    else:
        res="Only digits are allowed"
        return render(request, "request.html", {"result":res})

def division(request):
    num1 = request.POST['num1'] #100
    num2 = request.POST['num2'] #200

    if num1.isdigit() and num2.isdigit():
        a=int(num1)
        b=int(num2)
        res=a/b #300

        return render(request, "result.html", {"result":res})
    else:
        res="Only digits are allowed"
        return render(request, "request.html", {"result":res})