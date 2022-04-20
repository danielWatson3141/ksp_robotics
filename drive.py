import time
import tools
import krpc
import controller


conn = tools.get_connection()
vessel = conn.space_center.active_vessel

parts = vessel.parts.all
piston = parts[2]
piston.modules[1].set_field_float("Target Position", 0.0)