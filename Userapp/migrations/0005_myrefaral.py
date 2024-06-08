# Generated by Django 5.0.3 on 2024-06-02 19:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Userapp", "0004_remove_wallet_referral_deposit_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Myrefaral",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_name",
                    models.CharField(
                        default=None, max_length=25, null=True, unique=True
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]