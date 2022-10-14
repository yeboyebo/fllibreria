# @class_declaration interna_MAVE #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_MAVE(modelos.mtd_MAVE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_MAVE #
class fllibreria_MAVE(interna_MAVE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration MAVE #
class MAVE(fllibreria_MAVE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.MAVE_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
