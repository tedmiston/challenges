# Challenges

[![Code Health](https://landscape.io/github/tedmiston/challenges/master/landscape.svg?style=flat)](https://landscape.io/github/tedmiston/challenges/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f97d41838ac14875b60c7529ed68e630)](https://www.codacy.com/app/tedmiston/challenges?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tedmiston/challenges&amp;utm_campaign=Badge_Grade)

My solutions to programming puzzles & challenges.

Each top-level directory corresponds to one site that has challenge problems, and each directory under that is my solution to a particular problem.

<small>_**Disclaimer**: These solutions were developed by me individually unless otherwise stated and are shared for education and curiosity.  Please do not use them as your own.  If you're working on the same problem, please do not view my answer until you've solved it on your own.  If you're working on a related problem, it's generally okay to cite a solution to another problem as a reference._</small>

## Setup

```bash
mkvirtualenv --python=python3 challenges
pip install -r requirements_pinned.txt
```

## Quickstart

Just browse for a problem of interest.  Most can be run from the problem's directory with:

```bash
python solution.py
```

Newer ones are written in Python 3 while a few older ones are in Python 2 and will be converted at some point.

## Testing

Similary to run tests for a particular problem, `cd` into its directory, then run:

```bash
nose2
```

Many problems have tests included, but some older ones don't yet.
