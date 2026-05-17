from django.shortcuts import render, get_object_or_404
from .models import IceCream

# def index(request):
#     return render(request, 'ice_shop/index.html')


def product_view(request):
    products = IceCream.objects.all()
    context = {'products': products}
    return render(request,
                  'ice_shop/index.html',
                  context)

def product_detail_view(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    context = {'ice_cream': ice_cream}
    return render(request, 'ice_shop/ice_detail.html', context)