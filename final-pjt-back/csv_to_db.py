from ast import literal_eval
import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiserver.settings")
django.setup() 
from movies.models import Movie
csv_path = 'C:/Users/SAMSUNG/Desktop/final-pjt/final-pjt-back/clustering/cluster_output.csv'

with open(csv_path, newline='',encoding='utf-8') as f_csv:
		row_dics = csv.DictReader(f_csv)
		for row in row_dics: 
			print(row)
			movie = Movie.objects.get(pk=row['\ufeffid'])
			movie.cluster = row['cluster']
			movie.save()
				
