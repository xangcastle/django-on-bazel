# Django on Bazel

A minimal Django app (one model, two JSON endpoints) built, tested and shipped
as a container image with Bazel and `aspect_rules_py` 2.x. Hands-on material
for a 90-minute BazelCon training.

Requirements: `bazelisk`, `curl`, `git`, and for step 5 a container runtime
(`podman` or `docker`). No system Python, no virtualenv, no pip, no uv:
rules_py provides all of them.

## How to follow along

Start from an empty checkout of `main`. Each step is a pull request with only
the hand-written changes. Where a step begins with commands that generate
files, run them yourself; the reference output is committed on the
`step-N-generated` branch the pull request is based on, so `git diff
step-N-generated` shows how your output differs. `final` is the finished
project.

| Step | You run | Then apply |
|---|---|---|
| 1 | nothing yet | [PR 1](https://github.com/xangcastle/django-on-bazel/pull/1) `step-1-bazel-module` |
| 2 | `bazel run @uv -- init --bare --name notes --python 3.12`<br>`bazel run @uv -- add --no-sync --group runtime "django>=5.2,<6"`<br>`bazel run @uv -- add --no-sync --group dev pytest pytest-django` | [PR 2](https://github.com/xangcastle/django-on-bazel/pull/2) `step-2-dependency-groups` |
| 3 | `bazel run @uv -- lock`<br>`bazel run //:venv_link`<br>`.venv/_main/.venv/bin/django-admin startproject config .`<br>`.venv/_main/.venv/bin/django-admin startapp notes` | [PR 3](https://github.com/xangcastle/django-on-bazel/pull/3) `step-3-django-targets` |
| 4 | `.venv/_main/.venv/bin/python manage.py makemigrations notes` | [PR 4](https://github.com/xangcastle/django-on-bazel/pull/4) `step-4-tests` |
| 5 | nothing | [PR 5](https://github.com/xangcastle/django-on-bazel/pull/5) `step-5-container-image` |

Each pull request says what to check once applied. At the end,
`git diff final` should be empty.

## Cheat sheet

```sh
bazel run @uv -- add --no-sync --group runtime <pkg>   # then: bazel run @uv -- lock
bazel run //:venv_link                                 # .venv for the IDE, django-admin, makemigrations
bazel run //:manage -- <django command>
bazel test //...
bazel run //:image.load
```
