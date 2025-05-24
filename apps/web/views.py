from django.shortcuts import render
import datetime

# Create your views here.
def index(request): 
    fecha_actual = datetime.datetime.now()
    return render(request,'index.html',{'fecha_actual':fecha_actual}) 