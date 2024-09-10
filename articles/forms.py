from django import forms
from .models import Article, Comment

class Article_form(forms.ModelForm):
    # title = forms.CharField(min_length=2, max_length=255)
    # somary = forms.CharField(min_length=2, max_length=255)
    # date_pu = forms.DateField()
    # content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Article
        fields = ['title', 'somary', 'content', 'date_pu', 'image'] 
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "date_pu": forms.TextInput(attrs={'class': 'form-control',"type":"date"}),
            "somary": forms.TextInput(attrs={'class': 'form-control'}),
            "image": forms.ClearableFileInput()
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }