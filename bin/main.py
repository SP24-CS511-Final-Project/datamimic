import typer
import yaml
import pandas as pd
import numpy as np
from scipy.stats import zipf, norm, beta

from _version import __version__

app = typer.Typer()


@app.command()
def generate(config_path: str):
  with open(config_path) as config_file:
    content = config_file.read()
    obj = yaml.load_all(content, Loader=yaml.Loader)
    for doc in obj:
      print(doc)
      data = {}
      for column in doc['columns']:
          if column['type'] == 'int':
              if column['distribution'][0]['type'] == 'zipfian':
                  data[column['name']] = np.random.zipf(column['distribution'][0]['alpha'], doc['rows'])
              # Add more distributions here if needed
          elif column['type'] == 'string':
              data[column['name']] = np.random.choice(['a', 'b', 'c', 'd', 'e'], doc['rows'])

      df = pd.DataFrame(data)
      df.to_parquet(doc['outputFile'] + '.' + doc['outputFormat'])
      # Parquet file viewer: https://github.com/mukunku/ParquetViewer/releases


@app.command()
def version():
  print(__version__)


if __name__ == "__main__":
  app()
