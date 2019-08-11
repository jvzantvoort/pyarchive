
.PHONY: test docs tag rpm changelog

GITHUB_USER ?= jvzantvoort
GITHUB_PROJECT ?= pyarchive
GROUPNAME ?= "homenet"

docs:
	@make -C sphinxdoc html


tag:
	@ version=`grep  '__version__' pyarchive/version.py | grep -o "[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*"`; \
	git tag "$${version}"; \
	git push origin master --tags

rpm:
	python setup.py bdist_rpm

changelog:
	@ docker run -it --rm -v $(PWD):/usr/local/src/your-app \
	ferrarimarco/github-changelog-generator --user $(GITHUB_USER) \
	--project $(GITHUB_PROJECT)
