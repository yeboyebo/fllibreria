# @class_declaration interna_LOG #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_LOG(modelos.mtd_LOG, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_LOG #
class fllibreria_LOG(interna_LOG, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration LOG #
class LOG(fllibreria_LOG, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.LOG_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
