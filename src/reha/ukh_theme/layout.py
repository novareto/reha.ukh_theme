from reiter.application.browser import TemplateLoader
from reha.ukh_theme.resources import theme


TEMPLATES = TemplateLoader("./templates")
GLOBAL_MACROS = TEMPLATES['macros.pt'].macros


class Layout:

    _template = TEMPLATES["layout.pt"]

    def __init__(self, request, name):
        self.name = name

    def render(self, content, **namespace):
        theme.need()
        return self._template.render(content=content, **namespace)


def sitecap(request, name, view):
    return TEMPLATES["sitecap.pt"].render(request=request)


def globalmenu(request, name, view):
    return TEMPLATES["globalmenu.pt"].render(request=request)


def messages(request, name, view):
    utility = request.utilities.get("flash")
    if utility is not None:
        messages = list(utility)
    else:
        messages = []
    return TEMPLATES["messages.pt"].render(messages=messages)


def footer(request, name, view):
    return TEMPLATES["footer.pt"].render(request=request)
