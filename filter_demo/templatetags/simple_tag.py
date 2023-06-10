from django import template

register =  template.Library()

@register.simple_tag
def greet_user(message, username):
    return f"{message}, {username} !!!"