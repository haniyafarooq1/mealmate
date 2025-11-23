from django.shortcuts import render

def landing(request):
    # Shows the “User or Admin?” choice
    return render(request, 'home/landing.html')

