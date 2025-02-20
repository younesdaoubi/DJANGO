from django.http import request, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Situation

# Create your views here.
def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts,
    }
    return render(request,'Immo/post_favourite_list.html', context)




def search_posts(request):
    if request.method == "POST":
        searched = request.POST['searched']

        search_content = Post.objects.filter(content__contains=searched)
        search_title = Post.objects.filter(title__contains=searched)
        return render(request, 'Immo/search.html', {'searched': searched, 'search_content': search_content, 'search_title': search_title })
    else:
        return render(request, 'Immo/search.html', {})


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Immo/home.html', context)  # methode render, premier param request, 2e fichier.


class PostListView(ListView):
    model = Post
    template_name = 'Immo/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # afficher premier post par en bas
    paginate_by = 5


class UserPostListView(ListView):  # pour filter
    model = Post
    template_name = 'Immo/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post




    def favourite_post(request, id):


        #is_favourite = False
        post = get_object_or_404(Post, id = id)

        is_favourite = False

        if post.favourite.filter(id=request.user.id).exists():
            is_favourite = True

        if post.favourite.filter(id=request.user.id).exists():
                post.favourite.remove(request.user)
        else:
            post.favourite.add(request.user)
        return HttpResponseRedirect(post.get_absolute_url())

            #is_favourite = True
        # if Post.favourite.filter(id=request.user.id).exists():






class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    situation = Situation.address
    fields = ['title', 'price', 'content', 'surface', 'image', 'situation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = ['title', 'price', 'content', 'surface', 'image', 'situation']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




    def test_func(
            self):  # pour update que ses posts, et non les posts des autres users on tulise le UserPassesTestMixin en haut
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # ligne qui renvoie direct a la page des blogs apres suppression d'un blog.

    def test_func(
            self):  # pour delete que ses posts, et non les posts des autres users on tulise le UserPassesTestMixin en haut
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'Immo/about.html', {'title': 'My About Page'})





