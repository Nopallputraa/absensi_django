from django.http import HttpResponse

def profile_view(request):
    return HttpResponse("Ini halaman profil user (accounts app).")