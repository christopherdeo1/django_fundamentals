from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from django.forms import modelform_factory


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, template_name="website.html", context={"meetings": meeting})


def rooms_list(request):
    return render(request, template_name='meetings/rooms_list.html', context={"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request):
    if request.method == "POST":
        # form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, template_name='meetings/new.html', context={'form': form})


def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect(to='details', args=id)
        else:
            form = MeetingForm(instance=meeting)
    return render(request, template_name="meetings/edit")


def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect('welcome')
    else:
        return render(request, template_name='meetings/confirm_delete.html', context={'meeting': meeting})
