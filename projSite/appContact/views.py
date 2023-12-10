from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'tmp_contact/contact.html')