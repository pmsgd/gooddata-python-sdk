# (C) 2021 GoodData Corporation
# list all full paths to files and directories in CWD containing "gooddata", filter out ones ending by "client"
NO_CLIENT_GD_PROJECTS_ABS = $(filter-out %client, $(wildcard $(CURDIR)/*gooddata*))
# for each path, take only the base name of the path
NO_CLIENT_GD_PROJECTS_DIRS = $(foreach dir, $(NO_CLIENT_GD_PROJECTS_ABS), $(notdir $(dir)))
# TODO: replace API_VERSION in the future by call to API
API_VERSION="v1"
URL="http://localhost:3000/api/${API_VERSION}/schemas"

include ci_tests.mk

all:
	echo "Nothing here yet."

.PHONY: dev
dev:
	python3.11 -m venv .venv --upgrade-deps
	.venv/bin/pip3 install -r dev-requirements.txt
	.venv/bin/pre-commit install

.PHONY: lint
lint:
	.venv/bin/ruff .

.PHONY: format
format:
	.venv/bin/black --check .
	.venv/bin/isort --check .

.PHONY: format-diff
format-diff:
	.venv/bin/black --diff .
	.venv/bin/isort --diff .

.PHONY: format-fix
format-fix:
	.venv/bin/black .
	.venv/bin/isort .


define download_client
    curl "${URL}/$(1)" | jq --sort-keys > schemas/gooddata-$(1)-client.json
endef

define generate_client
	./scripts/generate_client.sh gooddata-$(1)-client -f "/local/schemas/gooddata-$(1)-client.json"
endef



.PHONY: api-client
api-client: download
	rm -f schemas/gooddata-api-client.json+
	cat schemas/gooddata-*.json | jq -S -s 'reduce .[] as $$item ({}; . * $$item) + { tags : ( reduce .[].tags as $$item (null; . + $$item) | unique_by(.name) ) }' > "schemas/gooddata-api-client.json"
	$(call generate_client,api)

.PHONY: download
download:
	$(call download_client,afm)
	$(call download_client,metadata)
	$(call download_client,scan)
	$(call download_client,"export")

.PHONY: mypy
mypy:
	RESULT=0; \
	for project in $(NO_CLIENT_GD_PROJECTS_DIRS); do $(MAKE) -C $${project} $@ || RESULT=$$?; done; \
	exit $$RESULT

.PHONY: test
test:
	RESULT=0; \
	for project in $(NO_CLIENT_GD_PROJECTS_DIRS); do $(MAKE) -C $${project} test || RESULT=$$?; done; \
	exit $$RESULT

.PHONY: release
release:
	if [ -z "$(VERSION)" ]; then echo "Usage: 'make release VERSION=X.Y.Z'"; false; else \
	tbump $(VERSION) --no-tag --no-push ; fi

.PHONY: check-copyright
check-copyright:
	./scripts/check_copyright.py FOLDER

.PHONY: docs
docs:
	RESULT=0; \
	for project in gooddata-fdw gooddata-pandas; do $(MAKE) -C $${project} $@ || RESULT=$$?; done; \
	exit $$RESULT

.PHONY: remove-cassettes
remove-cassettes:
	RESULT=0; \
	for project in $(NO_CLIENT_GD_PROJECTS_DIRS); do $(MAKE) -C $${project} $@ || RESULT=$$?; done; \
	exit $$RESULT

.PHONY: new-docs
new-docs:
	git submodule update --init --recursive --depth 1; \
	cd docs; \
	npm install; \
	hugo server
