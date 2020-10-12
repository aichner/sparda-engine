# graphene
import graphene
# graphene_django
from graphene_django.converter import String, Boolean

from .images import Image, wagtailImage


class FormField(graphene.ObjectType):
    name = graphene.Field(String)
    field_type = graphene.Field(String)
    help_text = graphene.Field(String)
    required = graphene.Field(Boolean)
    choices = graphene.Field(String)
    default_value = graphene.Field(String)
    label = graphene.Field(String)
    image = graphene.Field(Image)
    title = graphene.Field(String)
    placeholder = graphene.Field(String)

class FormError(graphene.ObjectType):
    name = graphene.Field(String)
    errors = graphene.List(String)
