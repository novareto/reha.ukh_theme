from typing import Optional, Type
from horseman.meta import Overhead
from reiter.application.browser import registries
from reha.ukh_theme import layout


UI = None


def get_theme(
        ui: Optional[registries.UIRegistry] = None,
        request_type: Type[Overhead] = Overhead):

    if ui is None:
        ui = registries.UIRegistry(macros=layout.GLOBAL_MACROS)

    # Registering main layout
    ui.register_layout(request_type)(layout.Layout)

    # Registering slots
    ui.register_slot(
        request=request_type, name="sitecap"
    )(layout.sitecap)

    ui.register_slot(
        request=request_type, name="globalmenu"
    )(layout.globalmenu)

    ui.register_slot(
        request=request_type, name="site-messages"
    )(layout.messages)

    ui.register_slot(
        request=request_type, name="footer"
    )(layout.footer)

    return ui


def install_theme(
        app,
        request_type: Type[Overhead] = Overhead,
        override: bool = False):

    if override:
        app.ui = get_theme(None, request_type=request_type)
    else:
        app.ui = get_theme(app.ui, request_type=request_type)
    return app
