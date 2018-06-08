from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPError
from myproject import views


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('raise_400', '/raise_400')
    config.add_view(views.error_view, context=HTTPError)
    config.scan()
    return config.make_wsgi_app()
