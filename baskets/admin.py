from django.contrib import admin

from baskets.models import Basket


class BasketAdmin(admin.TabularInline):
    """Позволяет показать корзину товара в классе User, в его профиле.
    необходимо дописать атрибут в класс User!
    необходим FK между моделями User и Basket
    """
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
