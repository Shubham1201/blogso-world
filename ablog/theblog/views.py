from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
#     return render(request, 'home.html')

def CategoryView(request, cats):
    category_post = Post.objects.filter(category = cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_post': category_post})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('artical-detail', args=[str(pk)]))

# def DislikeView(request, pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_dislike_id'))
#     disliked = False

#     if post.dislikes.filter(id=request.user.id).exists():
#         post.dislikes.remove(request.user)
#         disliked = False
#     else:
#         post.dislikes.add(request.user)
#         disliked = True    
    
#     return HttpResponseRedirect(reverse('artical-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date'] # newest post first
    # ordering = ['-id'] 
    #  last time post uploaded will be show friet but in ['id'] oldest post will show first but date-time wise is more good.

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class  ArticalDeatilView(DetailView):
    model = Post
    template_name = 'artical_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticalDeatilView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        # total_dislikes = stuff.total_dislikes()

        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        
        # disliked = False
        # if stuff.dislikes.filter(id=self.request.user.id).exists():
        #     disliked = True

        # if liked == True and disliked == True:
        #     liked = False
            
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        # context["total_dislikes"] = total_dislikes
        # context["disliked"] = disliked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    # fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    