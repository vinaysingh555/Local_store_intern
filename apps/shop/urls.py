from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductCreateView, Login, Signup, Product_list, ProfileView, ProductDetailView, AddToCartView, \
    CartView, remove_from_cart, paymenthandler, PreorderView, PreOrderListView, logout_view, increase_quantity, \
    decrease_quantity

urlpatterns = [
    path('', Product_list.as_view(), name='product_list'),

    path('register/', Signup.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='user_profile'),


    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create-product/', ProductCreateView.as_view(), name='create_product'),

    # Cart Related Paths
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),

    path('cart/increase/<int:pk>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),

    path('preorder/', PreorderView.as_view(), name='preorder'),
    path('preorder_list/', PreOrderListView.as_view(), name='preorder-list'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)