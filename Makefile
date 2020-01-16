help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


build: ## build the base dependencies needed for basic operations
	pip3 install -r requirements


invoke:
	sudo source /venv/bin/activate 
	 
interactive:
	/venv/bin/itango3 --profile=ska

test: ## run tests
	py.test
