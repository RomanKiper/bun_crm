# Generated by Django 4.1.7 on 2024-02-18 18:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'db_table': 'custom_user_table',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категрия рекламы',
                'verbose_name_plural': 'категрии рекламы',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124, unique=True, verbose_name='вид рекламы')),
                ('description', models.CharField(max_length=350, null=True, verbose_name='описание')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('mentor', 'ментор'), ('manager', 'менеджер'), ('administrator', 'администратор')], default='manager', max_length=15, null=True, unique=True, verbose_name='роль пользователя')),
            ],
            options={
                'verbose_name': 'роль',
                'verbose_name_plural': 'роли',
            },
        ),
        migrations.CreateModel(
            name='Commercial_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='описание')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='стоимость')),
                ('number', models.PositiveSmallIntegerField(default=0, verbose_name='номер предложения')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата создания')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bun_app.client', verbose_name='клиент')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'коммерческое предложение',
                'verbose_name_plural': 'коммерческие предложения',
            },
        ),
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='вид рекламы')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='стоимость')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertising_photos', verbose_name='картинка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bun_app.advertisingcategory', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'вид рекламы',
                'verbose_name_plural': 'виды рекламы',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bun_app.role', verbose_name='роль пользователя'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]