# @class_declaration interna_TBL #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_TBL(modelos.mtd_TBL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_TBL #
class fllibreria_TBL(interna_TBL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration TBL #
class TBL(fllibreria_TBL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.TBL_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
