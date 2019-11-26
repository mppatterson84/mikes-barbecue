from django.db import models
from datetime import datetime
from django.utils.text import slugify


class Recipe(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=False)
    updated_at = models.DateTimeField(default=datetime.now, blank=False)
    slug = models.SlugField(unique=False, blank=True, default='slug')
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = datetime.now()
        super(Recipe, self).save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('recipe-detail', kwargs={'pk': self.pk, 'slug': self.slug})