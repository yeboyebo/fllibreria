# @class_declaration interna_HTTP #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_HTTP(modelos.mtd_HTTP, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_HTTP #
class fllibreria_HTTP(interna_HTTP, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration HTTP #
class HTTP(fllibreria_HTTP, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.HTTP_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
