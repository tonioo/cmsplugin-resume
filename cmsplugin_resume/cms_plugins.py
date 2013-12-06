from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from cmsplugin_resume.models import Resume, WorkExperience, Education


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 1


class ResumePlugin(CMSPluginBase):
    model = Resume
    module = 'Resume'
    name = _("Resume")
    render_template = "cmsplugin_resume/resume.html"

    inlines = [
        WorkExperienceInline,
        EducationInline
    ]

    def render(self, context, instance, placeholder):
        context['resume'] = instance
        return context

plugin_pool.register_plugin(ResumePlugin)
