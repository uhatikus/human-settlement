#########################
# Aleksandr Ukhatov
# 2019/08/13
#########################

import vk_api
import pymysql
import yaml

def main():
	# get information about user
	user_info = yaml.full_load(open("params.yaml"))

	# connect to mysql database
	connection = pymysql.connect(host=user_info['mysql']['host'],
	                             user=user_info['mysql']['user'],
	                             password=user_info['mysql']['password'],
	                             db=user_info['mysql']['db'],
	                             charset='utf8mb4',
	                             cursorclass=pymysql.cursors.DictCursor)

	# create table 'cities' in given database
	try:

		# UNCOMMENT IF YOU WANT TO REMOVE PREVIUOS TABLE

		# with connection.cursor() as cursor:
		# 	# remove table
		# 	sql = "DROP TABLE IF EXISTS cities;"
		# 	cursor.execute(sql)

		with connection.cursor() as cursor:
			# create table
			sql = "CREATE TABLE IF NOT EXISTS cities ( id INTEGER, title VARCHAR(255), region VARCHAR(255), area VARCHAR(255), country VARCHAR(255), PRIMARY KEY (id) );"
			cursor.execute(sql)
		# connection is not autocommit by default. So you must commit to save
		# your changes.
		connection.commit()
	 
	finally:
		connection.close()

	# connect to vk
	vk_session = vk_api.vk_api.VkApi(str(user_info['vk']['login']), user_info['vk']['password'])
	vk_session.auth()
	vk = vk_session.get_api()

	# init constants
	max_num_of_cities = 1000
	country_ids = user_info['country_ids']
	cities = []

	# get information about all countries with given ids
	countries = vk.database.getCountriesById(country_ids=country_ids)
	# get all human settlements for every country
	for country in countries: 

		print("__________ new coutry ___________")
		print("Country name: " + country['title'])

		# vk API let us get information about 1000 human settlements for one request
		# Therefore, we get the number of cities of given country and 
		# perform requests until we get infromation about all human settlements.  
		response = (vk.database.getCities(country_id=country['id'], need_all=1, count=max_num_of_cities, offset=0))
		first_count = response['count']
		count = first_count - max_num_of_cities
		cities = cities + response['items']
		iteration = 1
		while count > 0:
			print("Done: %.1f" % (100*max_num_of_cities*iteration/first_count) + '%')
			response = (vk.database.getCities(country_id=country['id'], need_all=1, count=max_num_of_cities, offset=iteration*max_num_of_cities))
			cities = cities + response['items']
			count = count - max_num_of_cities
			iteration += 1
		# connect to mysql again
		connection = pymysql.connect(host=user_info['mysql']['host'], user=user_info['mysql']['user'], password=user_info['mysql']['password'], db=user_info['mysql']['db'], charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
		print("Save to mysql table")
		# Save information about human settlements of given country to mysql table  
		try:
			for city in cities:
				with connection.cursor() as cursor:
					# Create a new record
					if ('area' in city) and ('region' in city):
						sql = "INSERT INTO cities (id, title, region, area, country) VALUES (%s, %s, %s, %s, %s)"
						cursor.execute(sql, (city['id'], city['title'], city['region'], city['area'], country['title']))
					elif ('region' in city):
						sql = "INSERT INTO cities (id, title, region, country) VALUES (%s, %s, %s, %s)"
						cursor.execute(sql, (city['id'], city['title'], city['region'], country['title']))
					elif ('area' in city):
						sql = "INSERT INTO cities (id, title, area, country) VALUES (%s, %s, %s, %s)"
						cursor.execute(sql, (city['id'], city['title'], city['are'], country['title']))
					else:
						sql = "INSERT INTO cities (id, title, country) VALUES (%s, %s, %s)"
						cursor.execute(sql, (city['id'], city['title'], country['title']))

			# connection is not autocommit by default. So you must commit to save
			# your changes.
			connection.commit()
		finally:
			connection.close()
		# refresh cities list
		cities = []

	print("Done!")

if __name__ == '__main__':
    main()
