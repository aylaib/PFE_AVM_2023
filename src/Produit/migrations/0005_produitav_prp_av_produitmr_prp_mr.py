# Generated by Django 4.1.7 on 2023-04-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Produit', '0004_alter_promotionav_p_av_alter_promotionmr_p_mr'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitav',
            name='prP_av',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='produitmr',
            name='prP_mr',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
