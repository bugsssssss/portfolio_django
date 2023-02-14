from django.contrib import admin

from homeapp.models import Feedback, Portfolio, Service, Testimonial

# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name')

admin.site.register(Feedback)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Testimonial)
