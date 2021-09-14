from django.contrib import admin
from .models import Quiz, Result


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'question', 'answer']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'subject', 'marks', 'date', 'time']