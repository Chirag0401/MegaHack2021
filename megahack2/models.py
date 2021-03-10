from django.db import models

# Create your models here.
class contactForm(models.Model):   
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    query=models.CharField(max_length=500,blank=False)
    mobile_number=models.BigIntegerField(null=True,blank=True)
    message=models.TextField(blank=False)

    class Meta:
        verbose_name='contactForm'
        verbose_name_plural='contactForms'

    def __str__(self):
        return self.name

class gallery(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='media/img/gallery',blank=False)

    class Meta:
        verbose_name="gallery"
        verbose_name_plural="gallery"

    def __str__(self):
        return self.title 

class youtube_link(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="youtube_link"
        verbose_name_plural="youtube_links"

    def __str__(self):
        return self.title

class speaker(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    sub_title=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='media/img/speaker',null=True,blank=True)
    email_id=models.CharField(max_length=200,null=True,blank=True) 
    instagram_id=models.CharField(max_length=200,null=True,blank=True)
    linkedIn_id=models.CharField(max_length=200,null=True,blank=True) 

    class Meta:
        verbose_name="speaker"
        verbose_name_plural="speakers"

    def __str__(self):
        return self.name

class sponsor(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='media/img/sponsor',null=True)
    website_link=models.CharField(max_length=200,blank=True,null=True) 

    class Meta:
        verbose_name="sponsor"
        verbose_name_plural="sponsors"

    def __str__(self):
        return self.title
                
class code_of_conduct(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="code_of_conduct"
        verbose_name_plural="code_of_conducts"

    def __str__(self):
        return self.name

class view_poster(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="view_poster"
        verbose_name_plural="view_poster"

    def __str__(self):
        return self.name

class rule(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="rule"
        verbose_name_plural="rules"

    def __str__(self):
        return self.name

class registration_one(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="registration_one"
        verbose_name_plural="registration_one"

    def __str__(self):
        return self.name

class registration_two(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="registration_two"
        verbose_name_plural="registration_two"

    def __str__(self):
        return self.name

class registration_three(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="registration_three"
        verbose_name_plural="registration_three"

    def __str__(self):
        return self.name

class registration_four(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="registration_four"
        verbose_name_plural="registration_four"

    def __str__(self):
        return self.name

class registration_five(models.Model):
    available=models.BooleanField(default=True)
    name=models.CharField(max_length=100,blank=False)
    link=models.CharField(max_length=500,blank=False)

    class Meta:
        verbose_name="registration_five"
        verbose_name_plural="registration_five"

    def __str__(self):
        return self.name

class step_one(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(blank=False)

    class Meta:
        verbose_name="step_one"
        verbose_name_plural="step_one"

    def __str__(self):
        return self.title    

class step_two(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(blank=False)

    class Meta:
        verbose_name="step_two"
        verbose_name_plural="step_two"

    def __str__(self):
        return self.title    

class step_three(models.Model):
    available=models.BooleanField(default=True)
    title=models.CharField(max_length=100,blank=False)
    description=models.TextField(blank=False)

    class Meta:
        verbose_name="step_three"
        verbose_name_plural="step_three"

    def __str__(self):
        return self.title                    