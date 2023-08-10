from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog


class BlogCreateView(CreateView):
    """Контроллер создания новой статьи"""

    model = Blog
    fields = ('title', 'description', 'creation_date', 'preview', 'is_published')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    """Контроллер просмотра списка статей"""

    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Вывод только опубликованные записи"""

        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    """Контроллер просмотра статьи"""

    model = Blog

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object


class BlogUpdateView(UpdateView):
    """Контроллер редактирования статьи"""

    model = Blog
    fields = ('title', 'description', 'creation_date', 'preview', 'is_published')

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.pk])


class BlogDelete(DeleteView):
    """Контроллер удаления статьи"""

    model = Blog
    success_url = reverse_lazy('blog:list')
    