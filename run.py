from project import create_app, db
from project.models import User, Exercise

# Production
app = create_app("ProductionConfig")
# Development
# app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Exercise": Exercise}
