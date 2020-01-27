from django import forms
from .models import Todo


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'متن تایپ کنید',
            'aria-label': 'todo',
            'aria-describedby': 'add-btn'
        }))


class newTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'متن تایپ کنید',
                    'aria-label': 'todo',
                    'aria-describedby': 'add-btn'
                })
        }
