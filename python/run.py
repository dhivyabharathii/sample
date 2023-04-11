

from flaskblog import app,db
if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(host='0.0.0.0',port=5005,debug=True)