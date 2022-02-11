import logging

from django.http import HttpResponse
from django.shortcuts import render

from gyms.models import Gym


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Notes index view")


def gym_list(request):
    gyms = Gym.objects.order_by("-id")
    return render(request, "gyms/list.html", {"gyms": gyms})


def gym_view(request, gym_id):
    gym = Gym.objects.get(id=gym_id)
    return render(request, "gyms/card.html", {"gym": gym})
