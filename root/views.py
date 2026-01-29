from django.shortcuts import redirect

def root_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return redirect('/login')
