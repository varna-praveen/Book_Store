from django.urls import path

from .views import BookList , BookDetailView , SearchResultListView , BookCheckout , add_to_cart , cart , \
        remove_from_cart

from . import views

urlpatterns = [
        path('', BookList.as_view(), name='booklist'),
        path('detail view/<int:pk>/', BookDetailView.as_view(), name='detail_view'),
        path('search/', SearchResultListView.as_view(), name='search'),
        path('checkout/<int:pk>/', BookCheckout.as_view(), name='checkout'),
        path('add_to_cart/<int:book_id>/', add_to_cart, name='add_to_cart'),
        path('cart/', cart, name='mycart'),
        path('remove_from_cart/<int:book_id>/', remove_from_cart, name='remove_from_cart'),
]