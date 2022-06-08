from inspect import classify_class_attrs
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'