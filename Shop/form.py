from django import forms
from .models import OrderProduct

class orderform(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields =('product','customer_Id')
        fields = '__all__'