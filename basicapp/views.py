from django.shortcuts import render
from django.contrib import messages
from . import forms
from . import version_checker

# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    checker = version_checker.Solution()
    sol = ""

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            v1 = form.cleaned_data['version1']
            v2 = form.cleaned_data['version2']
            sol = checker.VersionChecker(v1,v2)
            messages.success(request, sol)



    return render(request,'basicapp/form_page.html',{'form':form})

