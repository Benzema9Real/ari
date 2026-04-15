from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def main2(request):
    return render(request, 'main2.html')