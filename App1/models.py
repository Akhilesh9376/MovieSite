from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.title
    

class Image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    link=models.URLField(max_length=200)
    image=models.ImageField(upload_to='images')
    added_date=models.DateTimeField(auto_now_add=True)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name