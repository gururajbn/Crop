import os
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from vid.settings import MEDIA_ROOT,BASE_DIR
import time
from .models import videos
from .forms import videoform
from django.views.generic import View
from django.core import serializers
# Create your views here.

def crop_file(f):
	name=str(int(round(time.time() * 1000)))+"_"+str(f._get_name())
	fd = open('%s/original/%s' % (MEDIA_ROOT,name), 'wb')
	for chunk in f.chunks():
		fd.write(chunk)
	fd.close()
	return str(name)

class videos(View):

	def get(self,request):
		from .models import videos
		file_list= serializers.serialize("json", videos.objects.all())
		return HttpResponse(file_list,content_type="application/json")

	def post(self,request):
		x=request.POST["x"]
		y=request.POST["y"]
		width= request.POST["width"]
		height= request.POST["height"]
		filename= str(request.FILES["file"]._get_name())
		form= videoform(request.POST)
		if form.is_valid():
			vid=form.save(commit=False)
			file_name=crop_file(request.FILES["file"])
			cmd="ffmpeg -i "+MEDIA_ROOT+"/original/"+file_name+" -strict -2 -filter:v \"crop="+width+":"+height+":"+x+":"+y+"\" "+MEDIA_ROOT+"/crop/"+file_name
			print cmd
			os.system(cmd)
			vid.originalfile="/media/original/"+file_name
			vid.cropedfile= "/media/crop/"+file_name
			vid.title= filename
			vid.save()
			return HttpResponse(json.dumps({
				"status":"OK",
				"message":"uploaded"
				}))
		else:
			return HttpResponse(json.dumps({
				"status":"FAIL",
				"message":"post request is not valid"
				}))	
