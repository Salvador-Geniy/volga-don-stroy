from django.shortcuts import render


def main_page(request):
    user = request.user
    return render(request, 'index.html', context={'user': user})
