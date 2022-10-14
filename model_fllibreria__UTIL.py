# @class_declaration interna_UTIL #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_UTIL(modelos.mtd_UTIL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_UTIL #
class fllibreria_UTIL(interna_UTIL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration UTIL #
class UTIL(fllibreria_UTIL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.UTIL_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
