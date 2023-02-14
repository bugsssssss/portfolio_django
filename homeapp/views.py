from tkinter.tix import Form
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView


data = {
    'bio': 'I am an experienced software engineer and have gained a strong reputation in the area. I have worked on a variety of projects, both in the public and private sector, and have gained a wealth of experience and knowledge. I am a motivated individual who is always looking to improve my skills and knowledge, and I am confident that I can make a positive contribution to any organisation.'
}

from homeapp.forms import FeedbackForm
from homeapp.models import Feedback, Portfolio, Service, Testimonial

class HomeView(CreateView):
    form_class = FeedbackForm
    template_name  = 'index.html' 
    success_url = '#'

   
        

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['feedbacks'] = Feedback.objects.all()
        context['services'] = Service.objects.all()
        context['portfolio'] = Portfolio.objects.all()
        context['data'] = data
        context['testimonials'] = Testimonial.objects.all()
        return context 


    


# def inputuserinfo(response):
#     if response.method == "POST":
#         form = FeedbackForm(response.POST)
#         if form.is_valid:
#             form.save()
#         return redirect('home')
#     else:
#         form = FeedbackForm()
#     return render(response, 'index.html', {'form' : form })
