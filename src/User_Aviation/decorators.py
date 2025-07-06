from django.shortcuts import redirect







def notLoggedUsers(view_func):
    def wrapper_func(request , *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return view_func(request , *args,**kwargs)
    return wrapper_func
    




def allowedUsersAV(allowedUsers=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group in allowedUsers:
               return view_func(request , *args,**kwargs)
            else:
                return redirect('loginAV')
            
        return wrapper_func
    return decorator