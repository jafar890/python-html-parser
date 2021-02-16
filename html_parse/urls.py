from django.urls import path

from html_parse import views

app_name = 'html_parse'
urlpatterns = [
    path('as/', views.ParseView.as_view(),name='parser'),
    path('show/', views.ShowParseView.as_view(),name='show')
]