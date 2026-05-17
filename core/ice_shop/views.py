from django.shortcuts import render


def index(request):
    return render(request, 'ice_shop/index.html')
