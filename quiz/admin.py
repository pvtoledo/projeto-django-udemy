from django.contrib import admin

from quiz.models import Questao, Alternativa


class AlternativaInline(admin.TabularInline):
    model = Alternativa


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AlternativaInline
    ]

    class Meta:
        model = Questao

admin.site.register(Questao, QuestionAdmin)
admin.site.register(Alternativa)
