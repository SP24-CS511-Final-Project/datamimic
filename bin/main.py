import typer
import yaml

app = typer.Typer()


@app.command()
def generate(config_path: str):
  with open(config_path) as config_file:
    content = config_file.read()
    obj = yaml.load_all(content, Loader=yaml.Loader)
    for doc in obj:
      print(doc)


@app.command()
def version():
  print("0.1.0")


if __name__ == "__main__":
  app()
