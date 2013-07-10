from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from allegro.lib import allegro_api,NoItemException
from nokaut.lib import nokaut_api

@view_config(route_name='home', renderer='pyramid_app:templates/base.mako')
def my_view(request):
    return {}

@view_config(route_name = 'search', renderer = 'pyramid_app:templates/search.mako')
def res_view(request):
    search_phrase = request.GET.get('search_field')
    (all_link, all_price), (nok_link, nok_price), mode = _get_prices(search_phrase)

    if not mode:
        return HTTPFound('/not_found')
    else:
        return {'product_name' : search_phrase,
                'allegro_link' : all_link,
                'nokaut_link' : nok_link,
                'allegro_price' : all_price,
                'nokaut_price' : nok_price,
                'allegro_price_mode' : 'price win' if mode == 'a' else 'price',
                'nokaut_price_mode' : 'price win' if mode == 'n' else 'price'}

@view_config(route_name = 'not_found', renderer = 'pyramid_app:templates/not_found.mako')
def nof_found_view(request):
    return {}

def _get_prices(search_phrase):
    nokaut_key = 'a8839b1180ea00fa1cf7c6b74ca01bb5'

    try :
        all = allegro_api(search_phrase)
        nok = nokaut_api(search_phrase,nokaut_key)
    except NoItemException:
        return (None, None), (None, None), False
    # import ipdb; ipdb.set_trace()
    nok_price = nok[1]
    all_price = all[1]

    if all_price < nok_price:
        mode = 'a'
    else:
        mode = 'n'

    return all, nok, mode