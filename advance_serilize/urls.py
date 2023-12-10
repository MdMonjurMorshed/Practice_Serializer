from django.urls import path,include
from advance_serilize.views import CreateFist
urlpatterns_v1=[
    path('create-first',CreateFist.as_view(),name='create_first')

]

