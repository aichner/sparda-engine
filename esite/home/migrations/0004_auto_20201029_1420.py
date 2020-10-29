# Generated by Django 2.2.13 on 2020-10-29 13:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201015_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='news',
            field=wagtail.core.fields.StreamField([('n_news', wagtail.core.blocks.StructBlock([('news_img', wagtail.images.blocks.ImageChooserBlock(help_text='News-Titelbild', required=True)), ('news_head', wagtail.core.blocks.CharBlock(help_text='News-Header', required=False)), ('news_text', wagtail.core.blocks.RichTextBlock(help_text='Kurze Beschreibung der News', label='Text', required=True)), ('news_page', wagtail.core.blocks.PageChooserBlock(help_text='News-Artikel', required=False))], icon='fa-info'))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='headers',
            field=wagtail.core.fields.StreamField([('h_hero', wagtail.core.blocks.StructBlock([('slide_image', wagtail.images.blocks.ImageChooserBlock(blank=False, help_text='Großes, hochauflösendes Titelbild einer Versicherung', required=True)), ('slide_head', wagtail.core.blocks.CharBlock(help_text='Versicherungstyp', required=True)), ('slide_lead', wagtail.core.blocks.CharBlock(help_text='Infosatz zur Versicherung', required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='image'))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('s_feature', wagtail.core.blocks.StructBlock([('features', wagtail.core.blocks.StreamBlock([('feature', wagtail.core.blocks.StructBlock([('feature_image', wagtail.images.blocks.ImageChooserBlock(help_text='Icon, um eine angebotene Leistung darzustellen', required=True)), ('feature_head', wagtail.core.blocks.CharBlock(help_text='Titel einer angebotenen Leistung', required=False)), ('feature_text', wagtail.core.blocks.RichTextBlock(help_text='Beschreibung der angebotenen Leistung', label='Text', required=True))], blank=False, icon='fa-info', null=True, required=False))], help_text='Füge zwischen einer und drei angebotenen Leistungen hinzu', max_num=3, null=True, required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_maps', wagtail.core.blocks.StructBlock([('coordinates', wagtail.core.blocks.StreamBlock([('coordinate', wagtail.core.blocks.StructBlock([('coordinate', wagtail.core.blocks.CharBlock(help_text='Gebe hier die Google-Maps-Koordinaten eines Projektes an', required=True))], icon='fa-info', required=False))], help_text='Zeige die Projekt-Locations in einer Map an', required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_partners', wagtail.core.blocks.StructBlock([('coordinates', wagtail.core.blocks.StreamBlock([('coordinate', wagtail.core.blocks.StructBlock([('coordinate', wagtail.core.blocks.CharBlock(help_text='Gebe hier die Google-Maps-Koordinaten eines Projektes an', required=True))], icon='fa-info', required=False))], help_text='Liste hier Partnerunternehmen auf', required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_about', wagtail.core.blocks.StructBlock([('about_img', wagtail.images.blocks.ImageChooserBlock(help_text='Portraitfoto', required=False)), ('about_head', wagtail.core.blocks.CharBlock(help_text='Über Uns-Header', required=False)), ('about_lead', wagtail.core.blocks.CharBlock(help_text='Untertitel', required=False)), ('about_text', wagtail.core.blocks.RichTextBlock(help_text='Beschreibung Über Uns', label='Text', required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_privateinsurances', wagtail.core.blocks.StructBlock([('insurances', wagtail.core.blocks.StreamBlock([('insurance', wagtail.core.blocks.StructBlock([('insurance_image', wagtail.images.blocks.ImageChooserBlock(help_text='Bild, um eine Versicherung darzustellen', required=True)), ('insurance_head', wagtail.core.blocks.CharBlock(help_text='Titel einer angebotenen Versicherung', required=True)), ('insurance_lead', wagtail.core.blocks.CharBlock(help_text='Lead Text einer angebotenen Versicherung', required=False)), ('insurance_text', wagtail.core.blocks.RichTextBlock(help_text='Beschreibung der angebotenen Leistung', label='Text', required=True))], blank=False, icon='fa-info', null=True, required=False))], help_text='Füge beliebig viele angebotene Versicherungen für Privatkunden hinzu', null=True, required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_businessinsurances', wagtail.core.blocks.StructBlock([('insurances', wagtail.core.blocks.StreamBlock([('insurance', wagtail.core.blocks.StructBlock([('insurance_image', wagtail.images.blocks.ImageChooserBlock(help_text='Bild, um eine Versicherung darzustellen', required=True)), ('insurance_head', wagtail.core.blocks.CharBlock(help_text='Titel einer angebotenen Versicherung', required=True)), ('insurance_lead', wagtail.core.blocks.CharBlock(help_text='Lead Text einer angebotenen Versicherung', required=False)), ('insurance_text', wagtail.core.blocks.RichTextBlock(help_text='Beschreibung der angebotenen Leistung', label='Text', required=True))], blank=False, icon='fa-info', null=True, required=False))], help_text='Füge beliebig viele angebotene Versicherungen für Geschäftskunden hinzu', null=True, required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_team', wagtail.core.blocks.StructBlock([('team_members', wagtail.core.blocks.StreamBlock([('team_member', wagtail.core.blocks.StructBlock([('member_image', wagtail.images.blocks.ImageChooserBlock(help_text='Bild des Mitarbeiters/der Mitarbeiterin', required=True)), ('member_name', wagtail.core.blocks.CharBlock(help_text='Name des Mitarbeiters/der Mitarbeiterin', required=True)), ('member_services', wagtail.core.blocks.StreamBlock([('services', wagtail.core.blocks.StructBlock([('service_name', wagtail.core.blocks.CharBlock(help_text='Angebotener Service', required=True))], blank=False, icon='fa-info', null=True, required=False))], help_text='Welche Services bietet dieser MA? z.B. KFZ-Versicherungsexperte, Haushaltsversicherungen, Allround-Experte, ...', null=True, required=True)), ('member_text', wagtail.core.blocks.RichTextBlock(help_text='Genauere Beschreibung des MA, z.B. langjährige Erfahrung, Wirtschaftserfahrung, ...', label='Text', required=False)), ('member_email', wagtail.core.blocks.CharBlock(help_text='E-Mail Adresse des Mitarbeiters/der Mitarbeiterin', required=False)), ('member_mobile', wagtail.core.blocks.CharBlock(help_text='Mobile Nummer des Mitarbeiters/der Mitarbeiterin', required=False)), ('member_phone', wagtail.core.blocks.CharBlock(help_text='Telefonnummer des Mitarbeiters/der Mitarbeiterin', required=False))], blank=False, icon='fa-info', null=True, required=False))], help_text='Füge beliebig viele angebotene Versicherungen für Privatkunden hinzu', null=True, required=True)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_contentcenter', wagtail.core.blocks.StructBlock([('content_center_head', wagtail.core.blocks.CharBlock(help_text='Content-Center Header', required=False)), ('content_center_lead', wagtail.core.blocks.CharBlock(help_text='Content-Center Untertitel', required=False)), ('content_center_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Center Text', label='Text', required=False)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_contentright', wagtail.core.blocks.StructBlock([('content_right_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Right Titelbild', required=False)), ('content_right_head', wagtail.core.blocks.CharBlock(help_text='Content-Right Header', required=False)), ('content_right_lead', wagtail.core.blocks.CharBlock(help_text='Content-Right Untertitel', required=False)), ('content_right_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Right Text', label='Text', required=False)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info')), ('s_contentleft', wagtail.core.blocks.StructBlock([('content_left_img', wagtail.images.blocks.ImageChooserBlock(help_text='Content-Left Titelbild', required=False)), ('content_left_head', wagtail.core.blocks.CharBlock(help_text='Content-Left Header', required=False)), ('content_left_lead', wagtail.core.blocks.CharBlock(help_text='Content-Left Untertitel', required=False)), ('content_left_text', wagtail.core.blocks.RichTextBlock(help_text='Content-Left Text', label='Text', required=False)), ('slug', wagtail.core.blocks.CharBlock(blank=True, help_text='Slug (Navigation)', null=True, required=False))], icon='fa-info'))], blank=True, null=True),
        ),
    ]