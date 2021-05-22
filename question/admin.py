from django.contrib import admin
from .models import *
# Register your models here.

class SelectInline(admin.StackedInline):
    model = Select
    extra = 2 #추가로 입력할 수 있는 Photo 테이블 객체 수는 2 개.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = (SelectInline,)

@admin.register(TypeIndicator)
class TypeIndicatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('mbti',)}


admin.site.register(Select)
admin.site.register(DetailText)


