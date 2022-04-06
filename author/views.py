from django.shortcuts import render, redirect
from .forms import AuthorForm
from .models import Author


# Create your views here.

def authors_update(request, id=0):

    if request.method == 'POST':
        if id == 0:
            form = AuthorForm(request.POST)
            button_submit = 'Add'
        else:
            form = AuthorForm(request.POST, instance=Author.get_by_id(id))
            button_submit = 'Update'

        if form.is_valid():
            return redirect('/book/')

    else:
        if id == 0:
            form = AuthorForm()
            button_submit = 'Add'
        else:
            form = AuthorForm(instance=Author.get_by_id(id))
            button_submit = 'Update'
    content = {
        'form': form,
        'button_submit':button_submit
        }
    return render(request, 'add_author.html', content)


def author_list(request):
    pass