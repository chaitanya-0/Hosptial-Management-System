from admin_app import models

data = models.admin_user.objects.filter(isadmin=True).values()
print(data)