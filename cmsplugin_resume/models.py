from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from djangocms_text_ckeditor.fields import HTMLField


class Resume(CMSPlugin):
    owner = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    summary = HTMLField(null=True, blank=True)

    class Meta:
        verbose_name = _('Resume plugin')
        verbose_name_plural = _('Resume plugins')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def copy_relations(self, from_instance):
        for wexp in from_instance.workexperience_set.all():
            wexp.pk = None
            wexp.resume = self
            wexp.save()
        for proj in from_instance.project_set.all():
            proj.pk = None
            proj.resume = self
            proj.save()
        for edu in from_instance.education_set.all():
            edu.pk = None
            edu.resume = self
            edu.save()
        for skc in from_instance.skillscategory_set.all():
            skc.pk = None
            skc.resume = self
            skc.save()


class Experience(models.Model):
    title = models.CharField(max_length=300)
    startdate = models.DateField()
    description = HTMLField(blank=True)
    resume = models.ForeignKey(Resume)
    skills = models.TextField()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title


class WorkExperience(Experience):
    company = models.CharField(max_length=150)
    enddate = models.DateField(blank=True, null=True)


class Education(models.Model):
    school = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    resume = models.ForeignKey(Resume)

    def __unicode__(self):
        return self.degree


class Project(Experience):
    url = models.URLField()


class SkillsCategory(models.Model):
    name = models.CharField(max_length=200)
    skills = models.TextField()
    resume = models.ForeignKey(Resume)

    def __unicode__(self):
        return self.name

