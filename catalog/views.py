from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'main/main.html')


def contacts(request):
    return render(request, 'main/contacts.html')
