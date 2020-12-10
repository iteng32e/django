from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('product_list/', views.ProductLisView.as_view(), name="product_list_url"),
    path('product_detail/<int:id>', views.product_detail_def, name="product_detail_url"),

    path('payment_list/', views.PaymentListView.as_view(), name="payment_list_url"),
    path('payment_detail/<int:id>', views.payment_detail_def, name="payment_detail_url"),

]
