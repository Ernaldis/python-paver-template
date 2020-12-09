#!/usr/bin/python

from paver.easy import *
import os
import glob
import shutil


@task
def setup():
	sh('python3 setup.py -q install')
	pass


@task
def test():
	sh('nosetests test')
	pass


@task
def clean():
	for pycfile in glob.glob("*/*/*.pyc"):
		os.remove(pycfile)
	for pycache in glob.glob("*/__pycache__"):
		os.removedirs(pycache)
	for pycache in glob.glob("./__pycache__"):
		shutil.rmtree(pycache)
	try:
		shutil.rmtree(os.getcwd() + "/cover")
	except:
		pass
	pass

@task
def afterMath():
        sh('rm -r assign1.egg-info/ build/ dist/')

@task
def output():
	sh('python3 src/hello.py')
	pass


@task
@needs(['setup', 'clean', 'test', 'output', 'afterMath'])
def default():
	pass
