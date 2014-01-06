from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # session
    config.include('pyramid_beaker')

    # routes
    config.add_route('root', '/')
    config.add_route('home', '/home')
    config.add_route('json', '/json')
    config.add_route('string', '/string')
    
    # views
    # config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('static', 'static')
    config.scan()

    # wsgi
    return config.make_wsgi_app()
