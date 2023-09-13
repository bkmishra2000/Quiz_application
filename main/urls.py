from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('accounts/register',views.register,name="register"),
    path('all-category',views.category),
    path('question-category/<int:cat_id>',views.category_question,name='category_question'),
    path('submit-answer/<int:cat_id>/<int:quest_id>',views.submit_answer,name='submit_answer'),
    
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)