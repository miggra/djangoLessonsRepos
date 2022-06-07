from django.http import HttpResponse
from django.template import loader


class Question:
    def __init__(self, id, question_text):
        self.id = id
        self.question_text = question_text


def index(request):
    latest_question_list = [Question(1, "First question"), Question(2, "Second question")]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
