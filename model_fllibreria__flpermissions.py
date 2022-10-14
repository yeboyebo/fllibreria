# @class_declaration interna_flpermissions #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_flpermissions(modelos.mtd_flpermissions, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_flpermissions #
class fllibreria_flpermissions(interna_flpermissions, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration flpermissions #
class flpermissions(fllibreria_flpermissions, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.flpermissions_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
