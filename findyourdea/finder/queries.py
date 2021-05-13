from .models import Dea
import json
import utm

class DEA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, user_x, user_y):
        c1 = (user_x - self.x) ** 2
        c2 = (user_y - self.y) ** 2
        return (c1+c2)**0.5
    
    def __str__(self):
        return "working"

def get_data(fichero):
    with open(fichero,encoding="utf8") as file:
        return json.load(file)["data"]

def get_nearest_dea(user_lat, user_long, dataset):
    user_xy = utm.from_latlon(user_lat, user_long)
    result = None
    first_dea = dataset[0]
    first_dea_object = DEA(first_dea.x_utm, first_dea.y_utm)
    distance_to_beat = first_dea_object.distance(user_xy[0], user_xy[1])

    for dea in dataset:
        dea_object = DEA(dea.x_utm, dea.y_utm)
        dea_distance = dea_object.distance(user_xy[0], user_xy[1])
        if dea_distance <= distance_to_beat:
            result = dea
            distance_to_beat = dea_distance
        else:
            continue
    dea_latlng = utm.to_latlon(result.x_utm,result.y_utm,30, "N")
    return result, dea_latlng

def insert_into(dataset):
    for dea in dataset:
        Dea.objects.create(codigo_dea=dea["codigo_dea"],
                        direccion_ubicacion = dea["direccion_ubicacion"],
                        direccion_portal_numero = dea["direccion_portal_numero"],
                        horario_acceso=dea["horario_acceso"],
                        x_utm = int(dea["direccion_coordenada_x"]),
                        y_utm = int(dea["direccion_coordenada_y"])
                            )

