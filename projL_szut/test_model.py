import sys
import os
import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projL_szut.settings")
django.setup()

"""
q3 = Question(question_text="", pub_date=timezone.now())

# printing objects
# for question in Question.objects.all():
#    print(question)

for choice in Choice.objects.all():
    print(choice, choice.question)
choice = Choice(question=Question.objects.all()[0], choice_text="nothing")
choice1 = Choice(question=Question.objects.all()[0], choice_text="WTF MAN")
choice.save()
choice1.save()

q = Question.objects.filter(id = 1)[0]
print(q)
print(q.choice)

# filter
print(Question.objects.filter(id = 1))
print(Question.objects.filter(question_text__startswith = "What"))


"""