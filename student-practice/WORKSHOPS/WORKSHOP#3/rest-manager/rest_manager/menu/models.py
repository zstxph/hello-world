from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Course(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    
    def __str__(self): #__str__ method will specify what to return when you call str() an object.
        return self.name



class MenuItem(models.Model): #MenuItem Class inherits models.Model
    dish_title = models.CharField(max_length=250) #a varchar
    price = models.IntegerField(default=0) #an integer field
    description = models.TextField(blank=True) #a text field
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date


    class Meta:
        ordering = ["dish_title"] #ordering by the created field
    
    def __str__(self) :
        return self.dish_title #name to be shown when called
