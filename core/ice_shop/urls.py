from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.product_view, name='index'),
    path('product/<int:pk>/', views.product_detail_view, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
