from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")

default_task = "publish"

@init
def set_properties(project):
    project.set_property("coverage_threshold_warn", 80)
    project.set_property("coverage_break_build", False)
    project.set_property("coverage_reset_modules", True)
    project.set_property('coverage_break_build', False)
    project.set_property("coverage_exceptions", ["__init__"])