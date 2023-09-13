from django.contrib import admin
from . import models

# Register your models here.
# add your model class here 
admin.site.register(models.QuizCategory)

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display=['question','lavel']
admin.site.register(models.QuizQuestion,QuizQuestionAdmin)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id','question','user','right_answer']
admin.site.register(models.UserSubmittedAnswer,UserSubmittedAnswerAdmin)