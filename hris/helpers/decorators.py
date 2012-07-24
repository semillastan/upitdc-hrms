from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404
from functools import wraps

__all__ = [
  'render_to',
  'active_required',
  'ownership_required',
  'groups_required',
  'superuser_required',
]

def render_to(template):
    def outer(view_func):
        @wraps(view_func)
        def inner_html(request, *args, **kwargs):
            context = view_func(request, *args, **kwargs)
            if not context:
                context = {}
            if isinstance(context, HttpResponse):
                return context
            assert type(context) is dict, "View must return a type dict"
            return render_to_response(template, context, context_instance=RequestContext(request))
        return inner_html
    return outer

def active_required(klass, pk_field):
    def outer(view_func):
        @wraps(view_func)
        def inner_html(request, *args, **kwargs):
            instance_pk = kwargs.get(pk_field)
            instance = get_object_or_404(klass, pk=instance_pk)
            if hasattr(instance, 'is_active') and instance.is_active:
                return view_func(request, *args, **kwargs)
            raise Http404
        return inner_html
    return outer

def ownership_required(klass, pk_field):
    def outer(view_func):
        @wraps(view_func)
        def inner_html(request, *args, **kwargs):
            instance_pk = kwargs.get(pk_field)
            instance = get_object_or_404(klass, pk=instance_pk)
            if hasattr(instance, 'user') and instance.user == request.user:
                return view_func(request, *args, **kwargs)
            raise Http404
        return inner_html
    return outer
    
def groups_required(*groups):
    def in_groups(user):
        if user.is_authenticated() and bool(user.groups.filter(name__in=groups)):
            return True
        return False
    return user_passes_test(in_groups)


def superuser_required():
    return user_passes_test(lambda u: u.is_superuser)
    
