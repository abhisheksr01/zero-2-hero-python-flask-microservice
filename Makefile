#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
    %Targets; \
    while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
    print "\n${WHITE}usage:\n"; \
	print "  ${YELLOW}make <target>                  ${GREEN} Replace the <target> with one of below operations.\n\n"; \
    for (sort keys %help) { \
    print "${WHITE}$$_:${RESET}\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (32 - length $$_->[0]); \
    print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
    }; \
    print "\n"; }

help: ##@target Show target help options.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

activate: FORCE ##@target Activates the poetry environment.
	poetry shell

install: FORCE ##@target Installs dependency specified in pyproject.toml.
	poetry install

format-lint: FORCE ##@target Format and lint check python code.
	poetry run task format-lint

unit-test: FORCE ##@target Executes unit testing
	poetry run pytest --cov=greetings tests/ -vvv -s --html=unit-test-report.html --self-contained-html

bdd-test: FORCE ##@target Executes BDD behave tests
	poetry run behave -f html -o bdd-test-report.html

sast: FORCE ##@target Performs SAST using bandit package
	poetry run bandit -r ./greetings

dependency-vulnerability-scan: FORCE ##@target Performs dependency vulnerability scan defined in pyproject.toml using safety package
	poetry run safety check --full-report

start: FORCE ##starts the flask application
	python3 run.py
	
run-all: FORCE ##@target Performs formatting,linting and runs Unit & BDD tests
	poetry run task runall

clear: FORCE ##@target Clears the "__pycache__" & ".pytest_cache". Will be required to run twice.
	@find . -name "__pycache__" -exec rm -rf {} \;
	@find . -name ".pytest_cache" -exec rm -rf {} \;

FORCE: 
