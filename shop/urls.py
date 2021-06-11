from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('category/<slug:category_slug>/', views.product_list,name='product_list'),
    # path('<int:id>/<slug:slug>/', views.product_detail,name='blog_details'),
    path('about/', views.about, name='about'),
    # path('product_details/', views.product_details, name='product_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
