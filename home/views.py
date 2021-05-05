from django.http.response import Http404
from django.shortcuts import render
from .models import About, Facts, Skills, Resume_Education, Resume_Professional_Experience, Portfolio_Category,Portfolio_Itemes,Service,Testimonials, Social_links
# Create your views here.


def Home(request):
    about = About.objects.first()
    facts = Facts.objects.all()
    skills = Skills.objects.all()
    ResumeEducation = Resume_Education.objects.all()
    Resume_Professional_Experiences = Resume_Professional_Experience.objects.all()
    PortfolioItemes =Portfolio_Itemes.objects.all()
    Portfolio_Categoris = Portfolio_Category.objects.all()
    services = Service.objects.all()
    testimonials = Testimonials.objects.all()
    social_links = Social_links.objects.all()
    template_name = 'index.html'
    context = {
        'about': about,
        'facts':facts,
        'skills':skills,
        'Resume_Education':ResumeEducation,
        'Resume_Professional_Experiences':Resume_Professional_Experiences,
        'Portfolio_Category':Portfolio_Categoris,
        'Portfolio_Itemes':PortfolioItemes,
        'Services':services,
        'testimonials':testimonials,
        'social_links':social_links
    }
    return render(request, template_name, context)

def portoflio_detail_view(request, id):
    try:
        Portfolio_Iteme = Portfolio_Itemes.objects.get(id=id)
    except Portfolio_Itemes.DoesNotExist:
        raise Http404('project does not exist')
    return render(request, 'portfolio_detail.html', context={'Portfolio_Iteme': Portfolio_Iteme})