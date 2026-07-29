from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """
    Multiplier une valeur par un argument.
    Utile pour définir le padding des commentaires MPTT.
    """
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0