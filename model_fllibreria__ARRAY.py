# @class_declaration interna_ARRAY #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_ARRAY(modelos.mtd_ARRAY, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_ARRAY #
class fllibreria_ARRAY(interna_ARRAY, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration ARRAY #
class ARRAY(fllibreria_ARRAY, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.ARRAY_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
