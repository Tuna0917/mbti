from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import *
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

max_question_number = Question.objects.count()
q = list(Question.objects.all())

class HomeView(TemplateView):
    template_name = 'home.html'

class TypeIndicatorListView(ListView):
    model = TypeIndicator 

class TypeIndicatorDetailView(DetailView):
    model = TypeIndicator


def test(request):
    if request.method == 'POST':
        n = int(request.POST['num'])

        print(request.POST['mbti'])
        print([x for x in request.POST.keys()])

        if n == max_question_number:
            result = request.POST['base']+request.POST['mbti']
            k = result.count
            mbti = "E" if k("E")>k("I") else "I"
            mbti += "S" if k("S")>k("N") else "N"
            mbti += "T" if k("T")>k("F") else "F"
            mbti += "J" if k("J")>k("P") else "P"

            
            context = {
            'mbti': TypeIndicator.objects.filter(mbti=mbti).get(),
            }
            return render(request, 'result.html', context)

        print(n)
        context = {
            'num':n+1,
            'question':q[n],
            'mbti': request.POST['base']+request.POST['mbti'],
            }

       
    else:

        context = {
            'num':1,
            'question':q[0],
            'mbti':''
            }

    return render(request, 'test.html', context)
