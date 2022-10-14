# @class_declaration interna_FILE #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_FILE(modelos.mtd_FILE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_FILE #
class fllibreria_FILE(interna_FILE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration FILE #
class FILE(fllibreria_FILE, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.FILE_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
