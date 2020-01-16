help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


build: ## build the base dependencies needed for basic operations
	pip3 install -r requirements


invoke:
	source /venv/bin/activate 
	 

test: ## run tests
	py.test
