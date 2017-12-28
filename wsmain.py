from wsgiref.simple_server import make_server
from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from model.models import DBSession, Base

my_session_factory = SignedCookieSessionFactory ('kvbjoeifHG4woi7rtc3ndxhq3x0xj398HR47yroq3dj93r98yriwxhiuhd7teu7e')
settings = {'sqlalchemy.url': 'sqlite:///./database/logurlaccess.db', 'sqlalchemy.echo': 'True'}

if __name__ == '__main__':
    with Configurator ( ) as config:
        engine = engine_from_config (settings, 'sqlalchemy.')
        DBSession.configure (bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all (engine)

        config.add_route ('home', '/')
        config.add_route ('quotes', '/quotes')
        config.add_route ('values', '/quotes/{value}')
        config.add_route ('consultas', '/consultas')

        config.set_session_factory (my_session_factory)
        config.include ('pyramid_jinja2')
        config.scan ('views')
        app = config.make_wsgi_app ( )

    server = make_server ('0.0.0.0', 8080, app)
    server.serve_forever ( )
