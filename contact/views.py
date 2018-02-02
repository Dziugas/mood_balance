from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
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
            email_address = form.cleaned_data['email']
            message = form.cleaned_data['message']
            email = EmailMessage('Message from the Mood Balance contact form', message, to=[settings.EMAIL_HOST_USER])
            email.send()
            return redirect('contact:contact')

#            subject = name
#            message = 'labas!'
#            from_email = settings.EMAIL_HOST_USER
#            recipient_list = [email]
#            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#        args = {'form':form, 'name':name, 'email':email_address}
#        return render(request, self.template_name, args)



