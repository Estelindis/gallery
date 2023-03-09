# Generated by Django 3.2 on 2023-03-09 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sku_code', models.CharField(max_length=6)),
                ('friendly_name', models.CharField(max_length=80, verbose_name='Friendly Name')),
                ('full_name', models.CharField(blank=True, max_length=240, null=True, verbose_name='Full Name')),
                ('location', models.CharField(blank=True, max_length=240, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Image URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('banner_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Image URL')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='')),
                ('facebook_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Facebook')),
                ('twitter_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Twitter')),
                ('insta_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Instagram')),
                ('deviant_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='DeviantArt')),
                ('pin_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Pinterest')),
                ('etsy_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Etsy')),
            ],
        ),
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sku_code', models.CharField(max_length=12)),
                ('friendly_name', models.CharField(max_length=80, verbose_name='Friendly Name')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Image URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Canvasses',
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('sku_code', models.CharField(max_length=12)),
                ('friendly_name', models.CharField(max_length=80, verbose_name='Friendly Name')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Image URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=250)),
                ('friendly_name', models.CharField(max_length=250, verbose_name='Friendly Name')),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True, verbose_name='Image URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.artist')),
                ('canvas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.canvas')),
                ('design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='artworks.design')),
            ],
        ),
    ]