import cherrypy


class Root:
    @cherrypy.expose
    def text(self):
        return "Hello, world!"


app = cherrypy.tree.mount(Root())
cherrypy.log.screen = False
