
from django.http import HttpResponse


def index(request):
    return HttpResponse("bad request")

def music(request):
    return HttpResponse('Go to favorite artists list by typing music/artist(1,2,or 3)')

def artist1(request):
    return HttpResponse('A')

def artist2(request):
    return HttpResponse('B')

def artist3(request):
    return HttpResponse('C')