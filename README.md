# Advent of Code 2020

Advent of Code 2020 with tests and utils etc

## Todo

- Complete all puzzles (Doh)

## Cookiecutter

To create a new day with the CookieCutter version run the command from the
`advent2020` directory.

```shell script
cookiecutter template -f
```

Answer the questions:
* `advendofcode2020` : Accept default answer. This installs the result in the currect directory
* `day` : Answer with day you're working on, with leading zero. Eg: 07, 10, 31.
* `directory_name`, `file_name`, `class_name` : Accept default answer

This will create the correct files in the `src` and `tests` directories.
The `-f` option is required to make the files in the current subdirectory.
When the project supports modules this is probably no longer needed.

The new solution still have to be added to the `main.py` file.

### Cookiecutter Todo

* Nothing at the moment

## Install

Install the application with:

```
pip3 install -e .
```

### Run

Use `tox` to run the tests, run `adventofcode` to run the main application.

## Pre-commit

This project uses [pre-commit]. Pre-commit runs all the required tools before committing.
This useful tool will be installed with:

```shell
pip install pre-commit
```

After installation run:

```shell
pre-commit install
```

Now every time before running `git commit` the hooks defined in the
`.pre-commit-config.yaml` file will be run before actually committing.
To run this manually, run:

```shell
pre-commit run --all-files
```

#### Update pre-commit

Update the `.pre-commit-config.yaml` with the command:

```shell
pre-commit autoupdate
```

This command will go online and find the latest versions.

[pre-commit]: https://pre-commit.com/

## Useful Repo's

### 2020

- <https://github.com/SebastiaanZ/aoc-2020>
- <https://github.com/joelgrus/advent2020>
- <https://github.com/EdwardChamberlain/Advent-of-Code>
- <https://github.com/Den4200/advent-of-code-2020>
- <https://github.com/GraceC23245/aoc_2020>
- <https://github.com/raeq/adventofcode>
- <https://github.com/svanjole/AoC2020/tree/master/solutions>
- <https://github.com/AltNyx/adventofcode2020/>

### 2019

- <https://github.com/SebastiaanZ/aoc-2019>
- <https://github.com/joelgrus/advent2019>
