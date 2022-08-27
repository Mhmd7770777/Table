# Generated by Django 4.1 on 2022-08-27 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("artists", "0006_remove_artist_country_remove_artist_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="artist",
            name="country",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="artists.country",
            ),
        ),
        migrations.AddField(
            model_name="artist",
            name="gender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="artists.gender",
            ),
        ),
    ]
