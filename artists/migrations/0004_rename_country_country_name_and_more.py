# Generated by Django 4.1 on 2022-08-18 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("artists", "0003_remove_country_artist_remove_gender_artist_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="country",
            old_name="country",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="gender",
            old_name="gender",
            new_name="option",
        ),
    ]