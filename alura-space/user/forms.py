from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuário', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex.: João Silva', 'class': 'form-control'}
    ))
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}
    ))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label='Usuário', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Ex.: João Silva', 'class': 'form-control'}
    ))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Ex.: joaosilva@xpto.com', 'class': 'form-control'}
    ))
    password1 = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Digite sua senha', 'class': 'form-control'}
    ))
    password2 = forms.CharField(label='Confirmação de Senha', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirme sua senha', 'class': 'form-control'}
    ))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.strip()
            if ' ' in username:
                raise forms.ValidationError('O nome de usuário não pode conter espaços.')
            else:
                return username
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('As senhas não coincidem.')
        
        return cleaned_data