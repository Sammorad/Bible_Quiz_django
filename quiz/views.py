from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    quiz_questions = Question.objects.all()[:5]
    context = {"quiz_questions": quiz_questions}
    return render(request, "quiz/index.html", context)

    


def detail (request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    return render(request, "quiz/detail.html", {"question": question})

    

def results (request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'quiz/detail.html', {'question':question, 'error_message': "You didnt select a choice",})
    is_correct = selected_choice.correct
    return render(request, 'quiz/results.html', {
                    'question': question, 'selected_choice':selected_choice, 'is_correct':is_correct,}) 
