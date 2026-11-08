from django.contrib import admin

from .models import Product, Customer, Order, OrderItems, ShippingAddress, Category
import datetime
from django.utils import timezone

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ShippingAddress)
admin.site.register(Category)



# تغيير النص في شريط العنوان الخاص بالمتصفح
admin.site.site_title = "Jadeer"

# تغيير النص الرئيسي الأزرق في أعلى الصفحة
admin.site.site_header = "Jadeer"

# تغيير النص الترحيبي في صفحة تسجيل الدخول (اختياري)
admin.site.index_title = "مرحباً بك في لوحة الإدارة"

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'status', 'price', 'created_at','product', 'quantity', 'get_total')

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price','product', 'quantity', 'get_total')