# Generated by Django 3.2.8 on 2021-10-28 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_image"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Image",
        ),
        migrations.AddField(
            model_name="blog",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
