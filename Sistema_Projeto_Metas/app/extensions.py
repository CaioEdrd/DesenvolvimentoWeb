from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() #inicialização da biblioteca do banco de dados
migrate = Migrate() #migração do banco de dados