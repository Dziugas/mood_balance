from django.views.generic import TemplateView
from contact.forms import ContactForm
from django.shortcuts import render, redirect


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
