from django import forms
from .models import Cliente

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(label="Mensaje")
    
class RegistroClienteForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    contraseña_confirmación = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'contraseña']

    def clean_contraseña_confirmación(self):
        contraseña = self.cleaned_data.get('contraseña')
        contraseña_confirmación = self.cleaned_data.get('contraseña_confirmación')
        if contraseña and contraseña_confirmación and contraseña != contraseña_confirmación:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return contraseña_confirmación
    
