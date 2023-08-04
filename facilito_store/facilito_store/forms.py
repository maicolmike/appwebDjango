from django import forms
#from django.contrib.auth.models import User
from users.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=50,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'id': 'username',
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                             'id': 'email',
                                                             'placeholder': 'Email'}))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'id': 'password',
                                                             'placeholder': 'Password'}))
    password2 = forms.CharField(label= 'Confirmar password',
                                required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'id': 'password',
                                                             'placeholder': 'Password'}))
    
    #usuario no se repita y no genere error
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=username).exists() :
            raise forms.ValidationError("el usuario ya se encuentra creado")
        
        return username
    
    def clean_email(self): #habilito que el correo sea unico, si quito esta funcion se peude tener el mismo correo en otros usuarios
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists() :
            raise forms.ValidationError("el email ya se encuentra creado")
        
        return email
    #se sobreescribe el metodo clean solo si debemos validar una condicion que dependa de otra
    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'Las contraseñas no coinciden')
    
    def save(self):
        return User.objects.create_user(
        self.cleaned_data.get('username'),
        self.cleaned_data.get('email'),
        self.cleaned_data.get('password')
        )