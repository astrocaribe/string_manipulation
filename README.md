# string_manipulation  ![Travis CI](https://travis-ci.org/astrocaribe/string_manipulation.svg)

This is a repo for two string manipulation tasks, a phrase reverser
`reverse_phrase.py` and a simple pig latin translator `pig_latin_translator.py`.
Both of the scripts also include a sample test suite, that can be used to
verify intended functionality.

# Install

The string manipulation tools can be installed simply by downloading this repo
locally. Everything necessary to run the scripts is contained in the `scripts`
folder, so grabbing this single folder should be enough.

# Execution

Executing the scripts should be a straightforward affair. Begin by accessing the
`scripts` folder:

```
$> cd scripts/
```

Then run the script of interest:

`reverse_phrase.py`:
```
$> python reverse_phrase.py
```

`pig_latin_translator`:
```
$> python pig_latin_translator.py
```

Follow the prompts for both scripts, and you're good to go!

# Notebooks

The notebook contained in this repo are the proof-of-concept scripts developed
for this exercise. The [Jupyter](jupyter.org) Notebook file (formally iPython
Notebook) can be rendered directly in GitHub; just select the file and it should
be rendered for your perusal.


# Dependencies
### Required dependencies:

* [Python](python.org) >= 2.6
* [requirements.txt](requirements.txt)

If you want to use the same requirements used in this repo, install them with
the following, preferably in a virtualenv (so as not to mess with your current
 system's global dependencies):

```
$> pip install -r requirements.txt
```

### Testing dependencies:
* [pytest](pytest.org) (for test suite, see below)

# Tests
The sample test suite is written using [pytest](pytest.org); execute the suite
with:

```
$> py.test
```

If you want a more verbose output:
```
$> py.test --verbose
```

# Future:
Planned updates include the following:

* Expand test coverage to include the main() functions of the scripts.
Currently, only the functions are covered in the tests.
* Package Python scripts for simple install with `pip` or `easy_install`
* Include Travis automated test coverage transperency for the GitHub repo
* Javascript modules for use with a simple front end or webapp
* Test coverage using [`mocha`](https://mochajs.org/) for Javascript
