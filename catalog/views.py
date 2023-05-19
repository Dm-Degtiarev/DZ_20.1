from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from catalog.models import Product, Contacts, Blog
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

#CBV
class IndexView(TemplateView):
    template_name = 'catalog/index.html'

class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Товары'
    }

class ProductDetailView(DetailView):
    model = Product

class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(blog_publicate_flg=True)

        return queryset

class BlogDetailView(DetailView):
    model = Blog

    def get_object(self):
        blog_slug = self.kwargs['blog_slug']
        obj = get_object_or_404(self.model, blog_slug=blog_slug)
        return obj

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return  context_data

    def get(self, request, *args, **kwargs):
        """Увеличивает счетчик просмотров статьи"""
        self.object = self.get_object()

        self.object.blog_views_count +=1
        self.object.save()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_name', 'blog_content', 'blog_image')
    success_url = reverse_lazy('catalog:blog')

class BlogUpdateView(UpdateView, BlogDetailView):
    model = Blog
    fields = ('blog_name', 'blog_content', 'blog_image')

    def get_success_url(self):
        blog = self.get_object()

        return reverse_lazy('catalog:blog_detail', kwargs={'blog_slug': blog.blog_slug})

class BlogDeleteView(DeleteView, BlogDetailView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')



#FBV
# def index(request):
#     return render(request, 'catalog/index.html')


# def products(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#
#     return render(request, 'catalog/product_list.html', context)


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': product_item
#     }
#
#     return render(request, 'catalog/product_detail.html', context)
