from django import forms
from .models import Article

# forms에는 textfield없음

# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'cr'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본')
#     ]
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)

# 위젯은 DB에 영향을 주지 않음

class ArticleForm(forms.ModelForm):
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
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 30,
            }
        ),
        error_messages={
            'required' : 'Please enter your content',
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)