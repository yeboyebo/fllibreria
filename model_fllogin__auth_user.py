# @class_declaration interna_auth_user #
import importlib

from YBUTILS.viewREST import helpers

from models.fllogin import models as modelos


class interna_auth_user(modelos.mtd_auth_user, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_auth_user #
class fllibreria_auth_user(interna_auth_user, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration auth_user #
class auth_user(fllibreria_auth_user, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllogin.auth_user_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
