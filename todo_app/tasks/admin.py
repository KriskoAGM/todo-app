from django.contrib import admin
from todo_app.tasks.models import Task, Comment, Priority, Category

# Register your models here.

class TaskAdmin(admin.ModelAdmin):

    list_display = ['title', 'user', 'due_date'] # Display these fields in the list view
    list_filter = ['user']  # Add filters for these fields
    search_fields = ['title', 'user__username'] # Enable search by title and user's username
    ordering = ['-due_date', 'user'] # Order tasks by due date (descending) and then by user



class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'user', 'created_at']
    list_filter = ['user']


class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(Category, CategoryAdmin)