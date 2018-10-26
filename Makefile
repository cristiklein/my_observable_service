help:
	@echo "You probably want to type things in this order:"
	@echo "  make init -> initialize the environment"
	@echo "  make run  -> run the app in development"

init:
	pipenv install

run:
	pipenv run env FLASK_APP=my_observable_service flask run
