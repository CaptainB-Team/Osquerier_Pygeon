from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('querybuilder/', views.builderQueryView, name='querybuilder'),
    path('queryhist/', views.queryHistView.as_view(), name='queryhist'),
    path('querybuilder/custom/', views.customQueryView, name='custom_query_sender')
]
