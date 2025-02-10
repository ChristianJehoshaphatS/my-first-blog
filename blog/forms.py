from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model= Post
        fields = ('title','text')
        
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('title') != cleaned_data.get('title').upper():
            raise forms.ValidationError('Title Must be uppercase')
        
        return self.cleaned_data
    
    def clean_text(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        if len(text) >= 100:
            raise forms.ValidationError('Text must be less than 100 characters')
        return text
    
    

# PR: Post form pakai forms.Form biasa, nggak pakai ModelForm
from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=200,  # Increased max length for author name
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}) #nice input field with placeholder
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 3}) #nice textarea input field with placeholder
    )
