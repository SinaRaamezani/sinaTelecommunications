from django.shortcuts import render
from accounts.models import CustomUser
from .forms import UserSearchForm

def user_list(request):
    ls_user = CustomUser.objects.all()
    form = UserSearchForm()
    return render(request , 'home/main.html' , context={"ls_user":ls_user , "forms" : form} )

def search_user(request):
    search = request.GET.get("search")
    ls_user = CustomUser.objects.filter(username__icontains=search)

    if ls_user.exists() == True :
        return render(request, "home/main.html", {"ls_user": ls_user})
    else:
        ls_user = CustomUser.objects.filter(phone_number1__icontains=search)
        return render(request, "home/main.html", {"ls_user": ls_user})











