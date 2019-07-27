from django.shortcuts import render
from django.contrib.auth.models import User


def signupfunc(request):
    if request.method == 'POST':
        username_post = request.POST['username']
        password_post = request.POST['password']
        try:
            User.objects.get(username=username_post)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username_post, 'mail@example.com', password_post)
            return render(request, 'signup.html', {'some': 100})

    return render(request, 'signup.html', {'some': 100})
