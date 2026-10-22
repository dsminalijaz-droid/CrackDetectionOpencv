

from cv2 import threshold
from django.shortcuts import render

from .models import crackdetect

from .controller import detect

import os
import cv2
from django.conf import settings
import numpy as np

def home(request):
    return render(request, 'crackdetectionapp/home.html')

def objective(request):
    return render(request, 'crackdetectionapp/objective.html')

def index(request):
        
        return render(request, 'crackdetectionapp/index.html')

def uploadImage(request):
        p=request.FILES['image'];
        pic=crackdetect(img= p)
        pic.save()
        users=crackdetect.objects.all()
        p=users[len(users)-1].img
        imag=p.url
        print("here is the url", imag)
        imag='.'+ imag
        alg=detect(imag)
        res=cv2.imwrite(r'media/output/s.jpg',alg)

        count_black = np.sum(alg == 0)
        count_white = np.sum(alg == 255)
        print('Number of white pixels : ', count_white)
        print('Number of black pixels : ', count_black)
        total_pixels = count_black + count_white
        crack_ratio = count_white / total_pixels
        crack_intensity = crack_ratio * 100
        print('Crack Intensity is :', crack_intensity)
        print("crack detected")
        
        

        return render(request, 'crackdetectionapp\index.html',{'img':imag, 'count_white':count_white})
        
        







#commands on cmd
#cd Documents/jango_app/env/Scripts
#cd crackdetection
#python manage.py runserver