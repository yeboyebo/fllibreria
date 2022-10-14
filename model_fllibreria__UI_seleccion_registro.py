# @class_declaration interna_UI_seleccion_registro #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_UI_seleccion_registro(modelos.mtd_UI_seleccion_registro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_UI_seleccion_registro #
class fllibreria_UI_seleccion_registro(interna_UI_seleccion_registro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration UI_seleccion_registro #
class UI_seleccion_registro(fllibreria_UI_seleccion_registro, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.UI_seleccion_registro_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
