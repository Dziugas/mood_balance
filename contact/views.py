from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from contact.forms import ContactForm

class ContactView(TemplateView):
    template_name = 'contact/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            return redirect('contact:contact')

        args = {'form':form, 'name':name, 'email':email}
        return render(request, self.template_name, args)


        subject = 'pimpadryla'
        message = 'Nuejai i kontaktu forma, ane??'
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER]

        send_mail(subject, message, from_email, to_list, fail_silently=True)
