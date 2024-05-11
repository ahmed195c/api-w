import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
# Create your views here.

def index(request):
    return HttpResponse("appnml/lyaout.html <h1> gg </h1> <button> btn </button> <a href='homepage'> link </a>")


def homepage(request):
    return render(request, "appnml/lyaout.html")

@csrf_exempt
def saveuser(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST request requierd"}, status=400)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        userNames = data.get("username", "")
        userEmails = data.get('userpassword', "")

        user = User(userName=userNames,userEmail=userEmails)

        user.save()
        return JsonResponse({"message": "Email sent successfully."}, status=201)
    
@csrf_exempt
def loadusers(request):
    if request.method == 'GET':
        user = User.objects.all()
        return JsonResponse([use.serilize() for use in user], safe=False )