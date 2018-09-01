from django import forms
from home.models import Comment

class CommentForm(forms.Form):

    comment = forms.CharField(
        required=True,
        label='Comentario:',
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe un comentario aqui...',
            'maxlength': 256,
            'rows':3,
            }
        ))

    def save(self, ip_address):
        cleaned_data = super(CommentForm, self).clean()
        comment = Comment()
        comment.text = cleaned_data['comment']
        comment.ip_address = ip_address
        comment.save()
        return comment
