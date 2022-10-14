# @class_declaration interna_DICT #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_DICT(modelos.mtd_DICT, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_DICT #
class fllibreria_DICT(interna_DICT, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration DICT #
class DICT(fllibreria_DICT, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.DICT_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
