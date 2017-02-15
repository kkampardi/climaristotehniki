from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from PIL import Image


class Project(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    short_description = models.CharField(max_length=200, blank=True)
    short_description_en = models.CharField(max_length=200, blank=True)
    description = RichTextField()
    description_en = RichTextField()
    client = models.CharField(max_length=200)
    client_en = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='portfolio')

    class Meta:
        ordering = ['-start_date', ]

    def get_absolute_url(self):
        return reverse('portfolio_detail',args=[self.slug])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.name


def get_image_path(instance, filename):
    return '/'.join(['project_images', instance.project.slug, filename])


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=1)
    image = models.ImageField(upload_to=get_image_path)

    # add this bit in after our model
    def save(self, *args, **kwargs):
        # this is required when you override save functions
        super(ProjectImage, self).save(*args, **kwargs)
        # our new code
        if self.image:
            image = Image.open(self.image)
            i_width, i_height = image.size
            max_size = (1240, 700)

            if i_width > 1240:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)
            elif i_height > 700:
                image.thumbnail(max_size, Image.ANTIALIAS)
                image.save(self.image.path)


class Category(models.Model):
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    description = RichTextField()
    description_en = RichTextField()
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"


    def __unicode__(self):
        return self.name
