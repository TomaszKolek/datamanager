# Generated by Django 2.2.10 on 2020-03-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetportal', '0047_categoryguide_guideindexpage_guidepage_learningindexpage_postindexpage_postpage_wagtailhomepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryguide',
            name='category_slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
