from django.db import models

from todo_app.auth_user.models import Profile

# Create your models here.

class Category(models.Model):

    CATEGORY_CHOICES = (
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Home', 'Home'),
        ('Health', 'Health'),
        ('Shopping', 'Shopping'),
        ('Social', 'Social'),
        ('Finance', 'Finance'),
        ('Travel', 'Travel'),
        ('Hobbies', 'Hobbies'),
    )

    name = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class Priority(models.Model):

    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    name = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        unique=True,
    )

    def __str__(self):
        return self.name


class Task(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    
    task = models.ForeignKey(
        Task, 
        on_delete=models.CASCADE
    )
    
    user = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE,
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.task.title} by {self.user.username}'