from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        # article.pk는 사용자가 보지 못해야한다. 그래서 exclude로 작성할 수 있는
        # Modelform을 한정한다.
        fields = ('content',)