import pandas as pd
import json
import pathlib

if __name__ == '__main__':
    dir = pathlib.Path(__file__).parent
    assert dir.name == 'data'
    df = pd.read_csv(dir / 'time-series-packages.csv')
    print(df.info())
    result = df.to_json(orient="records")
    parsed = json.loads(result)
    with open('time-series-packages.json', 'w') as f:
        json.dump(parsed, f, indent=4)