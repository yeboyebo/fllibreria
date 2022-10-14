# @class_declaration interna_SQL #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_SQL(modelos.mtd_SQL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_SQL #
class fllibreria_SQL(interna_SQL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration SQL #
class SQL(fllibreria_SQL, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.SQL_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
