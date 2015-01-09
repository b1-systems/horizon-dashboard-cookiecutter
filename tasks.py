#!/usr/bin/env python
import os
import shutil

from invoke import task, run

@task
def build():
    run("cookiecutter %s --no-input" % os.path.abspath(os.path.dirname(__file__)))

@task
def clean():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "mydashboard")
    if os.path.exists(path):
        shutil.rmtree(path)
        print("Removed %s" % path)

@task(pre=[clean, build])
def test():
    run("flake8 %s" % os.path.join(os.path.abspath(os.path.dirname(__file__)), "mydashboard"))
