build:
	docker-compose -f ./docker/docker-compose.yml build 
up:
	docker-compose -f ./docker/docker-compose.yml up 
migrate:
	docker-compose -f ./docker/docker-compose.yml exec --rm talataa python ./src/manage.py migrate 
migrations:
	docker-compose -f ./docker/docker-compose.yml exec talataa python ./src/manage.py makemigrations
test:
	# FUNCTION="unit/apps/test_product.py"
	# PARAMS="-rm"
	docker-compose -f ./docker/docker-compose.yml run --rm talataa pytest ./src/tests/${FUNCTION} ${PARAMS}