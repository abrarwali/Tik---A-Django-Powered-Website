from django import forms
from .models import Discussion,Comments
from django.core.exceptions import ValidationError

class DiscussionForm(forms.ModelForm):
    class Meta:
        model=Discussion
        fields=['title','argument','slug']

class CommentsForm(forms.ModelForm):
    # username=forms.CharField(widget=forms.TextInput(attrs={
    # 'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
    # }))
    comment_text=forms.CharField(widget=forms.TextInput(attrs={
        'style': 'border-color:SteelBlue; border-radius: 7px; border-width: thin;',
        }))
    class Meta:
        model=Comments
        fields=['comment_text']
