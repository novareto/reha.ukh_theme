from reiter.application.browser import TemplateLoader
from uvcreha.request import Request
from uvcreha.browser import ui
from reha.ukh_theme.resources import theme


TEMPLATES = TemplateLoader("./templates")
layout_template = TEMPLATES["layout.pt"]


@ui.register_layout(Request)
class Layout:

    __slots__ = ("_template", "name")

    def __init__(self, request, name):
        self.name = name
        self._template = layout_template

    @property
    def macros(self):
        return self._template.macros

    def render(self, content, **namespace):
        theme.need()
        return self._template.render(content=content, **namespace)


@ui.register_slot(request=Request, name="sitecap")
def sitecap(request, name, view):
    return TEMPLATES["sitecap.pt"].render(request=request)


@ui.register_slot(request=Request, name="globalmenu")
def globalmenu(request, name, view):
    return TEMPLATES["globalmenu.pt"].render(request=request)


@ui.register_slot(request=Request, name="site-messages")
def messages(request, name, view):
    utility = request.utilities.get("flash")
    if utility is not None:
        messages = list(utility)
    else:
        messages = []
    return TEMPLATES["messages.pt"].render(messages=messages)


@ui.register_slot(request=Request, name="footer")
def footer(request, name, view):
    return TEMPLATES["footer.pt"].render(request=request)
