import os
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from vid.settings import MEDIA_ROOT,BASE_DIR
import time
# Create your views here.
def crop_file(f):
	name=str(int(round(time.time() * 1000)))+"_"+str(f._get_name())
	fd = open('%s/%s' % (MEDIA_ROOT,name), 'wb')
	for chunk in f.chunks():
		fd.write(chunk)
	fd.close()
	return str(name)

@csrf_exempt
def cropIt(request):
	height= request.POST['height']
	witdth= request.POST['width']
	x = request.POST['x']
	y = request.POST['y']
	file_path=crop_file(request.FILES['file'])
	cmd="ffmpeg -i "+MEDIA_ROOT+"/"+file_path+" -strict -2 -filter:v \"crop="+witdth+":"+height+":"+x+":"+y+"\" static/"+file_path
	print cmd
	os.system(cmd)
	return HttpResponse(json.dumps({
		"status":"OK",
		"file":"localhost:8000/static/"+file_path
		}))

def getVideos(request):
	file_list=os.listdir(BASE_DIR+"/static")

	return render(request,"list.html",{
		'objects':file_list
		})
