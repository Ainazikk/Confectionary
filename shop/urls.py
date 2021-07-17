from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductList

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.product_list,name='products_by_category'),
    path('products/', views.product_list, name='products'),
    path('about_us/', views.about_us, name='about_us'),
    path('blog/', views.blog, name='blog'),
    path('blog/blog_details/', views.blog_details, name='blog_details'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('products/', ProductList.as_view()),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/', views.category_list, name='categories'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



