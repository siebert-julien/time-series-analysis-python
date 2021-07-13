import logging
import pathlib
import time

import click
import requests
import json
import pandas as pd

from extraction_code.data_preparation import prepare_dataframe


@click.command()
@click.option('--token', required=True, type=str)
def main(token):
    """
    :param token: a Github API token
    """

    extracted_data_directory = pathlib.Path(__file__).parent.parent / 'data/extracted'

    # search topics
    with open('manual_addition.json', 'r') as f:
        urls = json.load(f)['topics']

    headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}

    items = []

    for url in urls:
        response = requests.get(url, headers=headers)
        logging.info(f'querying {url}')
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            items.append(content)
        else:
            logging.error(f'{response.status_code}: url')

    logging.info(f'saving to manually_added.csv')
    df = prepare_dataframe(items)
    df.to_csv(extracted_data_directory / 'manually_added.csv')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
