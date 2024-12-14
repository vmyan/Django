from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scopes


class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tag_count += 1
        
        if main_tag_count != 1:
            raise ValidationError('Должен быть указан только один основной тег.')
        
        return super().clean()


class ScopesInline(admin.TabularInline):
    model = Scopes
    formset = ScopesInlineFormset  
    extra = 1  


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopesInline]  


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scopes)
class ScopesAdmin(admin.ModelAdmin):
    pass
