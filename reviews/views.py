from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Back1

def home(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        if username1 == "":
            return render(request, 'home.html',{'has_error':True})
        if len(username1)>20:
            return render(request, 'home.html',{'len_error':True})
        
        if email1 == "":
            return render(request, 'home.html',{'email_error':True})
        if password1 == "":
            return render(request, 'home.html',{'password_error':True})
        #b = False
        #for i in Back1.objects.filter('username'):
        #    if i == username1:
        #        b = True
        #            
        #    
        #if b:
           # return render(request, 'home.html',{'username_exit_error':True})
        a = Back1()
        a.username = password1
        a.email = email1
        a.password = password1
        a.save()
        return HttpResponseRedirect('thankyou')
    return render(request, 'home.html',{'has_error':False,
                                        'password_error':False,
                                        'len_error':False,
                                        'email_error':False})


def thankyou(request):
    return render(request, 'thankyou.html')