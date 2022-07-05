from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'

    def ready(self):
        import cart.signals  # noqa


# class ItemConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'item'
#
#     def ready(self):
#         import item.signals  # noqa
