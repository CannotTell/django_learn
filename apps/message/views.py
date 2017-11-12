from django.shortcuts import render
from .models import UserMessage
import pymysql
# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print(message.name)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email','')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.address = address
        user_message.email = email
        user_message.message = message

        user_message.save()

    return render(request, 'messageForm.html')
