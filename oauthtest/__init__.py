from pyramid.config import Configurator

from zope.interface import implementer

from pyramid_oauth2_provider.interfaces import IAuthCheck

from pyramid.authorization import ACLAuthorizationPolicy

@implementer(IAuthCheck)
class AuthChecker(object):
    def checkauth(self, username, password):
        return True

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    authorization_policy = ACLAuthorizationPolicy()
    config.set_authorization_policy(authorization_policy)
    config.include('pyramid_oauth2_provider')

    config.scan()
    return config.make_wsgi_app()
