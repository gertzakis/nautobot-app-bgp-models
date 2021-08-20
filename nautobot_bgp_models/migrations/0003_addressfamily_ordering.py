# Generated by Django 3.1.8 on 2021-07-13 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nautobot_bgp_models", "0002_refactoring"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="addressfamily",
            options={
                "ordering": ["-peer_endpoint", "-peer_group"],
                "verbose_name": "BGP address-family",
                "verbose_name_plural": "BGP address-families",
            },
        ),
    ]