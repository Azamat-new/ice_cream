from django.shortcuts import render, get_object_or_404, redirect
from .models import IceCream
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'ice_shop/signup.html', {'form': form})



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
