
from django.shortcuts import render
from .factn import factn
def factorial(request):
	result=factn(5)
	return render(request, "index.html",{"param1":result})

