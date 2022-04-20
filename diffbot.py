import tools
import controller

from tools import connection as c, parts_with_name

#First find all the wheels

wheels = parts_with_name(c, 'Rotatron - Basic')

print([part.title for part in wheels])