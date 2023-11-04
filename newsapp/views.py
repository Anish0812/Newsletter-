from django.shortcuts import render,redirect
from requests import *

def pnf(request,exception):
    return redirect("home")

def about(request):
    return render(request,"about.html")

def home(request):
    try:
        a1="https://newsapi.org/v2/top-headlines"
        a2="?country=in"
        a3="&apiKey=fc61421bebad40319262f6bbd6b377b3"
        wa=a1+a2+a3
        res=get(wa)
        data=res.json()
        info=data["articles"]
        msg=info
        return render(request,"home.html",{"msg":msg})
    except Exception as e:
        return render(request,"home.html0",{"msg":str(e)})
