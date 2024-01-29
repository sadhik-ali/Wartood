from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField

# Create your models here.


class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    image = models.ImageField(upload_to="photos")
    title = models.CharField(max_length=100)
    paragraph = models.TextField()
    description = models.TextField()

    ICON_CHOICES = (
        ("dlicon design_compass", "Design Compass Icon"),
        ("dlicon furniture_light", "Furniture Light Icon"),
        ("dlicon design_design", "Design Design Icon"),
        ("dlicon tech-2_firewall", "Firewall Icon"),
        ("dlicon furniture_mixer", "Furniture Mixer Icon"),
        ("dlicon transportation_bus", "Transportation Bus Icon"),
    )
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))

    admin_photo.short_description = "Image"
    admin_photo.allow_tags = True

    def __str__(self):
        return self.title

    def get_images(self):
        return ServiceImage.objects.filter(project=self)


class EnquiryForm(models.Model):
    Product = models.CharField(max_length=100)
    Name = models.EmailField()
    Phone = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Product


class ServiceImage(models.Model):
    project = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="upload/project-img")

    def __str__(self):
        return self.image.name


class Update(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="upload/project-img")
    service = models.CharField(max_length=100)
    title = models.CharField(max_length=220)
    description = HTMLField()

    def __str__(self):
        return self.service

    def display_image(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))

    display_image.short_description = "Image"
    display_image.allow_tags = True


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=150)
    # name=models.CharField(max_length=50)
    image = models.ImageField(upload_to="upload/project-img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # subtitle=models.TextField()

    def __str__(self):
        return self.title


class TandurStone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/project-img")
    description = models.TextField()

    def __str__(self):
        return self.name

    def tandur_image(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))

    tandur_image.short_description = "Image"
    tandur_image.allow_tags = True


class kadappaStone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/project-img")
    description = models.TextField()

    def __str__(self):
        return self.name

    def kadappa_image(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))

    kadappa_image.short_description = "Image"
    kadappa_image.allow_tags = True


class BangaloreStone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="upload/project-img")
    description = models.TextField()

    def __str__(self):
        return self.name

    def bangalore_image(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))

    bangalore_image.short_description = "Image"
    bangalore_image.allow_tags = True



class BeforeAfter(models.Model):
    before_image = models.ImageField(upload_to='media')
    after_image = models.ImageField(upload_to='media')


class Testimonial(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    