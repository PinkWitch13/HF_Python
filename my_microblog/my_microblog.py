from app import app, db
from app.models import User, Posts

@app.shell_context_processior
def make_shell_context():
    return {'db':db, 'User':User, 'Posts':Posts}
