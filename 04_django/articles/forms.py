from django import forms
from .models import Article

class ArticleForm(forms.Form):
    NATION_A = 'kr'
    NATION_B = 'cr'
    NATION_C = 'jp'
    NATION_CHOICES = {
        NATION_A : '한국',
        NATION_B : '중국',
        NATION_C : '일본',
    }
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATION_CHOICES, widget=forms.RadioSelect)
    
# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         field = '__all__'