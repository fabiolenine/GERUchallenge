from sqlalchemy import engine_from_config
from model.models import DBSession

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)