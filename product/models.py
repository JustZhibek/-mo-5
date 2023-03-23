from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    category = models.ForeignKey('Category' , on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Review(models.Model):
    text = models.TextField(blank=True, null=True)
    product = models.ForeignKey('Category' , on_delete=models.CASCADE())


    def __str__(self):
        return self.text
