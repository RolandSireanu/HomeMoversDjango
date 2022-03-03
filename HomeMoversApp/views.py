from distutils.log import error
import re
from wsgiref.validate import validator
from xml.dom import ValidationErr
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context
from django.core.mail import send_mail
from .forms import MessageModelForm
import ipdb

def home(req):
    return render(req, "HomeMoversApp/index.html")  

def about(req):
    return render(req, "HomeMoversApp/about.html")



def contact(req):
    
    form = MessageModelForm(req.POST or None);
    thankyou_message = ""
    if form.is_valid() and req.method == "POST":        
        form.save(commit=True)         
        send_mail("HomeMovers contact", "Thank you for contacting us " + form.cleaned_data["first_name"], "sireanu.roland@gmail.com", 
        ["sireanu.roland@gmail.com"], fail_silently=False)
        thankyou_message = "Your message has been received !"
        form = MessageModelForm(None);
    else:        
        for invalidField in form.errors.keys():
            form.setFieldInvalid(invalidField);
    
    return render(req, "HomeMoversApp/contact.html", context={"form":form, "thankyou_message": thankyou_message})

def news(req):
    return render(req, "HomeMoversApp/news.html")

def services(req):
    return render(req, "HomeMoversApp/services.html")