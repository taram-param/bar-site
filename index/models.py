from django.db import models
from datetime import date
import os
from django.urls import reverse


class Place(models.Model):

    name = models.CharField("Заведение", max_length=255)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("place_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Заведение"
        verbose_name_plural = "Заведения"


class Collection(models.Model):

    place = models.ForeignKey(Place, verbose_name="Заведение", on_delete=models.CASCADE, null=False)
    banner = models.ImageField("Обложка", upload_to="collection/")
    date = models.DateField("Дата проведения")
    name = models.CharField("Событие", max_length=300)
    views = models.PositiveIntegerField("Просмотры", default=0)
    url = models.SlugField(max_length=255, unique=True)
    collection_archive = models.FileField("Архив с фотографиями", upload_to="collection_archives/%Y/%m/%d/")

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse("collection_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Отчет"
        verbose_name_plural = "Отчеты"


class PlaceShots(models.Model):

    title = models.CharField("Название", default="Any", max_length=100)
    place = models.ForeignKey(Place, verbose_name="Заведение", on_delete=models.CASCADE)
    image = models.ImageField("Изображение заведения", upload_to="place/")

    class Meta:
        verbose_name = "Изображение заведения"
        verbose_name_plural = "Изображения заведения"


class CollectionShots(models.Model):

    title = models.CharField(max_length=10, null=True, default="any")
    collection = models.ForeignKey(Collection, verbose_name="Отчет", on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='collection_shots/%Y/%m/%d/')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Video(models.Model):

    place = models.ForeignKey(Place, verbose_name="Заведение", on_delete=models.CASCADE)
    event = models.CharField("Событие", max_length=250)
    banner = models.ImageField("Кадр", upload_to="video_shots/", null=False)
    date = models.DateField("Дата события")
    youtube_url = models.CharField("Ссылка с Youtube", max_length=250)

    url = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"slug": self.url})
