from django.http import HttpResponse
from django.db import models
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import PageChooserPanel, TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from modelcluster.fields import ParentalKey

from esite.colorfield.fields import ColorField, ColorAlphaField
from esite.colorfield.blocks import ColorBlock, ColorAlphaBlock, GradientColorBlock

#from grapple.models import (
#    GraphQLField,
#    GraphQLString,
#    GraphQLStreamfield,
#)

# Create your homepage related models here.

@register_snippet
class Button(models.Model):
    button_title = models.CharField(null=True, blank=False, max_length=255)
    button_embed = models.CharField(null=True, blank=True, max_length=255)
    button_link = models.URLField(null=True, blank=True)
    button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    panels = [
        FieldPanel('button_title'),
        FieldPanel('button_embed'),
        FieldPanel('button_link'),
        PageChooserPanel('button_page')
    ]

    def __str__(self):
        return self.button_title


#> Header
class _H_HeroBlock(blocks.StructBlock):
    slide_image = ImageChooserBlock(required=True, blank=False, help_text="Großes, hochauflösendes Titelbild einer Versicherung")
    slide_head = blocks.CharBlock(required=True, help_text="Versicherungstyp")
    slide_lead = blocks.CharBlock(required=True, help_text="Infosatz zur Versicherung")
    slide_contact = blocks.CharBlock(required=True, help_text="Ansprechpartner (Name)")
    slide_email = blocks.CharBlock(required=False, help_text="E-Mail Adresse des Ansprechpartners")
    slide_mobile = blocks.CharBlock(required=False, help_text="Mobile Handynummer des Ansprechpartners")
    slide_phone = blocks.CharBlock(required=False, help_text="Telefonnummer des Ansprechpartners")

class FeatureFeatureBlock(blocks.StructBlock):
    feature_image = ImageChooserBlock(required=True, help_text="Icon, um eine angebotene Leistung darzustellen")
    feature_head = blocks.CharBlock(required=False, help_text="Titel einer angebotenen Leistung")
    feature_text = blocks.RichTextBlock(label='Text', required=True, help_text="Beschreibung der angebotenen Leistung")

