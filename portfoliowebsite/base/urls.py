from django.urls import path
# from . import views 
from .views import *

urlpatterns = [
    path('', homePage, name='home'),
    path('project/<uuid:pk>', projectPage, name='project'),
    path('pbiProject', pbiProjectPage, name='pbiProject'),
    path('demo', AjaxHandlerView.as_view() ),
]
