import os

import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from daily import models
from daily.form import UploadFileForm
from daily.form import handle_uploaded_file
from django.views.decorators.csrf import csrf_exempt
from djangoProject.settings import base_settings

# Create your views here.
from djangoProject import settings


def index(request):
    event = models.Event.objects.filter(event_id=16)
    user = models.UserInfo.objects.filter(user_id=1)
    response = HttpResponse()
    o = None
    for i in event:
        o = i
    url = r"http://127.0.0.1:8080/api/user/loginByFace"
    data = dict(
        userId=1
    )
    try:
        ppp = requests.post(url, data)
    except:
        print("net err")
    return HttpResponse("Hello, 7th world welcome for You." + o.user.user_name)



# Imaginary function to handle an uploaded file.

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        data = request.FILES['file']  # or self.files['image'] in your form
        apath = base_settings.MEDIA_ROOT
        path = default_storage.save(apath+'tmp/somename.jpg', ContentFile(data.read()))
        print(path)
        return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
