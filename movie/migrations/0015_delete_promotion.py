# Generated by Django 4.1.1 on 2022-10-03 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0014_rename_promotions_promotion"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Promotion",
        ),
    ]
