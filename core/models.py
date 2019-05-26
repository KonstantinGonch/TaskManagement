from django.db import models
from django.contrib.auth.models import User
import datetime


class Namespace(models.Model):
    title = models.CharField(max_length=100, verbose_name="Имя")
    creator = models.ForeignKey("SystemUser", on_delete=models.SET_NULL, null=True, related_name="namespace_creator")
    users = models.ManyToManyField("SystemUser")

    def __str__(self):
        return self.title


class SystemUser(models.Model):
    USER_ROLES = (("user", "Пользователь"), ("admin", "Администратор"), ("customer", "Заказчик"))
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Пользователь")
    role = models.CharField(max_length=100, choices=USER_ROLES, verbose_name="Роль")
    full_name = models.CharField(max_length=100, verbose_name="Полное имя")
    contacts = models.TextField()

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    useful_info = models.TextField(verbose_name="Дополнительная информация", null=True)
    creator = models.ForeignKey(SystemUser, on_delete=models.SET_NULL, null=True, related_name="project_creator")
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
    customer = models.ForeignKey(SystemUser, on_delete=models.SET_NULL, null=True, related_name="project_customer")
    creation_date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return self.title


class Task(models.Model):
    TASK_STATS = (("not assigned", "Не назначено"),
                  ("assigned", "Назначено"), ("in progress", "В процессе"),
                  ("done", "Сделано"), ("rejected", "Отклонено"))
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание задачи")
    status = models.CharField(max_length=100, verbose_name="Статус", choices=TASK_STATS)
    executors = models.ManyToManyField(SystemUser)
    creator = models.ForeignKey(SystemUser, on_delete=models.SET_NULL, null=True, related_name="task_creator")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProjectDoc(models.Model):
    document = models.FileField(verbose_name="Файл")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + "Документ"


class ProjectStage(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    planned_start = models.DateField()
    planned_end = models.DateField()
    real_start = models.DateField()
    real_end = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " Проект: " + self.project.title
