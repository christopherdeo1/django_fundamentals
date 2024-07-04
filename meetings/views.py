from django.shortcuts import render, get_object_or_404
from meetings.models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, template_name="website.html", context={"meetings": meeting})


def rooms_list(request):
    return render(request, template_name='meetings/rooms_list.html', context={"rooms": Room.objects.all()})
