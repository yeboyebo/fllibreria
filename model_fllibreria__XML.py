# @class_declaration interna_XML #
import importlib

from YBUTILS.viewREST import helpers

from models.fllibreria import models as modelos


class interna_XML(modelos.mtd_XML, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration fllibreria_XML #
class fllibreria_XML(interna_XML, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True


# @class_declaration XML #
class XML(fllibreria_XML, helpers.MixinConAcciones):
    pass

    class Meta:
        proxy = True

    def getIface(self=None):
        return form.iface


definitions = importlib.import_module("models.fllibreria.XML_def")
form = definitions.FormInternalObj()
form._class_init()
form.iface.ctx = form.iface
form.iface.iface = form.iface
