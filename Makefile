install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

test:
	python -m pytest -vv --cov=main --cov=logic test_*.py

format:
	black *.py

refactor: format lint

deploy:
	#pushes container to ECR (your info will be different!)
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 778411468391.dkr.ecr.us-east-1.amazonaws.com
	docker build -t activity_generator .
	docker tag activity_generator:latest 778411468391.dkr.ecr.us-east-1.amazonaws.com/activity_generator:latest
	docker push 778411468391.dkr.ecr.us-east-1.amazonaws.com/activity_generator:latest

all: install lint test format deploy