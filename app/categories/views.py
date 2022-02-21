from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.template import RequestContext
from teacher.models import papers
import random
# → In this view, we configure the operation of the categories. 
# # The categories and keywords obtained from the Machine Learning part are obtained and displayed on the screen.
def categories(request):
    paper_id = request.session.get('paper_id')
    category = request.session.get('category')
    keywords = request.session.get('keywords')
    context = {
        "cat0": category[0],
        "cat1": category[1],
        "cat2": category[2],
        "cat3": category[3],
        "cat4": category[4],
        "cat5": category[5],
        "cat6": category[6],
        "cat7": category[7],
        "cat8": category[8],
        "cat9": category[9],
        "cat10": category[10],
        "cat11": category[11],
        "cat12": category[12],
        "key0": keywords[0],
        "key1": keywords[1],
        "key2": keywords[2],
        "key3": keywords[3],
        "key4": keywords[4],
        "key5": keywords[5],
        "key6": keywords[6],
        "key7": keywords[7],
        "key8": keywords[8],
        "key9": keywords[9]
    }
    # → If a POST occurs, the categories that the teacher selected are retrieved and stored with the previously loaded Paper.
    if request.method == 'POST':
        fcategory = []
        cat0 = request.POST.getlist('cat0')
        cat1 = request.POST.getlist('cat1')
        cat2 = request.POST.getlist('cat2')
        cat3 = request.POST.getlist('cat3')
        cat4 = request.POST.getlist('cat4')
        cat5 = request.POST.getlist('cat5')
        cat6 = request.POST.getlist('cat6')
        cat7 = request.POST.getlist('cat7')
        cat8 = request.POST.getlist('cat8')
        cat9 = request.POST.getlist('cat9')
        cat10 = request.POST.getlist('cat10')
        cat11 = request.POST.getlist('cat11')
        cat12 = request.POST.getlist('cat12')
        if len(cat0) != 0:
            fcategory.append(cat0[0])
        if len(cat1) != 0:
            fcategory.append(cat1[0])
        if len(cat2) != 0:
            fcategory.append(cat2[0])
        if len(cat3) != 0:
            fcategory.append(cat3[0])
        if len(cat4) != 0:
            fcategory.append(cat4[0])
        if len(cat5) != 0:
            fcategory.append(cat5[0])
        if len(cat6) != 0:
            fcategory.append(cat6[0])
        if len(cat7) != 0:
            fcategory.append(cat7[0])
        if len(cat8) != 0:
            fcategory.append(cat8[0])
        if len(cat9) != 0:
            fcategory.append(cat9[0])
        if len(cat10) != 0:
            fcategory.append(cat10[0])
        if len(cat11) != 0:
            fcategory.append(cat11[0])
        if len(cat12) != 0:
            fcategory.append(cat12[0])
        print(fcategory)
        paper = papers.objects.get(p_id=paper_id)
        paper.category = fcategory
        paper.keywords = keywords
        paper.save()
        return redirect('/teacher/teacher')
    return render(request,"categories.html",context)