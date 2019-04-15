import os
import glob

from doit.tools import create_folder
from doit.action import CmdAction


DOIT_CONFIG = {'default_tasks': ['build', "unit_test", "clang_tidy"]}

BUILD_DIR="build_"

def task_cmake():
    """Generate Makefiles using cmake"""

    return {
        'targets' : [BUILD_DIR],
        'actions': [
            (create_folder, [BUILD_DIR]),
            CmdAction('cmake ..', cwd=BUILD_DIR)
        ],
        'clean': ['rm -r build_']
    }


def task_build():
    """Compile project"""

    return {
        'task_dep': ['cmake'],
        'actions': [CmdAction('make -j', cwd=BUILD_DIR)],
    }


def post_build_task(action):
    """Helper function to generate tasks that depend on 'build"""
    return {
        'task_dep' : ['build'],
        'actions' : [CmdAction(action, cwd=BUILD_DIR)],
    }


def task_unit_test():
    """Run unit tests"""
    return post_build_task("test/unittest")


def task_clang_tidy():
    """Run clang tidy"""
    return post_build_task('run-clang-tidy.py -quiet -j 8')
