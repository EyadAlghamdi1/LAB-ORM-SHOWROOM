from django.urls import path 
from . import views

app_name = "cars"

urlpatterns = [
    path('all/',views.all_cars_view,name="all_cars_view"),
    path('add/',views.add_car_view,name="add_car_view"),
    path('add/color/',views.add_color_view,name="add_color_view"),
    path('delete/color/<int:color_id>',views.delete_color_view,name="delete_color_view"),
    path('update/<int:car_id>',views.update_view,name="update_view"),
    path('detail/<car_id>',views.detail_view,name="detail_view"),
    path('delete/<car_id>',views.delete_view,name="delete_view"),
    path('reviews/add/<car_id>',views.add_review_view,name="add_review_view"),
]