class _S_FeatureBlock(blocks.StructBlock):
    features = blocks.StreamBlock([
        ('feature', FeatureFeatureBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Füge zwischen einer und drei angebotenen Leistungen hinzu', max_num=3)

class MapsCoordBlock(blocks.StructBlock):
    coordinate = blocks.CharBlock(required=True, help_text="Gebe hier die Google-Maps-Koordinaten eines Projektes an")

class _S_MapsBlock(blocks.StructBlock):
    coordinates = blocks.StreamBlock([
        ('coordinate', MapsCoordBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Zeige die Projekt-Locations in einer Map an")

class PartnersPartnerBlock(blocks.StructBlock):
    partner_img = ImageChooserBlock(required=True, help_text="Partner-Logo")
    partner_link = blocks.CharBlock(required=False, help_text="URL der Partner-Website")

class _S_PartnersBlock(blocks.StructBlock):
    coordinates = blocks.StreamBlock([
        ('coordinate', MapsCoordBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Liste hier Partnerunternehmen auf")

class _S_AboutBlock(blocks.StructBlock):
    about_img = ImageChooserBlock(required=False, help_text="Portraitfoto")
    about_head = blocks.CharBlock(required=False, help_text="Über Uns-Header")
    about_lead = blocks.CharBlock(required=False, help_text="Untertitel")
    about_text = blocks.RichTextBlock(label='Text', required=True, help_text="Beschreibung Über Uns")

class NewsNewsBlock(blocks.StructBlock):
    news_img = ImageChooserBlock(required=True, help_text="News-Titelbild")
    news_head = blocks.CharBlock(required=False, help_text="News-Header")
    news_text = blocks.RichTextBlock(label='Text', required=True, help_text="Kurze Beschreibung der News")

class _S_NewsBlock(blocks.StructBlock):
    news = blocks.StreamBlock([
        ('news', NewsNewsBlock(required=False, icon='fa-info'))
    ], required=True, help_text="Neuigkeiten")

class InsurancesInsuranceBlock(blocks.StructBlock):
    insurance_image = ImageChooserBlock(required=True, help_text="Bild, um eine Versicherung darzustellen")
    insurance_head = blocks.CharBlock(required=True, help_text="Titel einer angebotenen Versicherung")
    insurance_lead = blocks.CharBlock(required=False, help_text="Lead Text einer angebotenen Versicherung")
    insurance_text = blocks.RichTextBlock(label='Text', required=True, help_text="Beschreibung der angebotenen Leistung")

class _S_PrivateInsuranceBlock(blocks.StructBlock):
    insurances = blocks.StreamBlock([
        ('insurance', InsurancesInsuranceBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Füge beliebig viele angebotene Versicherungen für Privatkunden hinzu')

class _S_BusinessInsuranceBlock(blocks.StructBlock):
    insurances = blocks.StreamBlock([
        ('insurance', InsurancesInsuranceBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Füge beliebig viele angebotene Versicherungen für Geschäftskunden hinzu')

class TeamMemberServiceBlock(blocks.StructBlock):
    service_name = blocks.CharBlock(required=True, help_text="Angebotener Service")

class TeamMemberBlock(blocks.StructBlock):
    member_image = ImageChooserBlock(required=True, help_text="Bild des Mitarbeiters/der Mitarbeiterin")
    member_name = blocks.CharBlock(required=True, help_text="Name des Mitarbeiters/der Mitarbeiterin")
    member_services = blocks.StreamBlock([
        ('services', TeamMemberServiceBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Welche Services bietet dieser MA? z.B. KFZ-Versicherungsexperte, Haushaltsversicherungen, Allround-Experte, ...')
    member_text = blocks.RichTextBlock(label='Text', required=False, help_text="Genauere Beschreibung des MA, z.B. langjährige Erfahrung, Wirtschaftserfahrung, ...")
    member_email = blocks.CharBlock(required=False, help_text="E-Mail Adresse des Mitarbeiters/der Mitarbeiterin")
    member_mobile = blocks.CharBlock(required=False, help_text="Mobile Nummer des Mitarbeiters/der Mitarbeiterin")
    member_phone = blocks.CharBlock(required=False, help_text="Telefonnummer des Mitarbeiters/der Mitarbeiterin")

class _S_TeamBlock(blocks.StructBlock):
    team_members = blocks.StreamBlock([
        ('team_member', TeamMemberBlock(null=True, blank=False, required=False, icon='fa-info'))
    ], null=True, required=True, help_text='Füge beliebig viele angebotene Versicherungen für Privatkunden hinzu')

class _S_ContentCenter(blocks.StructBlock):
    content_center_head = blocks.CharBlock(required=False, help_text="Content-Center Header")
    content_center_lead = blocks.CharBlock(required=False, help_text="Content-Center Untertitel")
    content_center_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Center Text")
    
class _S_ContentRight(blocks.StructBlock):
    content_right_img = ImageChooserBlock(required=False, help_text="Content-Right Titelbild")
    content_right_head = blocks.CharBlock(required=False, help_text="Content-Right Header")
    content_right_lead = blocks.CharBlock(required=False, help_text="Content-Right Untertitel")
    content_right_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Right Text")

class _S_ContentLeft(blocks.StructBlock):
    content_left_img = ImageChooserBlock(required=False, help_text="Content-Left Titelbild")
    content_left_head = blocks.CharBlock(required=False, help_text="Content-Left Header")
    content_left_lead = blocks.CharBlock(required=False, help_text="Content-Left Untertitel")
    content_left_text = blocks.RichTextBlock(label='Text', required=False, help_text="Content-Left Text")

#> Homepage
class HomePage(Page):
    city = models.CharField(null=True, blank=False, max_length=255)
    zip_code = models.CharField(null=True, blank=False, max_length=255)
    address = models.CharField(null=True, blank=False, max_length=255)
    telephone = models.CharField(null=True, blank=True, max_length=255)
    vat_number = models.CharField(null=True, blank=True, max_length=255)
    email = models.CharField(null=True, blank=True, max_length=255)

    copyrightholder = models.CharField(null=True, blank=True, max_length=255)

    about = RichTextField(null=True, blank=True)
    privacy = RichTextField(null=True, blank=True)
    shipping = RichTextField(null=True, blank=True)
    gtc = RichTextField(null=True, blank=True)
    cancellation_policy = RichTextField(null=True, blank=True)

    sociallinks = StreamField([
        ('link', blocks.URLBlock(help_text="Important! Format https://www.domain.tld/xyz"))
    ], null=True, blank=True)

    array = []
    def sociallink_company(self):
        for link in self.sociallinks:
            self.array.append(str(link).split(".")[1])
        return self.array


    headers = StreamField([
        ('h_hero', _H_HeroBlock(icon='image')),
        # ('code', blocks.RawHTMLBlock(null=True, blank=True, classname="full", icon='code'))
    ])

    sections = StreamField([
        ('s_feature', _S_FeatureBlock(icon='fa-info')),
        ('s_maps', _S_MapsBlock(icon='fa-info')),
        ('s_partners', _S_PartnersBlock(icon='fa-info')),
        ('s_about', _S_AboutBlock(icon='fa-info')),
        ('s_news', _S_NewsBlock(icon='fa-info')),
        ('s_privateinsurances', _S_PrivateInsuranceBlock(icon='fa-info')),
        ('s_businessinsurances', _S_BusinessInsuranceBlock(icon='fa-info')),
        ('s_team', _S_TeamBlock(icon='fa-info')),
        ('s_contentcenter', _S_ContentCenter(icon='fa-info')),
        ('s_contentright', _S_ContentRight(icon='fa-info')),
        ('s_contentleft', _S_ContentLeft(icon='fa-info'))
    ], null=True, blank=True)

    main_content_panels = [
        StreamFieldPanel('headers'),
        StreamFieldPanel('sections'),
        # StreamFieldPanel('footers')
    ]

    imprint_panels = [
        MultiFieldPanel(
            [
            FieldPanel('city'),
            FieldPanel('zip_code'),
            FieldPanel('address'),
            FieldPanel('telephone'),
            FieldPanel('email'),
            FieldPanel('copyrightholder')
            ],
            heading="contact",
        ),
        MultiFieldPanel(
            [
            FieldPanel('vat_number')
            ],
            heading="legal",
        ),
        StreamFieldPanel('sociallinks'),
        MultiFieldPanel(
            [
            FieldPanel('about'),
            FieldPanel('privacy'),
            FieldPanel('shipping'),
            FieldPanel('gtc'),
            FieldPanel('cancellation_policy'),
            ],
            heading="terms",
        )
    ]

    edit_handler = TabbedInterface([
        ObjectList(Page.content_panels + main_content_panels, heading='Main'),
        ObjectList(imprint_panels, heading='Imprint'),
        ObjectList(Page.promote_panels + Page.settings_panels, heading='Settings', classname="settings")
    ])

    preview_modes = []