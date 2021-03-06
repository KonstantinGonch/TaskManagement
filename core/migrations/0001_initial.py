# Generated by Django 2.2.1 on 2019-05-26 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('description', models.TextField(verbose_name='Описание')),
                ('useful_info', models.TextField(null=True, verbose_name='Дополнительная информация')),
            ],
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор'), ('customer', 'Заказчик')], max_length=100, verbose_name='Роль')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное имя')),
                ('contacts', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('status', models.CharField(choices=[('not assigned', 'Не назначено'), ('assigned', 'Назначено'), ('in progress', 'В процессе'), ('done', 'Сделано'), ('rejected', 'Отклонено')], max_length=100, verbose_name='Статус')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_creator', to='core.SystemUser')),
                ('executors', models.ManyToManyField(to='core.SystemUser')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование')),
                ('planned_start', models.DateField()),
                ('planned_end', models.DateField()),
                ('real_start', models.DateField()),
                ('real_end', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='', verbose_name='Файл')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_creator', to='core.SystemUser'),
        ),
        migrations.AddField(
            model_name='project',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_customer', to='core.SystemUser'),
        ),
        migrations.AddField(
            model_name='project',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Namespace'),
        ),
        migrations.AddField(
            model_name='namespace',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='namespace_creator', to='core.SystemUser'),
        ),
        migrations.AddField(
            model_name='namespace',
            name='users',
            field=models.ManyToManyField(to='core.SystemUser'),
        ),
    ]
