import connexion
from connexion.resolver import MethodViewResolver

app = connexion.FlaskApp(__name__, specification_dir='openapi', resolver=MethodViewResolver('src'))
app.add_api('api.yaml')
app.run(port=8080)


