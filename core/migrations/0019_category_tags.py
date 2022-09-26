# Generated by Django 4.0.5 on 2022-08-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_category_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='core.tags'),
        ),
    ]
