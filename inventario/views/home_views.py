from django.shortcuts import redirect, render


def home_view(request):
    return render(request, 'inventario/home.html')


def inventario_redirect_view(request):
    return redirect('home')
