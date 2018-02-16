from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from notes.models import Post
from .forms import CreateForm
# Create your views here.

def index(request):
    #if request.method=='POST':
        # note_title = request.POST.get('title')
        # note_body = request.POST.get('body')
        # p = Post.objects.create(title=str(note_title),body=str(note_body))
        # return render(request, 'notes/index.html', {'data': p})
    # p = None
    #
    # if request.method == 'GET':
    #     return render(request, 'notes/index.html', {'objects': Post.objects.all()})

    if request.method == 'POST':
        note_title = request.POST.get('title')
        note_body = request.POST.get('body')
        p = Post.objects.create(title=note_title, body=note_body)
        return render(request, 'notes/index.html', {'objects': Post.objects.all()})


def create(request):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, 'notes/create.html', context)

def list(request):
    queryset = Post.objects.all()
    context = {
        "objects_list": queryset,
        "title": "List",
    }
    return render(request, 'notes/list.html',context)


def note_detail(request,id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "instance": instance,
    }
    return render(request, "notes/detail.html", context)


def note_edit(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = CreateForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "notes/create.html", context)


def note_delete(request,id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect('/notes/all')



