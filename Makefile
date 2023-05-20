# Init vars
MAKEFILE := $(lastword $(MAKEFILE_LIST))
BASENAME := $(shell basename "$(PWD)")
SHELL := /bin/bash

DOCKER_AUTOMATION_TEST_DIR = tests/docker-automations
PACKER_AUTOMATION_TEST_DIR = tests/packer-automations
DJANGO_AUTOMATION_TEST_DIR = tests/django-automations
ANGULAR_AUTOMATION_TEST_DIR = tests/angular-automations
ANGULAR_UI_TEST_DIR = tests/angular-ui-lib

.PHONY: help
all: help
help: Makefile
	@echo
	@echo " Commands:"
	@echo
	@sed -n 's/^##//p' $< | sed -e 's/^/ /' | sort
	@echo

build:
	echo "Removing Old Files"
	rm -rf build dist ask_jennie.egg-info

	echo "Start Building"
	python -m build
	@echo "OK"

upload:
	echo "Uploading build"
	twine upload dist/*
	@echo "OK"

prepare-docker-test:
	@echo "Preparing Docker Automation Test"
	docker build -f ${DOCKER_AUTOMATION_TEST_DIR}/Dockerfile -t docker-automations .

test-docker:
	@echo "Running Docker Automation Test"
	docker run docker-automations:latest > ${DOCKER_AUTOMATION_TEST_DIR}/jennie.automations.log | sleep 5

prepare-packer-test:
	@echo "Preparing Packer Automation Test"
	docker build -f ${PACKER_AUTOMATION_TEST_DIR}/Dockerfile -t packer-automations .

test-packer:
	@echo "Running Packer Automation Test"
	docker run packer-automations:latest > ${PACKER_AUTOMATION_TEST_DIR}/jennie.automations.log | sleep 5

prepare-angular-test:
	@echo "Preparing Angular Automation Test"
	docker build -f ${ANGULAR_AUTOMATION_TEST_DIR}/Dockerfile -t angular-automations  .

test-angular:
	@echo "Running Angular Automation Test"
	docker run angular-automations:latest > ${ANGULAR_AUTOMATION_TEST_DIR}/jennie.automations.log | sleep 5

prepare-angular-ui-test:
	@echo "Preparing Angular Automation Test"
	docker build -f ${ANGULAR_UI_TEST_DIR}/Dockerfile -t angular-automations  .

test-angular-ui:
	@echo "Running Angular Automation Test"
	docker run angular-automations:latest > ${ANGULAR_UI_TEST_DIR}/jennie.automations.log | sleep 5

prepare-django-test:
	@echo "Preparing Django Automation Test"
	docker build -f ${DJANGO_AUTOMATION_TEST_DIR}/Dockerfile -t django-automations  .

test-django:
	@echo "Running Django Automation Test"
	docker run django-automations:latest > ${DJANGO_AUTOMATION_TEST_DIR}/jennie.automations.log | sleep 5


prepare-for-test:
	@$(MAKE) -f $(MAKEFILE) prepare-docker-test
	@$(MAKE) -f $(MAKEFILE) prepare-packer-test
	@$(MAKE) -f $(MAKEFILE) prepare-angular-test
	@$(MAKE) -f $(MAKEFILE) prepare-angular-ui-test
	@$(MAKE) -f $(MAKEFILE) prepare-django-test
	@echo "Test Prepared"

execute-test:
	@$(MAKE) -f $(MAKEFILE) test-docker
	@$(MAKE) -f $(MAKEFILE) test-packer
	@$(MAKE) -f $(MAKEFILE) test-angular
	@$(MAKE) -f $(MAKEFILE) test-angular-ui
	@$(MAKE) -f $(MAKEFILE) test-django
	@echo "Test Executed"

run-tests:
	@$(MAKE) -f $(MAKEFILE) prepare-for-test
	@$(MAKE) -f $(MAKEFILE) execute-test
	@echo "OK"

clear-test-result:
	@echo "Deleting Old Test Result"
	rm -rf ${DOCKER_AUTOMATION_TEST_DIR}/jennie.automations.log
	rm -rf ${PACKER_AUTOMATION_TEST_DIR}/jennie.automations.log
	rm -rf ${ANGULAR_AUTOMATION_TEST_DIR}/jennie.automations.log
	rm -rf ${DJANGO_AUTOMATION_TEST_DIR}/jennie.automations.log
	rm -rf ${ANGULAR_UI_TEST_DIR}/jennie.automations.log