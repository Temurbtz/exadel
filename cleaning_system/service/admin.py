from django.contrib import admin

from  .models  import Service,  Category

admin.site.register([Service, Category])
