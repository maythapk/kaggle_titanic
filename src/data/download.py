# -*- coding: utf-8 -*-
import requests
import os
import click

url_train_data = 'https://www.kaggle.com/c/titanic/download/train.csv'
url_test_data = 'https://www.kaggle.com/c/titanic/download/test.csv'

raw_train = os.path.join(os.getcwd(), 'data', 'raw', 'train.csv')
raw_test = os.path.join(os.getcwd(), 'data', 'raw', 'test.csv')

@click.command()
@click.argument('url')
@click.argument('filename', type=click.Path())
def download_file(url, filename):
	print('downloading from {} to {}'.format(url, filename))
	response = requests.get(url)
	with open(filename, 'wb') as out:
		out.write(response.content)

if __name__ == '__main__':
    download_file()


