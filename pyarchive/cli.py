# coding: utf-8
"""Command line handling."""

# from __future__ import unicode_literals
import sys
import os.path
import logging
import click
from pyarchive.exceptions import PyArchiveException, PyArchiveConfigException
from pyarchive.version import __version__

from pyarchive.main import Move

#
# ------------------------------------------------------------------------------
class State(object):
    """Maintain logging level."""

    def __init__(self, log_name='pyarchive', level=logging.INFO):
        self.logger = logging.getLogger(log_name)
        self.logger.propagate = False
        stream = logging.StreamHandler()
        formatter = logging.Formatter("%(levelname)s %(funcName)s:  %(message)s")
        stream.setFormatter(formatter)
        self.logger.addHandler(stream)

        self.logger.setLevel(level)

# pylint: disable=C0103
pass_state = click.make_pass_decorator(State, ensure=True)

def verbose_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.DEBUG)
    return click.option('-v', '--verbose',
                        is_flag=True,
                        expose_value=False,
                        help='enable verbose output',
                        callback=callback)(f)

def quiet_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(State)
        if value:
            state.logger.setLevel(logging.ERROR)
    return click.option('-q', '--quiet',
                        is_flag=True,
                        expose_value=False,
                        help='silence warnings',
                        callback=callback)(f)

def verbosity_options(f):
    f = verbose_option(f)
    f = quiet_option(f)
    return f

DEFAULT_PYARCHIVE_LOCATION = 'default'
# ------------------------------------------------------------------------------
# 
pyarchloc_opt = click.option('--location', '-l', 'pyarchive_location',
                          help="which location should be used" +
                          " (default: %s)" % DEFAULT_PYARCHIVE_LOCATION,
                          metavar="LOCATION",
                          default=DEFAULT_PYARCHIVE_LOCATION)


# base options for all
base_options = [
    pyarchloc_opt,
    click.argument('srcfile', nargs=1, required=True, type=str, metavar='SOURCEFILE')
]

# export specific options
mover_options = base_options + [
    click.option('-b', '--bundles', 'bundles', is_flag=True, default=False, help="export to bundles"),
    click.option('--outputdir', '-o', 'outputdir', help="where the export shut be put")
]

def add_options(options):
    """ Given a list of click options this creates a decorator that
    will return a function used to add the options to a click command.
    :param options: a list of click.options decorator.
    """
    def _add_options(func):
        """ Given a click command and a list of click options this will
        return the click command decorated with all the options in the list.
        :param func: a click command function.
        """
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options

@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '-V', '--version')
def cli():
    """
    GitLab tools
    """
    pass


@cli.command(name="mv")
@add_options(mover_options)
@verbosity_options
def mover(**kwargs):
    """Export the latest version of the projects"""
    try:
        glt_obj = Move(**kwargs)
        glt_obj.main()

    except PyArchiveException as exp:
        raise SystemExit("\n" + str(exp))

