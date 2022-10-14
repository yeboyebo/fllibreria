# @class_declaration interna_auth_group #
import importlib

from YBUTILS.viewREST import helpers

from models.fllogin import models as modelos


class interna_auth_group(modelos.mtd_auth_group, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_auth_group #
class fllibreria_auth_group(interna_auth_group, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration auth_group #
class auth_group(fllibreria_auth_group, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllogin.auth_group_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
