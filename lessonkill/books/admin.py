from django.contrib import admin

# Register your models here.

from lessonkill.books.models import Publisher, Author, Book, Account

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date', )

class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'signature', 'logintime')
    list_filter = ('username', )

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Account, AccountAdmin)

