from django.apps import AppConfig



class MysiteblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysiteblog'

    def ready(self):
        import mysiteblog.signals  
