from django.contrib import admin
from .models import Author, Blog, Category


admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Category)

