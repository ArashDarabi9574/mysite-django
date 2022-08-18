from django.shortcuts import render
from django.http import HttpResponse
from website.forms import ContactForm
def index_view(response):
    return render(response, 'website/index.html')


def about_view(response):
    return render(response, 'website/about.html')


def contact_view(response):
    if response.method == 'POST':
        form = ContactForm(response.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(response, 'website/contact.html')


def elemntry_view(response):
    return render(response, 'website/elements.html')
