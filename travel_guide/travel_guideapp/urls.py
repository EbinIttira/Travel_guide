from django.urls import path
from . import views
app_name='travel_guideapp'
urlpatterns= [
     path('',views.home,name='home'),
     path('addplace/',views.addplace,name='addplace'),
     path('home/<int:place_id>/',views.placedetail,name='placedetail'),
     path('update/<int:place_id>/',views.update,name='update'),
]