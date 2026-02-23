from django import forms
from apps.gallery.models import Image

# Esse método cria um formulário com base no models
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['published',]
        labels = {
            'name': 'Nome',
            'legend': 'Legenda',
            'category': 'Categoria',
            'description': 'Descrição',
            'photo': 'Foto',
            'image_date': 'Data da Imagem',
            'user': 'Usuário',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'legend': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'image_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }