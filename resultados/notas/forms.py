from django import forms

class NotasForm(forms.Form):
    matematicas_o_historia = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        min_value=0,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )

    lengua_y_litertura = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        min_value=0,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )

    idioma = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        min_value=0,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )

    prueba_especifica = forms.DecimalField(
        max_digits=4,
        decimal_places=1,
        min_value=0,
        max_value=10,
        required=True,
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )
