from django.contrib import admin

from .models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display= ["id","name","email","password"]
    list_editable= ["email","name"]
    search_fields = ["name"]

    
admin.site.register(Users,UsersAdmin)
