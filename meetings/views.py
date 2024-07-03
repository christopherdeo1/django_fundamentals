from django.http import HttpResponse
from django.shortcuts import render
from models.meetings import Meeting


# Create your views here.


def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, template_name="website.html", context={"meeting": meeting})
