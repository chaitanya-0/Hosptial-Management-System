from admin_app import models

def check_user_priviledge(request):
    data = models.admin_user.objects.filter(isadmin=True).values('user_id', 'isadmin')
    check=False
    if request.user.is_authenticated:
        username = request.user.username
        data = list(data)
        check_dict = next((item for item in data if item["user_id"] == username), None)
        if check_dict:
            check=True
            return {'is_user_admin': check}  
             
    return {'is_user_admin': check}