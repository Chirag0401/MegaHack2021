from django.contrib import admin
from .models import contactForm,step_one,step_two,step_three, sponsor, speaker, gallery, youtube_link, code_of_conduct, rule, view_poster ,registration_five, registration_one, registration_two, registration_three, registration_four
# Register your models here.
class contactFormAdmin(admin.ModelAdmin):
    list_display =[ 'name','email','mobile_number']


admin.site.register(contactForm, contactFormAdmin)
admin.site.register(sponsor)
admin.site.register(speaker)
admin.site.register(gallery)
admin.site.register(youtube_link)
admin.site.register(code_of_conduct)
admin.site.register(rule)
admin.site.register(view_poster)
admin.site.register(registration_one)
admin.site.register(registration_two)
admin.site.register(registration_three)
admin.site.register(registration_four)
admin.site.register(registration_five)
admin.site.register(step_one)
admin.site.register(step_two)
admin.site.register(step_three)
