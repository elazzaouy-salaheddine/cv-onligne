from django.contrib import admin
from .models import About,Facts, Skills, Resume_Education,Resume_Professional_Experience,Portfolio_Category,Portfolio_Itemes,Testimonials,Contact,Social_links, Service
# Register your models here.

class About_Admin(admin.ModelAdmin):
    list_display = ['job_title','age','birthday','website','degree','phone','phEmailone']
admin.site.register(About,About_Admin)


class Facts_Admin(admin.ModelAdmin):
    list_display=['number','title']
admin.site.register(Facts,Facts_Admin)

class Skills_Admin(admin.ModelAdmin):
    list_display = ['title','valeu']
admin.site.register(Skills,Skills_Admin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree','duration','institute_name']
admin.site.register(Resume_Education,EducationAdmin)


class ResumeProfessionalExperienceAdmin(admin.ModelAdmin):
    list_display = ['title','duration','company']
admin.site.register(Resume_Professional_Experience,ResumeProfessionalExperienceAdmin)

admin.site.register(Portfolio_Category)


class Portfolio_Itemes_admin(admin.ModelAdmin):
    list_display=['client','category']
    list_filter = ['category']
admin.site.register(Portfolio_Itemes,Portfolio_Itemes_admin)


admin.site.register(Service)

class TestimonialsAdmin(admin.ModelAdmin):
    list_display =['client_name','job_client']

admin.site.register(Testimonials,TestimonialsAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display=['email','phone_number','location']
admin.site.register(Contact,ContactAdmin)


class SocialAdmin(admin.ModelAdmin):
    list_display = ['social_name','social_link']
admin.site.register(Social_links,SocialAdmin)
