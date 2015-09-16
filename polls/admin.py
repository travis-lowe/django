from django.contrib import admin

from .models import Choice, Question
# Register your models here.

class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		('The Question',	{'fields':['question_text']}),
		('Date Information', {'fields': ['pub_date']}),
	]

	inlines = [ChoiceInLine]
	list_display = ('question_text', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
