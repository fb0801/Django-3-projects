from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages


# Create your views here.
def index(request):
    #adding todo object
    todo= Todo.objects.all() #displays all items
    if request.method =='POST':

        queryset = Todo.objects.all().values()
        if queryset == False:

            new_todo = Todo(
            title = request.POST['title']
            )
            new_todo.save()
            return redirect('/')
        else:
            messages.error(request, 'Item already exists')
            return redirect('/')
    
    return render(request, 'index.html', {'todos':todo})


def delete(request, pk):
    #delete todo object
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/') #return user to homepage