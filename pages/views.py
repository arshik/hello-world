# import imp
from django.shortcuts import render
from django.http import HttpResponse


def homePageView(response):
    return HttpResponse("<h1>Hello!!</h1>")


# Create your views here.
