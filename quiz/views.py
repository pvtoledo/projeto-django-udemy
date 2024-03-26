from django.http import HttpResponse
from django.shortcuts import render
from quiz.models import Questao


def carrega_quiz(request):
    # questao = Questao.objects.raw('select * from blog.blog_db.quiz_questao order by random() limit 1')[0]
    questao = Questao.objects.order_by("?").first()
    context = {
        'questao': questao
    }
    return render(request, 'quiz/quiz.html', context=context)


def carrega_resposta(request):
    resposta = request.POST.get('resposta')

    if resposta == "True":
        return HttpResponse("<p style='color:green'> Resposta correta. </p>")
    elif resposta == "False":
        return HttpResponse("<p style='color:red'> Resposta errada. </p>")
    else:
        return HttpResponse("<p style='color:red'> Selecione uma alternativa. </p>")
