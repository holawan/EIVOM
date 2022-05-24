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
			Movie.objects.create(
				# id = row['id'],
				title = row['title'],
				original_title = row['original_title'],
				poster_path = row['poster_path'],
				backdrop_path = row['backdrop_path'],
				overview = row['overview'],
				release_date = row['release_date'],
				vote_count = row['vote_count'],
				vote_average = row['vote_average'],
				popularity = row['popularity'],
				runtime = row['runtime'],
				tagline = row['tagline'],
				actor_id = row['actor_id'],
				actors = row['actors'],
				actors_path = row['actors_path'],
				genres = row['genres'],
				cluster = row['cluster'],
			)

