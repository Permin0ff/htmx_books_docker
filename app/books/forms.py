from django import forms 
from django.utils.translation import gettext_lazy as _  # new

from .models import Book


class BookCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": _("Title"),
            }
        ),
    )
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": _("Author"),
            }
        ),
    )
    price = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "disbtn form-control",
                "placeholder": _("Price"),
            }
        ),
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']


class BookEditForm(BookCreateForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    price = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
