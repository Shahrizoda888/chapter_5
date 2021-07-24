from django.urls import path
from blog import views
app_name='blog'




urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('order_post/', views.order_post,name='order_post'),
]
