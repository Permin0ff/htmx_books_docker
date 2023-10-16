from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.utils.translation import gettext_lazy as _
from django.core.cache import cache

from .models import Book
from .forms import BookCreateForm, BookEditForm


def delete_cache_keys():
    key_list = ['cached_book_list']
    for col in ('pk', 'title', 'author', 'price', 'read'):
        key_list += ['cached_book_list_sorted_' + col]
        key_list += ['cached_book_list_sorted_-' + col]
    cache.delete_many(key_list)


@require_http_methods(['GET'])
def book_list(request):
    book_list = cache.get_or_set('cached_book_list', Book.objects.all())
    # book_list = cache.get('cached_book_list')
    # if not book_list:
    #    book_list = Book.objects.all()
    #    cache.set('cached_book_list', book_list)
    form = BookCreateForm(auto_id=False)
    return render(request, '../templates/base.html', {'book_list': book_list, 'form': form})


@require_http_methods(['POST'])
def create_book(request):
    form = BookCreateForm(request.POST)
    if form.is_valid:
        book = form.save()
        delete_cache_keys()
    return render(request, '../templates/partial_book_detail.html', {'book': book})


def update_book_details(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            delete_cache_keys()
            return render(request, '../templates/partial_book_detail.html', {'book': book})
    else:
        form = BookEditForm(instance=book)
    return render(request, '../templates/partial_book_update_form.html', {'book': book, 'form': form})


@require_http_methods(['GET'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, '../templates/partial_book_detail.html', {'book': book})


@require_http_methods(['DELETE'])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    delete_cache_keys()
    return HttpResponse()


@require_http_methods(['PUT'])
def update_book_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.read:
        book.read = False
    else:
        book.read = True
    book.save()
    delete_cache_keys()
    # cache.delete('cached_book_list')
    return render(request, '../templates/partial_book_detail.html', {'book': book})


@require_http_methods(['GET'])
def book_list_sort(request, filter, direction):
    filter_dict = {_('id'): 'pk',
                   _('title'): 'title',
                   _('author'): 'author',
                   _('price'): 'price',
                   _('read'): 'read'}

    if filter in filter_dict:
        sort_str = ('-', '')[direction == _('ascend')] + filter_dict[filter]
        cache_key = 'cached_book_list_sorted_' + sort_str
        book_list = cache.get_or_set(cache_key, Book.objects.all().order_by(sort_str))
    else:
        book_list = cache.get_or_set('cached_book_list', Book.objects.all())

    return render(request, '../templates/partial_book_list.html', {'book_list': book_list})
