from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Категорія')
    slug = models.SlugField(max_length=255,
                            verbose_name='Url',
                            unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Тег')
    slug = models.SlugField(max_length=50,
                            verbose_name='Url',
                            unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50,
                            verbose_name='Url',
                            unique=True)
    author = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубліковано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кількість переглядів')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='post')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Пости'
