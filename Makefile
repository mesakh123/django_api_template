PACKAGE := web-server
MODULE := $(PACKAGE)
GIT_COMMIT = $(shell git rev-parse --short HEAD)
GIT_COMMIT_TIME = $(shell git log -n 1 --pretty=format:"%ad" --date=iso)
VERSION = $(shell cat VERSION)
ARCH = $(shell if [[ $(shell uname -m) == 'arm64' ]]; then echo "-arm64" ; fi)
TARGET := $(realpath ..)

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: build-service
build-service: ## Build container (production)
	@DOCKER_BUILDKIT=1 docker build -f ./dockerfiles/Dockerfile \
		-t ${MODULE} \
		-t ${MODULE}:${VERSION} \
		--build-arg GIT_COMMIT=$(GIT_COMMIT) \
		--build-arg GIT_COMMIT_TIME="$(GIT_COMMIT_TIME)" \
		--build-arg VERSION=$(VERSION) \
		.

.PHONY: build-service-local
build-service-local:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build


.PHONY: run-local
run-local:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 ARCH=$(ARCH) docker-compose up -d --build


.PHONY: stop
stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 ARCH=$(ARCH) docker-compose down


.PHONY: test
test:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 ARCH=$(ARCH) docker-compose run visionai-app pytest --cov


.PHONY: show-module
show-module: ## Show module name
	echo -n "${MODULE}\n"

.PHONY: run
run : ##run Django server
	$(PYTHON) $(APP_DIR)/manage.py runserver
