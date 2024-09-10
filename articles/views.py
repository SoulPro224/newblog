from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Article_form, CommentForm
from .models import Article, Comment
from django.core.exceptions import PermissionDenied


class ArticleListView(ListView):
    model = Article
    template_name = 'article/list_article.html'
    context_object_name = 'article'
    
    def get_success_rul(self):
        return reverse('article:list_article')
    

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = Article_form
    template_name = 'article/formulaireArticle.html'

    def form_valid(self, form):
        # Définir l'auteur automatiquement à l'utilisateur connecté
        article = form.save(commit=False)
        article.auteur = self.request.user
        article.save()
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        # Optionnel : afficher les erreurs pour déboguer
        print("Le formulaire est invalide")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('article:list_article')



# class ArticleCreateView(LoginRequiredMixin,CreateView):
#     model = Article
#     form_class = Article_form
#     template_name = 'article/formulaireArticle.html'
    
#     def get_success_url(self):
#         return reverse('article:list_article')
    

class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model = Article
    form_class = Article_form
    template_name = 'article/updateArticle.html'
    
    def get_success_url(self):
        return reverse('article:list_article')

# class ArticleUpdateView(LoginRequiredMixin, UpdateView):
#     model = Article
#     form_class = Article_form
#     template_name = 'article/updateArticle.html'

#     def dispatch(self, request, *args, **kwargs):
#         article = self.get_object()
#         if article.auteur != self.request.user:
#             raise PermissionDenied("Vous n'êtes pas autorisé à modifier cet article.")
#         return super().dispatch(request, *args, **kwargs)

#     def get_success_url(self):
#         return reverse('article:list_article')

class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article/confirm_delete.html' 
    
    def get_success_url(self):
        return reverse('article:list_article')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.object)
        return context
    
    
class AddCommentView(LoginRequiredMixin,View):
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm()
        return render(request, 'article/add_comment.html', {'form': form, 'article': article})

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article:article_detail', pk=article.pk)
        return render(request, 'article/add_comment.html', {'form': form, 'article': article})
    
    
