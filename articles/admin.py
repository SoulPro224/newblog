from django.contrib import admin
from .models import Article, Comment

class ArticleAdmin(admin.ModelAdmin):
    date_hierarchy = "date_pu"
    list_display = ["title", "somary", "date_pu","auteur"]
    # fields = ['title', 'somary','date_pu','auteur','image','content']
    fieldsets = [
        (
            None,
            {
                "fields": ["title","somary","date_pu","auteur"],
            },
        ),
        (
            "Description",  
            {
                "classes": ["collapse"],
                "fields": ["content","image"],
            },
        ),
    ]


admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)