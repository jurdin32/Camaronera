from io import  BytesIO
import os

from django.conf import settings
from future.backports.datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


def Attr(cls):
    model= cls.__name__
    return cls.__doc__.replace(model,"").replace("(","").replace(")","").replace(" ","").split(",")


def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    return path


def render_to_pdf(template_src,context_dict={}):
    template=get_template(template_src)
    html=template.render(context_dict)
    result=BytesIO()
    pisa.pisaDocument(BytesIO(html.encode("utf8")),result,link_callback=fetch_resources)
    return HttpResponse(result.getvalue(),content_type="application/pdf")

def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)


def obtener_dias_del_mes(mes: int, anio: int) -> int:
    una_fecha = '01/%s/2022'%str.zfill(str(mes),2)
    fecha_dt = datetime.strptime(una_fecha, '%d/%m/%Y')
    dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]
    print(dias[fecha_dt.weekday()],fecha_dt.weekday())
    if mes in [4, 6, 9, 11]:
        return 30
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        return 31


dias = obtener_dias_del_mes(datetime.now().month, datetime.now().year)
print("Este mes tiene:",dias)