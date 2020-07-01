from django.urls import path
from . import views

app_name = 'merchant'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('item/<slug:slug>/', views.ItemDetailView.as_view(), name="item-detail"),
    path('order-summary', views.OrderSummaryView.as_view(), name="order-summary"),
    path('add-to-order/<slug>/', views.add_to_order, name="add-to-order"),
    path('remove-from-cart/<slug>/', views.remove_item_from_cart, name="remove-from-cart"),
    path('<user>/finalize/', views.FinalizingView.as_view(), name='finalize'),
    path('registeration/', views.RegisterationFormView.as_view(), name='registration'),
    path('order-confirm/', views.OrderConfirmView.as_view(), name="order-confirm"),
]