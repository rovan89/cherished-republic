from django.contrib import admin
from .models import ToDoList
from django_summernote.admin import SummernoteModelAdmin

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_on')
    summernote_fields = ('content')

