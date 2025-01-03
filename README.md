shiv demo
============

A demo to use shiv + PEP 723 Inline script metadata + uv together.

# Get Started

### Build shiv with inline script metadata support

* Checkout code: `git clone -b my-branch https://github.com/clayrosenthal/shiv.git`
* Build: `cd shiv; uv build; cd dist; uv tool install ./shiv-1.1.0-py2.py3-none-any.whl`
* Test: `shiv --help`

### Bundle PEP 723 script

Create a hello.py file:

```python
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///

import requests


def main():
    print(requests.get("https://httpbin.org/ip").text)


if __name__ == "__main__":
    main()
```

Then bundle it with shiv:

```shell
$ shiv --python "/usr/bin/env python3.13" -o hello.pyz --inline-script hello.py
```

**Attention**: Please assign the correct python versio if needed.

### Run the bundled script

Run bundled script with uv:  `uv run hello.pyz`

Why run script with uv? Because uv can detect shebang and run the script with the correct python version.

# References

* shiv: https://shiv.readthedocs.io/
* All your Python project in one file with shiv: https://www.bitecode.dev/p/all-your-python-project-in-one-file
* Support PEP-723 Style in-line metadata annotated scripts: https://github.com/linkedin/shiv/issues/266
* PEP 441 – Improving Python ZIP Application Support: https://peps.python.org/pep-0441/
* PEP 723 – Inline script metadata: https://peps.python.org/pep-0723/