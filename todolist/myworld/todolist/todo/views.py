from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    #adding todo object
    todo= Todo.object.all()
    if request.method =='POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')
    
    return render(request, 'index.html', {'todos':todo})


def delete(request, pk):
    #delete todo object
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/') #return user to homepage