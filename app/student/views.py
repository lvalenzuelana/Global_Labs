from django.shortcuts import render,redirect

# → Here you get the parameters to start searches within the database. 
# # The student can search by Title. 
# # Here some modifications could be made to search for other parameters.
def student(request):
    if request.method == 'POST':
        request.session['search'] = request.POST['search']
        request.session['input'] = request.POST['input']
        return redirect('/results/results')
    else: 
        return render(request,"student.html")