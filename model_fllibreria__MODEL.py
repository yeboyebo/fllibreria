# @class_declaration interna_MODEL #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_MODEL(modelos.mtd_MODEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_MODEL #
class fllibreria_MODEL(interna_MODEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration MODEL #
class MODEL(fllibreria_MODEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.MODEL_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
