from django.shortcuts import redirect, HttpResponse
from typing import Callable, TypeVar, ParamSpec, LiteralString

P = ParamSpec('P')
R = TypeVar('R')

def unauthenticated_user(view_function: Callable[P, R]) -> Callable[P, R]:
    def wrapper_function(request, *args: P.args, **kwargs: P.kwargs) -> R:
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('placementIndex')
            else:
                return redirect('index')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function

def allowed_users(allowed_roles: list[LiteralString] = []) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(view_function: Callable[P, R]) -> Callable[P, R]:
        def wrapper_function(request, *args: P.args, **kwargs: P.kwargs) -> R:
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                try:
                    raise PermissionError('You are not authorized to view this page')
                except PermissionError as e:
                    e.add_note(f"User group: {group}, Allowed roles: {allowed_roles}")
                    return HttpResponse(str(e))

        return wrapper_function
    return decorator

def allowed_admin(view_function: Callable[P, R]) -> Callable[P, R]:
    def wrapper_function(request, *args: P.args, **kwargs: P.kwargs) -> R:
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Student':
            return redirect('index')

        if group == 'Placement_Cell':
            return view_function(request, *args, **kwargs)
        else:
            try:
                raise PermissionError('You are not authorized to view this page')
            except PermissionError as e:
                e.add_note(f"User group: {group}")
                return HttpResponse(str(e))

    return wrapper_function
