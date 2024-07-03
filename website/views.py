from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting


def welcome(request):
    return render(request, template_name="website/welcome.html", context={"num_meetings": Meeting.objects.count()})


def about(request):
    return HttpResponse('This is my about me page!')
