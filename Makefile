help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


build_base: ## build the base dependencies needed for basic operations
	sudo apt-get update && \
	sudo apt-get install python3-pip -y

build_dep: build_base ## build the dependencies needed for testing
	sudo pip3 install -r requirements

test: ## run tests
	py.test
