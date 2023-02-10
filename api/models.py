from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name



class Phrases(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='phrases', blank=False)
    phrase = models.CharField(max_length=255, unique=True, verbose_name='Phrase', blank=False)
    image_url = models.CharField(max_length=255, unique=True)


    def __str__(self):
        return self.phrase

    class Meta:
        verbose_name = 'Phrase'
        verbose_name_plural = 'Phrases'