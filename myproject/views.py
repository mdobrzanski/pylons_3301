from pyramid.httpexceptions import HTTPBadRequest
from pyramid.renderers import render_to_response
from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.mako')
def my_view(request):
    return {'project': 'MyProject'}


@view_config(route_name='raise_400')
def raise_error_view(request, context):
    """Raises HTTP 400."""
    raise HTTPBadRequest(detail=u'HTTP 400: Yata yata yata')


def error_view(exc, request):
    """Customized error page."""
    data = {"msg": unicode(exc)}
    return render_to_response('templates/exception.mako', data, request=request)
