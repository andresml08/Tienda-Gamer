from django.contrib import admin
from .models import Order, OrderLine

admin.site.register([Order, OrderLine])