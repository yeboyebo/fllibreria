# @class_declaration interna_CMD #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_CMD(modelos.mtd_CMD, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_CMD #
class fllibreria_CMD(interna_CMD, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration CMD #
class CMD(fllibreria_CMD, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.CMD_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
