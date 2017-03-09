from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import Post
from .forms import PostForm

def createPost(request):
    if not request.user.is_authenticated():
        return redirect('users:index')

    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            content = post_form.cleaned_data['content']
            postModel = Post(id=None, title=title, content=content, date_published=datetime.now(),
                             author=request.user)
            postModel.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('users:blog', args=(request.user.id,)))

    else:
        post_form = PostForm()

    return render_to_response('post/createPost.html', {'form': post_form}, context_instance=RequestContext(request))


def editPost(request, post_id):
    if not request.user.is_authenticated():
        return redirect('users:index')

    post_model = get_object_or_404(Post, pk=post_id)
    if not post_model.author.id == request.user.id:
        return redirect('users:index')

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_model.title = post_form.cleaned_data['title']
            post_model.content = post_form.cleaned_data['content']
            post_model.save()
            return HttpResponseRedirect(reverse('users:blog', args=(request.user.id,)))
    else:
        post_form = PostForm(instance=post_model)

    return render_to_response('post/createPost.html', {'form': post_form}, context_instance=RequestContext(request))



def removePost(request, post_id):
    if not request.user.is_authenticated():
        return redirect('users:index')

    model = get_object_or_404(Post, pk=post_id)
    if not model.author.id == request.user.id:
        return redirect('users:index')

    model.delete()
    return HttpResponseRedirect(reverse('users:blog', args=(request.user.id,)))
