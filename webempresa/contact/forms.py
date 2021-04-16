from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre...'}
    ), min_length=3, max_length=100)
    correo_electronico = forms.EmailField(label="Correo electónico", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu correo electónico...'}
    ), min_length=3, max_length=100)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':3, 'placeholder':'Escribe tu mensaje...'}
    ), min_length=10, max_length=1000)