from django.shortcuts import render
from django.views import View
from home.models import *
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

context = dict()


def page_not_found_view(request, exception):
    return render(request, 'error.html', status=404)


def get_updated_details():
    userBasicDetails = get_object_or_404(UserBasicDetails)
    context['userBasicDetails'] = userBasicDetails
    languages = Languages.objects.all()
    context['languages'] = languages
    technicalSkills = TechnicalSkills.objects.all()
    context['technicalSkills'] = technicalSkills


class IndexView(View):
    def get(self, request):
        get_updated_details()
        workExperience = WorkExperiences.objects.all()
        context['workExperience'] = workExperience
        return render(request, 'index.html', context=context)


class History(View):
    def get(self, request):
        get_updated_details()
        education = Education.objects.all()
        context['education'] = education
        workExperience = WorkExperiences.objects.all()
        context['workExperience'] = workExperience
        return render(request, 'history.html', context=context)


class Contact(View):
    def get(self, request, *args, **kwargs):
        get_updated_details()
        technicalSkills = TechnicalSkills.objects.all()
        context['technicalSkills'] = technicalSkills
        submitButton = None
        context['submitButton'] = submitButton
        return render(request, 'contact.html', context=context)

    def post(self, request, *args, **kwargs):
        get_updated_details()
        data = formData()
        data.name = request.POST.get('your-name')
        if data.name:
            data.name = request.POST.get('your-name')
            data.email = request.POST.get('your-email')
            data.message = request.POST.get('your-message')
            data.save()

            submitButton = request.POST.get('submit')
            context['submitButton'] = submitButton
            subject = "you got an notification from " + data.name
            send_mail(subject, "Name: " + data.name + "\n" + "Email: "
                      + data.email + "\n" + "Message: " + data.message, data.email, ['exiall750@gmail.com'])
            return render(request, 'contact.html', context=context)

        return render(request, 'contact.html', context=context)


class AboutMe(View):
    def get(self, request, *args, **kwargs):
        get_updated_details()
        about = About.objects.all()
        context['about'] = about
        return render(request, 'about.html', context=context)


class Achievement(View):
    def get(self, request, *args, **kwargs):
        get_updated_details()
        achievement = Achievements.objects.all()
        context['achievement'] = achievement
        return render(request, 'achievement.html', context=context)


class CsBrideProgram(View):
    def get(self, request, *args, **kwargs):
        get_updated_details()
        csBridge = CsBrideProgramm.objects.all()
        context['csBridge'] = csBridge
        return render(request, 'csBridgeProgram.html', context=context)


class Project(View):
    def get(self, request, *args, **kwargs):
        get_updated_details()
        projects = Projects.objects.all()
        context['projects'] = projects
        return render(request, 'projects.html', context=context)
