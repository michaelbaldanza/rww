from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='insert_slash')
@stringfilter
def insert_slash(value, arg):
  """Replaces all spaces with a forward slash"""
  return value.replace(arg, '/')

@register.filter(name='insert_comma')
@stringfilter
def insert_comma(value, arg):
  """Replaces a substring a comma"""
  return value.replace(arg, ', ')

@register.filter(name='insert_space')
@stringfilter
def insert_space(value, arg):
  """Replaces a substring with some other string"""
  return value.replace(arg, ' ')

@register.filter(name='questify')
@stringfilter
def questify(value):
  """Adds a question mark at the end of a string"""
  return value + '?'

@register.filter(name='hyphenate_one')
@stringfilter
def hyphenate_one(value):
  """Hyphenates the phrase 'one on one'"""
  return value.replace('one on one', 'one-on-one')

@register.filter(name='make_string')
@stringfilter
def make_string(value):
  return(str(value))