from django import forms

class LoginForms(forms.Form):
    name_login=forms.CharField(
        label='Login name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User name',
            }
        )
    )
    password=forms.CharField(
        label='password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Type your password',
            }
        )
    )

class Registerforms(forms.Form):
    name_register=forms.CharField(
        label='Register name',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User name',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'User email',
            }
        )
    )
    password_1=forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'type your password',
            }
        )
    )
    password_2=forms.CharField(
        label='Confirm your password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'forms-control',
                'placeholder': 'Type your password again',
            }
        )
    )
    identity=forms.CharField(
        label='id',
        required=True,
        min_length=15,
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'class': 'forms-control',
                'placeholder': 'Type your id',
            }
        )
    )

    def clean_name_register(self):
        name = self.cleaned_data.get('name_register')

        if name:
            name = name.strip()
            if ' ' in name:
                raise forms.ValidationError('Espaces are not allowed in this field!')
            else:
                return name
    def clean_password(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2:
            if password_1 != password_2:
                raise forms.ValidationError('Passwords are not equal!')
            else:
                return password_2