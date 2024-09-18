from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Nome de Usuário', 
                                 required=True, 
                                 max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Ex.: Joao Silva',
                                     },
                                     ),
                                 )
    senha = forms.CharField(label='Senha', 
                            required=True,
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 
                                'placeholder': 'Ex.: Joao Silva',
                                }
                                ),
                            )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de Cadastro', 
                                 required=True, 
                                 max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Ex.: Joao Silva',
                                     },
                                     ),
                                 )
    
    email= forms.EmailField(label="Email", required=False, max_length=100, 
                            widget=forms.EmailInput(attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Ex.: JoaoSilva@gmail.com',
                                     },))

    senha = forms.CharField(label='Senha', 
                            required=True,
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 
                                'placeholder': 'Digite sua senha',
                                }
                                ),
                            )
    
    repetir_senha = forms.CharField(label='Repetir Senha', 
                            required=True,
                            max_length=70, 
                            widget=forms.PasswordInput(
                                attrs={'class': 'form-control', 
                                'placeholder': 'Confirme sua senha',
                                }
                                ),
                            )