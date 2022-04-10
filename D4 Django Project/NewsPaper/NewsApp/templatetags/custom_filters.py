from django import template

register = template.Library()



@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError

    return value.replace("fick", "f***")





