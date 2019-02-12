from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="usuario")
    password = forms.CharField(label="senha", widget=forms.PasswordInput)


class NovoRegistroForm(forms.Form):
    username = forms.CharField(max_length=50, label="usuario")
    password = forms.CharField(max_length=20, label ="senha", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="confirmar senha", widget=forms.PasswordInput)
    
    def limpar(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("verifique a senha informada")

        values = {
            "username" : username,
            "password" : password
        }
        return values


