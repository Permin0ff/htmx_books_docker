from django.forms import ModelForm, CharField, TextInput
from .models import Book
from django.utils.translation import gettext_lazy as _ # new


class BookCreateForm(ModelForm):
    title  = CharField(label='qwerty', required=False, widget=TextInput(attrs={"class":"clrtxt", "placeholder":_("Title")}))
    author = CharField(required=False, widget=TextInput(attrs={"class":"clrtxt", "placeholder":_("Author")}))
    price  = CharField(required=False, widget=TextInput(attrs={"class":"clrtxt", "placeholder":_("Price")}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']

class BookEditForm(BookCreateForm):
    title  = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
    author = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
    price  = CharField(required=False, widget=TextInput(attrs={"class":"form-control-sm form-control"}))
