from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    field = ['pub_date', 'question_text']
    fieldsets = [
        ("Question title", {'fields':['question_text']}),
        ('Data information', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # pub_date(설문조사 생성 시간)을 기준으로 필터 기능 추가
    search_fields = ['question_text'] # question_text(설문조사 주제)를 기준으로 검색 기능 추가

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)