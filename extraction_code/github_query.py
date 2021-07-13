import logging
import pathlib

import requests
import json
import click

from extraction_code.data_preparation import prepare_dataframe


@click.command()
@click.option('--token', required=True, type=str)
def main(token):
    """
    :param token: a Github API token
    """

    extracted_data_directory = pathlib.Path(__file__).parent.parent / 'data/extracted'

    # search topics
    with open('search_topics.json', 'r') as f:
        topics = json.load(f)['topics']

    headers = {'Content-Type': 'application/json', 'Authorization': f'token {token}'}

    nb_requests = 0

    for topic in topics:
        url_query = f'https://api.github.com/search/repositories?q=topic:"{topic}"+language:"python"+stars:">=100"+pushed:>2020-07-01'
        logging.info(f'requesting topic {topic}, querying {url_query}')

        response = requests.get(url_query, headers=headers)
        nb_requests += 1
        if response.status_code == 200:
            content = json.loads(response.content.decode('utf-8'))
            items = content['items']

            while response.links.get('next'):
                next_url = response.links['next']['url']
                response = requests.get(next_url, headers=headers)
                nb_requests += 1
                content = json.loads(response.content.decode('utf-8'))
                items.extend(content['items'])

            logging.info(f'number of requests so far: {nb_requests}')
            logging.info(f'found {len(items)} items for topic {topic}\n{url_query}')
            logging.info(f'saving to github_results_query_{topic}.csv')

            df = prepare_dataframe(items)
            df.to_csv(extracted_data_directory / f'github_results_query_{topic}.csv')
        else:
            logging.error(f'{topic} {response.status_code}')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
