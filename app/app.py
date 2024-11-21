import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("api.yml")
app.run(port=5000)