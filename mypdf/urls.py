from django.urls import path
from . import views
from .views import render_pdf_view, MyPdfListView, mypdf_render_pdf_view

app_name = 'mypdf'

urlpatterns = [
    path('', MyPdfListView.as_view(),name ='mypdf-list-view'),
    path('test/',render_pdf_view,name ='test-view'),
    path('pdf/<pk>/',mypdf_render_pdf_view,name ='mypdf-pdf-view'),

]