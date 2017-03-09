from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, render_to_response
from django.template import RequestContext
from .forms import UserForm
from .models import Post
from .models import UserInfo
from .models import profile_pic_path


def index(request):
    user_list = UserInfo.objects.all()
    return render(request, 'SIB.html/', {'user_list': user_list})

def userBlog(request, user_id):
    post_list = get_list_or_404(Post.objects.order_by('-date_published'), author=user_id)
    #post_list = Post.objects.order_by('-date_published').filter(author=user_id)
    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, 'users/blog.html', {'post_list': posts})

def editUser(request):
    if not request.user.is_authenticated():
        return redirect('users:index')

    user_model = get_object_or_404(UserInfo, pk=request.user.userinfo.id)

    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_model.name = user_form.cleaned_data['name']
            user_model.surname = user_form.cleaned_data['surname']
            request.user.email = user_form.cleaned_data['email']
            request.user.save()
            user_model.phone = user_form.cleaned_data['phone']
            user_model.about = user_form.cleaned_data['about']
            if user_form.cleaned_data['profile_image'] is not None:
                user_model.profile_image = user_form.cleaned_data['profile_image']
            profile_pic_path(request.user, 'something')
            user_model.save()

            return HttpResponseRedirect(reverse('users:blog', args=(request.user.id,)))

    else:
        user_form = UserForm(instance=user_model)
        user_form.initial['email'] = request.user.email

    return render_to_response('users/editUser.html', {'user_form': user_form}, context_instance=RequestContext(request))
