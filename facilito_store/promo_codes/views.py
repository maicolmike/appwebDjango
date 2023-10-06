from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def validate(request):
    return JsonResponse({
        'name':'Maicol',
        'job':'Facilito'
    })