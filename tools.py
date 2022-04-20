import krpc
from krpc import Client

def get_connection():
    return krpc.connect(
    name='KRPC_CONNECTION',
    address='10.0.0.24',
    rpc_port=50000, stream_port=50001)

def get_vessel(connection:Client):
    return connection.space_center.active_vessel

def get_parts(connection:Client):
    return get_vessel(connection).parts.all

def wheels(c:Client):
    return [part for part in get_parts(c) if part.wheel is not None]

def en_parts(c:Client):
    return [part.title for part in get_parts(c)]

def parts_with_name(c:Client, name):
    l = []
    for part in get_parts(c):
        if name in part.title:
            l.append(part)
    return l

def en_modules(part):
    return [module.name for module in part.modules]

def module_with_name(part, name):
    for module in part.modules:
        if module.name == name:
            return module
    return None

connection = get_connection()
vessel = get_vessel(connection)
parts = get_parts(connection)


        






