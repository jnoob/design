from django.shortcuts import render
from django.http import HttpResponse
from pastebin.models import PasteContent
import json
import uuid
import urllib.parse
import time


def pastebin_handle(request, link=None):
   if(request.method == 'GET'):
       return load(request, link)
   else:
       return generate(request)


# Create your views here.
def generate(request):
  data = json.load(request.body)
  data['link'] = uuid.uuid4()
  PasteContent.objects.create(**data)
  response = {
      'succeed': True,
      'link': data['link']
  }
  return HttpResponse(json.dumps(response), content_type='application/json')


def load(request, link):
    decoded_link = urllib.parse.unquote(link)
    content = PasteContent.objects.get(link=decoded_link)
    response = {}
    if content:
        response['succeed'] = True
        response['content'] = content.content
        response['expire_at'] = content.expire_at
    else:
        response['succeed'] = False
        response['content'] = '--NOT-FOUND--'
        response['expire_at'] = time.time()
    return HttpResponse(json.dumps(response), content_type='application/json')

