# mysiteapp/admin.py

from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at', 'total_likes')
    list_filter = ('created_at',)
    search_fields = ('question__title', 'content')

    def total_likes(self, obj):
        return obj.likes.count()
    total_likes.admin_order_field = 'likes__count'

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
