.PHONY: package test-package test-docker test-docker-dry-run

package:
	python setup.py sdist bdist_wheel upload

package-register:
	python setup.py register

test-docker:
	docker-volume add
	docker-volume mount
	docker-volume unmount
	docker-volume remove

test-docker-dry-run:
	docker-volume add --dry-run
	docker-volume mount --dry-run
	docker-volume unmount --dry-run
	docker-volume remove --dry-run

test-package:
	python setup.py register -r "https://testpypi.python.org/pypi"
	python setup.py sdist bdist_wheel upload -r "https://testpypi.python.org/pypi"
