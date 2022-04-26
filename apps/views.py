from django.shortcuts import render, redirect
from .models import Userurls
import random
# Create your views here.


def index(request):
    return render(request, 'index.html')


def stored(request):
    input_url = request.POST.get('input_url', 'NULL')

    a1 = random.randint(0, 9)
    a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    s1 = str(a1)
    s2 = str(a2)
    s3 = str(a3)
    s4 = str(a4)
    fid = s1+s2+s3+s4
    fid = int(fid)

    storing_url = Userurls(inputurl=input_url, urlint=fid)
    storing_url.save()


    b1 = 'tiny.pythonanywhere.com/'

    fid = str(fid)
    reduced_url = b1 + fid
    return render(request, 'stored.html', {'reduced_url': reduced_url})


def work(request, id):
    url_obj = Userurls.objects.get(urlint=id)
    stored_url = url_obj.inputurl
    return redirect(stored_url)

    