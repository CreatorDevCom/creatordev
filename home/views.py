from django.shortcuts import render

# Create your views here.
def homeRenderer(request):
  return render(request , "index.html")


# Uplaods
def upload(request):
  return render(request,'upload/index.html')