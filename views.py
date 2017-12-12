from uuid import uuid4
from pyramid.response import Response
from pyramid.view import view_config
from model.models import DBSession, LogModel
import transaction
import json, datetime
import quoteslib as q

def gen_save_idsession(session, path):
    value = session
    if 'id' in session:
        print('Registra no banco a requisição')
    else:
        print('ID da session gerado.')
        value['id'] = str(uuid4())

    # DBSession.begin()
    DBSession.add(LogModel(idsession=value['id'], endpoint=path))
    transaction.commit()

    return value

def datetime_handler(pdate):
    if isinstance(pdate, datetime.datetime):
        return pdate.isoformat()

# First view, available at http://localhost:8080/
@view_config(route_name='home', renderer='./templates/index.jinja2')
def home(request):
    session = gen_save_idsession(request.session, request.current_route_url())
    return dict(nome='Fabio Lenine')

@view_config(route_name='quotes', renderer='./templates/quotes.jinja2')
def quotes(request):
    session = gen_save_idsession(request.session, request.current_route_url())
    retorno = q.get_quotes()
    return dict(frases=retorno['quotes'])

@view_config(route_name='values', renderer='./templates/value.jinja2')
def quotes_values(request):
    # print('Passei por aqui...')
    session = gen_save_idsession(request.session, request.current_route_url())
    retorno = q.get_quote(request.matchdict)
    return dict(frase=retorno)

@view_config(route_name='consultas', renderer='jsonp')
def consultas(request):
    retorno = DBSession.query(LogModel).all()
    json_string = json.dumps([ob.__dict__ for ob in retorno], default=datetime_handler)
    return Response(json_body=json.loads(json_string))
