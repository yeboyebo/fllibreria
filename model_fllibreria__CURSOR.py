# @class_declaration interna_CURSOR #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_CURSOR(modelos.mtd_CURSOR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_CURSOR #
class fllibreria_CURSOR(interna_CURSOR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration CURSOR #
class CURSOR(fllibreria_CURSOR, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.CURSOR_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
