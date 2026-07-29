from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # Nou ajoute yon jaden kache pou parent_id a (si nou vle reponn yon kòmantè espesifik)
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ecrire votre commentaire...'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # Ajoute labels si ou vle
        self.fields['name'].label = "Nom"
        self.fields['email'].label = "Address Email"
        self.fields['body'].label = "commentaire"