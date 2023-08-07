from django.contrib import admin

# NOTE: Tenemos que importar los modelos con los que vamos a trabajar:
from e_commerce.models import Comic, WhishList

# Register your models here.

# NOTE: Aquí personalizamos los campos en el Django Admin.

@admin.register(Comic)
class ComicsAdmin(admin.ModelAdmin):
    # NOTE: Para seleccionar los campos en la tabla de registros
    list_display = ('marvel_id', 'title', 'stock_qty', 'price')

    # NOTE: Filtro lateral de elementos:
    list_filter= ('marvel_id','title')
    
    # NOTE: Buscador de elementos en la columna:
    search_fields = ['title']

    # NOTE: Para seleccionar los campos en el registro. 
    # fields = ('marvel_id', 'title', 'stock_qty')

    # NOTE: Genera un campo desplegable con los registros seleccionados.
    fieldsets = (
         (None, {
             'fields': ('marvel_id', 'title', 'stock_qty')
         }),
         ('Advanced options', {
             'classes': ('collapse',),
             'fields': ('description','price', 'picture'),
         }),
    )

@admin.register(WhishList)
class WhishListAdmin(admin.ModelAdmin):
    list_display = ('user','comic','favorite','cart','wished_qty','bought_qty')
    search_fields = ['comic']
    fieldsets = (
         (None, {
             'fields': ('user', 'comic', 'wished_qty', 'bought_qty')
         }),
         ('Advanced options', {
             'classes': ('collapse',),
             'fields': ('favorite', 'cart'),
         }),
    )


