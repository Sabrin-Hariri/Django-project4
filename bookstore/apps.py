from django.apps import AppConfig


class BookstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookstore'
    


    ##### محتاج سجل السجنل بالتطبيق تاعي 

    def ready(self):
        import bookstore.signals


    ######