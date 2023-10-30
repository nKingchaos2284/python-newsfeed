from app.routes import home
from flask import Flask

def create_app(test_config=None):
  # set up app config
@app.route('/hello')
def hello():
  return 'hello world'

# register routes
app.register_blueprint(home)

return app