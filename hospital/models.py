from django.db import models


# Create your models here.
class Doctors(models.Model):
    department = models.CharField("Отделение", max_length=70)
    second_name_doctor = models.CharField("Фамилия", max_length=50)
    first_name_doctor = models.CharField("Имя", max_length=50)
    last_name_doctor = models.CharField("Отчествво", max_length=50)
    age = models.IntegerField("Возраст")
    experience = models.IntegerField("Опыт работы")
    about_doctor = models.TextField("О докторе")

    def __str__(self):
        return f"{self.second_name_doctor} {self.first_name_doctor} {self.last_name_doctor} ({self.department})"

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'


class Departments(models.Model):
    department_name = models.CharField("Назавание отделения", max_length=50)
    department_info = models.TextField("Что лечат в этом отделении")

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'


class Diagnosis(models.Model):
    second_name_patient = models.CharField("Фамилия пациента", max_length=50)
    first_name_patient = models.CharField("Имя пациента", max_length=50)
    last_name_patient = models.CharField("Отчествво пациента", max_length=50)
    age_patient = models.IntegerField("Возраст пациента")
    complaints = models.TextField("Жалобы пациента")
    date_start = models.DateField("Начало лечения")
    date_finish = models.DateField("Конец лечения")
    second_name_doctor = models.CharField("Фамилия доктора", max_length=50)
    first_name_doctor = models.CharField("Имя доктора", max_length=50)
    last_name_doctor = models.CharField("Отчествво доктора", max_length=50)
    diagnosis = models.CharField("Диагноз", max_length=50)

    def __str__(self):
        return f"{self.second_name_patient} - {self.second_name_doctor}, ({self.date_start}-{self.date_finish}) -> {self.diagnosis}"

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'


class Rooms(models.Model):
    department = models.CharField("Отделение", max_length=70)
    number = models.IntegerField("Номер палаты")
    status = models.BooleanField("Свободна палата", default=True)

    def __str__(self):
        return f"{self.department}: {self.number} - {self.status}"

    class Meta:
        verbose_name = "Палата"
        verbose_name_plural = "Палаты"
