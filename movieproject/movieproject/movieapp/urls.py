from django.urls import path
from . import views


urlpatterns = [
   path('',views.demo,name='demo'),
   path('sav/<int:movie_id>/',views.demo1,name='save'),
   path('update/<int:id>/',views.UPDATE,name='update'),
#    above step after that creat forms.py in app
   path('delete/<int:id>/',views.DELETE,name='delete'),

   path('add',views.ADD,name='add'),
#    aft this go to views and def it

]
