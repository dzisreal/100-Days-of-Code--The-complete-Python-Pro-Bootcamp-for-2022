from django.shortcuts import render,get_object_or_404
from .models import Question
# Create your views here.

def index(request):
    myname = "Danh Hoa"
    taisan = ["Phone","Laptop","Plane"]
    context ={"name" : myname, "item" : taisan}
    return render(request, "polls/index.html", context)

def viewlist(request):
    #get_object_or_404(Question, pk = 1)
    list_question = Question.objects.all()
    context = {"lstquest" : list_question}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    q = Question.objects.get(pk = question_id)
    return  render(request,"polls/detail_question.html", {"qs": q})
