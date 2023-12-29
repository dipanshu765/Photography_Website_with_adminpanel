from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if Contact.objects.filter(email=email).exists():
            messages.error(request, 'You have already submitted an enquiry...')
        else:
            enquiry = Contact.objects.create(name=name, email=email, message=message)
            enquiry.save()
            messages.success(request, 'Your query has been successfully submitted...')
            return redirect('contact:contact')

    return render(request, 'contact/contact.html')
