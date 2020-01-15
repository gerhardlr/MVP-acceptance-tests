help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


build: ## build the base dependencies needed for basic operations
	sudo apt-get update && \
	sudo apt-get install pipenv -y && \
	cd /app && \
	pipenv update && \
	cd /home/MVP-acceptance-tests && \
	sudo chown $USER -R .

invoke:
	pipenv shell && \
	cd /home/MVP-acceptance-tests 

	

test: ## run tests
	py.test
