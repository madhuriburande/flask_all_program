from first_flask.product import launch_app
app=launch_app()
if __name__=='__main__':
    app.run(debug=True)