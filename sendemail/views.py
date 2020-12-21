from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import EmailForm

def email_view(request):
    if request.method == 'GET':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            form.save()
            try:
                send_mail(subject, message, from_email, ['mppatterson84@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context = {
        'title': 'Contact Us',
        'contact_active': 'active',
        'contact_active_link': '#',
        'contact_active_sr': '<span class="sr-only">(current)</span>',
        'form': form,
        'reCAPTCHA_site_key_v2': os.environ['RECAPTCHA_SITE_KEY_V2'],
    }
    return render(request, 'sendemail/email.html', context)


class SuccessPageView(TemplateView):
    template_name = 'sendemail/success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Success'
        return context