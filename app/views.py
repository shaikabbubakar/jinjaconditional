from django.shortcuts import render

# Create your views here.
def conditional(request):
    return render(request,'conditional.html',context={'a':20,'b':30,'c':25})