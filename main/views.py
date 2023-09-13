from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
# Create your views here.

def home(request):
    cate = models.QuizCategory.objects.all()
    return render(request,'index.html',{'ca_data':cate})


def register(request):
    msg=None
    form=forms.RegisterUser
    if request.method=="POST":
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            msg='data hass been added'
    return render(request,'registration/register.html',{'form':form,'msg':msg})


def category(request):
    catData = models.QuizCategory.objects.all()
    return render(request, 'all-category.html',{'data':catData})

# Qestion According to category

def category_question(request,cat_id):
    category = models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'category-question.html',{'question':question,'category':category}) 

def submit_answer(request,cat_id,quest_id):
    if request.method=='POST':
        category = models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest = models.QuizQuestion.objects.get(id=quest_id)
                user = request.user
                answer = 'Not Submitted'
                models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
                return render(request, 'category-question.html',{'question':question,'category':category})  
        else:
            quest=models.QuizQuestion.objects.get(id=quest_id)
            user=request.user
            answer=request.POST['answer']
            models.UserSubmittedAnswer.objects.create(user=user,question=quest,right_answer=answer)
        if question:
            return render(request, 'category-question.html',{'question':question,'category':category})
        else:
            return HttpResponse('No More Question !!')
        
    else:   
        return HttpResponse('method not allowed!!')



