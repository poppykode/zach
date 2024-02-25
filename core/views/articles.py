from django.shortcuts import get_object_or_404,  render
from django.core.paginator import Paginator
from core.models import Article

def articles(request):
    template_name = 'articles/articles.html'
    articles_ = Article.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(articles_, 9)
    articles = paginator.page(page)
    context = {
        'articles':articles,
    }
    return render(request, template_name, context)

def article_details(request,slug):
    template_name = 'articles/article_details.html'
    article = get_object_or_404(Article,slug=slug)
    return render(request, template_name, { 'obj':article})