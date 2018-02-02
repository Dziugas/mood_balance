from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
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
            email = EmailMessage('Hello', ('Whats up???, my name is %s' %name), to=[email_address])
            email.send()
            return redirect('contact:contact')

#            subject = name
#            message = 'labas!'
#            from_email = settings.EMAIL_HOST_USER
#            recipient_list = [email]
#            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

#        args = {'form':form, 'name':name, 'email':email_address}
#        return render(request, self.template_name, args)



