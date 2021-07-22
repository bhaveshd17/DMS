from django.shortcuts import redirect,HttpResponse


def unauthenticated_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('placementIndex')
            else:
                return redirect('index')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                 return view_function(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')

        return wrapper_function
    return decorator

def allowed_admin(view_function):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Student':
            return redirect('index')

        if group == 'Placement_Cell':
             return view_function(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view thi page')

    return wrapper_function