from django import template

register = template.Library()


def render_skills(skills, classes="label-primary"):
    result = []
    for skill in skills.split(','):
        result += ["<span class='label %s'>%s</span>"
                   % (classes, skill.strip())]
    return ' '.join(result)


@register.simple_tag
def render_normal_skills(skills):
    return render_skills(skills)


@register.simple_tag
def render_big_skills(skills):
    return render_skills(skills, classes="label-primary label-big")
