from fanstatic import Library, Resource, Group
import uvcreha.browser.resources


library = Library("reha.ukh_theme", "static")

CSS = Group([
    Resource(library, "css/bootstrap-4.3.1.min.css"),
    Resource(library, "css/fontawesome-5.11.2.min.css"),
    Resource(library, "css/default.css")
])

JS = Group([
    Resource(library, "js/jquery-3.3.1.min.js", bottom=True),
    Resource(library, "js/popper-1.14.3.min.js", bottom=True),
    Resource(library, "js/bootstrap-4.3.1.min.js", bottom=True),
    Resource(library, "js/fontawesome-5.11.2.min.js", bottom=True)
])


theme = Group([
    uvcreha.browser.resources.application_webpush,
    uvcreha.browser.resources.f_input_group,
    CSS,
    JS,
])
