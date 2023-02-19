from django.db import models
from django.urls import reverse


class University(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя учебного заведения')
    summary = models.TextField(verbose_name='Краткая информация')
    location = models.ForeignKey('UniversityLocation', on_delete=models.PROTECT, verbose_name='Место нахождения')
    avg_price = models.IntegerField(null=True, blank=True, verbose_name='Средняя стоимость обучения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    avg_score = models.IntegerField(null=True, blank=True, verbose_name='Средние баллы для поступления')
    unv_type = models.ForeignKey('UniversityType', on_delete=models.PROTECT, verbose_name='Тип учебного заведения [Гражданский - False/Военный - True]')
    text_history = models.TextField(null=True, blank=True, verbose_name='История')
    paragraph1 = models.TextField(null=True, blank=True, verbose_name='Информация [1 параграф]')
    paragraph2 = models.TextField(null=True, blank=True, verbose_name='Информация [2 параграф]')
    paragraph3 = models.TextField(null=True, blank=True, verbose_name='Информация [3 параграф]')
    paragraph4 = models.TextField(null=True, blank=True, verbose_name='Информация [4 параграф]')
    paragraph5 = models.TextField(null=True, blank=True, verbose_name='Информация [5 параграф]')
    subject1 = models.ForeignKey('UniversitySubject', on_delete=models.PROTECT, null=True, blank=True, related_name='subject1', verbose_name='Предмет1')
    subject2 = models.ForeignKey('UniversitySubject', on_delete=models.PROTECT, null=True, blank=True, related_name='subject2', verbose_name='Предмет2')
    subject3 = models.ForeignKey('UniversitySubject', on_delete=models.PROTECT, null=True, blank=True, related_name='subject3', verbose_name='Предмет3')
    subject4 = models.ForeignKey('UniversitySubject', on_delete=models.PROTECT, null=True, blank=True, related_name='subject4', verbose_name='Предмет4')
    subject5 = models.ForeignKey('UniversitySubject', on_delete=models.PROTECT, null=True, blank=True, related_name='subject5', verbose_name='Предмет5')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон учебного заведения')
    website = models.CharField(max_length=200, null=True, blank=True, verbose_name='Веб сайт учебного заведения')
    img1 = models.ImageField(upload_to="photos", verbose_name='Изображение учебного заведения')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    is_after9 = models.BooleanField(null=True, blank=True, verbose_name='После 9 класса?')
    is_after11 = models.BooleanField(null=True, blank=True, verbose_name='После 11 класса?')
    after = models.IntegerField(null=True, blank=True, verbose_name='После какого класса')
    who_is_creator =  models.ForeignKey('Creator', on_delete=models.PROTECT, null=True, blank=True, related_name='post_creator', verbose_name='Создатель поста')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('certain', kwargs={'unv_id': self.pk})

    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'
        ordering = ['id']


class UniversityType(models.Model):
    isMilitary = models.BooleanField(db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return str(self.isMilitary)
    
    class Meta:
        verbose_name = 'Тип учебного заведения'
        verbose_name_plural = 'Типы учебных заведений'
        ordering = ['id']


class Creator(models.Model):
    creator = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return str(self.creator)
    
    class Meta:
        verbose_name = 'Создатель'
        verbose_name_plural = 'Создатели'
        ordering = ['id']


class UniversityLocation(models.Model):
    location = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Местонахождение учебных заведений'
        verbose_name_plural = 'Местонахождения учебных заведений'
        ordering = ['id']


class UniversitySubject(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Предмет учебного заведения'
        verbose_name_plural = 'Предметы учебных заведений'
        ordering = ['id']
