TODO: Create VENV
  Venv pip install flask
  Venv pip install flask-login
  Venv pip install flask-sqlalchemy
  
from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
