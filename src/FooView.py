from flask.views import MethodView

class FooView(MethodView):

    def getdata(self, name):
        return f"Hello {name}", 200