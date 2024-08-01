from django.contrib.auth.models import User

admin_username = 'admin'
admin_password = '440856Mo'
admin_email = 'admin@admin.com'

if not User.objects.filter(username=admin_username).exists():
    User.objects.create_superuser(admin_username, admin_email, admin_password)
    print("Superuser created")
else:
    print("Superuser already exists")
