from django import forms
from .models import Articles

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'JP'
#     NATIONS_CHOICE = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]
    
#     title = forms.CharField(max_length=10)
    
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICE)
    
class  ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content form-control',
                'placeholder' : 'Enter thr content',
                'cols' : 50,
                'rows' : 5,
            }
        ),
        error_messages={
            'required' : 'please enter content',
        }
    )
    
    class Meta:
        model = Articles
        fields = '__all__'