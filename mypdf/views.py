from django.shortcuts import render,get_object_or_404 
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import MyPdf

# Create your views here.

class MyPdfListView(ListView):
    model = MyPdf
    template_name = 'mypdf/main.html'

def mypdf_render_pdf_view(request, *args, **kwargs):

    pk = kwargs.get('pk')
    mypdf = get_object_or_404(MyPdf, pk=pk)
    template_path = 'mypdf/pdf.html'
    context = {'mypdf': mypdf}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if downloads:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf 
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    

def render_pdf_view(request):
    template_path = 'mypdf/pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if downloads:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf 
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response