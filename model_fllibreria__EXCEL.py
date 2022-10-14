# @class_declaration interna_EXCEL #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_EXCEL(modelos.mtd_EXCEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_EXCEL #
class fllibreria_EXCEL(interna_EXCEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration EXCEL #
class EXCEL(fllibreria_EXCEL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.EXCEL_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
