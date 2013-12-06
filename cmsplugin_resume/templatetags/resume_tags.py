from django import template

register = template.Library()


@register.simple_tag
def render_skills(skills):
    result = []
    for skill in skills.split(','):
        result += ["<span class='label label-primary'>%s</span>" % skill.strip()]
    return ' '.join(result)
