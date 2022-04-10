from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewsForm





class NewsList(ListView):

    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['dateCreation']
    paginate_by = 3



# Create your views here.

#для просмотра поста
class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'searchpost'
    ordering = ['dateCreation']

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


#Для редактирования поста
class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = NewsForm


class PostUpdateView(UpdateView):
    template_name = 'post_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'



