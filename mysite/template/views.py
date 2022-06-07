from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def echo(request: HttpRequest):
    template = loader.get_template('template/echo.html')
    context = {
        'requestGET': request.GET,
        'requestPOST': request.POST,
        'requestHeaders': request.META
    }
    return HttpResponse(template.render(context, request))
