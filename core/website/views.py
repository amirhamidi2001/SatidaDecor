from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from website.forms import ContactForm

class IndexView(TemplateView):
    template_name = "website/index.html"


class ContactView(FormView):
    """Handles display and processing of the contact form."""

    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:contact")

    def form_valid(self, form):
        """If the form is valid, save it and show a success message."""
        form.save()
        messages.success(self.request, "پیام شما با موفقیت ارسال شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, show an error message."""
        messages.error(self.request, "ارسال پیام ناموفق بود.")
        return super().form_invalid(form)
