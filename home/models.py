from django.db import models

# Create your models here.

class WorkExperiences(models.Model):
    title = models.TextField()
    company_name = models.CharField(max_length=200)
    details = models.TextField()
    short_details = models.TextField(default=None, null=True, blank=True)
    skills = models.TextField()
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    exp_bg_img = models.ImageField(upload_to="ExpBackground/", default=None, blank=True, null=True)
    img = models.ImageField(upload_to="ExpImg/", default=None, blank=True, null=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.TextField(default=None, blank=True, null=True)
    university_name = models.CharField(max_length=200)
    cgpa = models.FloatField(default=None, blank=True, null=True)
    cgpa_outOf = models.IntegerField(default=None, blank=True, null=True)
    percentage = models.FloatField(default=None, blank=True, null=True)
    percentage_outOf = models.IntegerField(default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    start_date = models.DateField(default=None,blank=True,null=True)
    end_date = models.DateField(default=None,blank=True,null=True)

    def __str__(self):
        return self.title

class Projects(models.Model):
    title = models.TextField()
    description = models.TextField(max_length=5001)
    link = models.CharField(max_length=65535)
    link_name = models.TextField(max_length=100 ,default=None ,null=True ,blank=True)
    link_report = models.TextField(default=None, null=True, blank=True, max_length=65535)
    link_report_name = models.TextField(max_length=100, default=None, null=True, blank=True)
    start_date = models.DateField(default=None,blank=True,null=True)
    end_date = models.DateField(default=None,blank=True,null=True)
    bg_img = models.ImageField(upload_to="background/", default=None, blank=True, null=True)
    img = models.ImageField(upload_to="ProjectImg/", default=None, blank=True, null=True)

    # def __str__(self):
    #     return self.title

class TechnicalSkills(models.Model):
    name = models.TextField(max_length=100)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class UserBasicDetails(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    bio = models.TextField(max_length=250)
    country = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    age = models.IntegerField()
    email = models.EmailField()
    phone_number = models.IntegerField()
    technical = models.ForeignKey(TechnicalSkills, on_delete=models.CASCADE, related_name="technical")
    other_skills = models.TextField()
    languages = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name="languages")
    profile_image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.name

class formData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    def __str__(self):
        return self.name

class About(models.Model):
    about = models.TextField(max_length=10000, default=None, null=True, blank=True)
    aboutImg = models.ImageField(upload_to="profile/", default=None, null=True, blank=True)

class Achievements(models.Model):
    title = models.TextField(max_length=500)
    university = models.TextField(max_length=100)
    achievement_description = models.TextField(max_length=1000, default=None, null=True, blank=True)
    year = models.DateField(default=None, null=True, blank=True)

class CsBrideProgramm(models.Model):
    title = models.TextField(max_length=500, default=None, blank=True, null=True)
    university = models.TextField(max_length=100, default=None, blank=True, null=True)
    courseInfo = models.TextField(max_length=10000, default=None, blank=True, null=True)





