import logging

from django.http import HttpResponse
from django.shortcuts import render

from gyms.models import Gym, Trainer


logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Notes index view")


def gym_list(request):
    gyms = Gym.objects.order_by("-id")
    return render(request, "gyms/list_gyms.html", {"gyms": gyms})


def gym_view(request, gym_id):
    gym = Gym.objects.get(id=gym_id)
    return render(request, "gyms/card.html", {"gym": gym})


def trainer_list(request):
    trainers= Trainer.objects.order_by("-id")
    return render(request, "trainers/list_trainer.html", {"trainers": trainers})


def trainer_view(request, coach_id):
    trainer = Trainer.objects.get(id=coach_id)
    return render(request, "trainers/trainer_card.html", {"trainer": trainer})