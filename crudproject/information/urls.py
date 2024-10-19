from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list/', views.user_list),

    path('add/', views.add),
    path('success/', views.add_success),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.delete),
    path('view/<int:id>', views.view),

]