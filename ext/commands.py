from ext.database import db

def init_app(app):
    
    @app.cli.command()
    def create_database():
        db.create_all()
