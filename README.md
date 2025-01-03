shiv demo
============


# Build shiv with inline script metadata support

* checkout code: `git clone -b my-branch https://github.com/clayrosenthal/shiv.git`
* build: `cd shiv; uv build; cd dist; uv tool install ./shiv-1.1.0-py2.py3-none-any.whl`
* test: `shiv --help`

# References

* shiv: https://shiv.readthedocs.io/
* All your Python project in one file with shiv: https://www.bitecode.dev/p/all-your-python-project-in-one-file
* Support PEP-723 Style in-line metadata annotated scripts: https://github.com/linkedin/shiv/issues/266
* PEP 441 – Improving Python ZIP Application Support: https://peps.python.org/pep-0441/
* PEP 723 – Inline script metadata: https://peps.python.org/pep-0723/