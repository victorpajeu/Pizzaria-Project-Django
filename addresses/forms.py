from django import forms
from addresses.models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('street', 'number', 'neighborhood', 'city', 'country', )