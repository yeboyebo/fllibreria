# @class_declaration interna_STR #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_STR(modelos.mtd_STR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_STR #
class fllibreria_STR(interna_STR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration STR #
class STR(fllibreria_STR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.STR_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
