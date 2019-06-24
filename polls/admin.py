from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """
        Choice objects are edited on the Question admin page. By default, 
        provides enough fields for 3 choices.
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
