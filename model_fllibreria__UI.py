# @class_declaration interna_UI #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_UI(modelos.mtd_UI, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_UI #
class fllibreria_UI(interna_UI, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration UI #
class UI(fllibreria_UI, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.UI_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
