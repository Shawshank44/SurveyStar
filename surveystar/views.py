from django.shortcuts import render
from .forms import *
# Create your views here.

def Customer_view(request):
    if request.method == 'POST':
        fm = Customer_form(request.POST)

        if fm.is_valid():
            fm.save()
            return render(request , 'thankyou.htm')
    else:
        fm = Customer_form()

    return render(request, 'index.htm',{'form':fm})
