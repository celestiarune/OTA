# Generated by Django 4.2.4 on 2023-09-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0005_rename_host_experience_owner'),
        ('rooms', '0005_alter_room_amenities_alter_room_category_and_more'),
        ('wishlists', '0003_alter_wishlist_experiences_alter_wishlist_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlists', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(blank=True, null=True, related_name='wishlists', to='rooms.room'),
        ),
    ]
