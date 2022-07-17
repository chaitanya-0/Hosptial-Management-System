from admin_app import models

def check_user_priviledge(request):
    data = models.admin_user.objects.filter(isadmin=True).values('user_id', 'isadmin')
    check=False
    if request.user.is_authenticated:
        username = request.user.username
        data = list(data)
        check_dict = next((item for item in data if item["user_id"] == username), None)
        print(check_dict)
        print(data)
        return {'is_user_admin': check}
    else:
        return {'is_user_admin':check}