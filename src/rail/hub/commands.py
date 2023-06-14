import sys
from typing import Any, Tuple

import click

from rail.hub import options, scripts


@click.group()
@click.version_option(package_name="rail")
def cli() -> None:
    """RAIL utility scripts"""


@cli.command()
@options.outdir(default='docs')
@options.clear_output()
@options.dry_run()
@options.inputs()
def render_nb(outdir, clear_output, dry_run, inputs, **kwargs):
    """Render jupyter notebooks"""
    scripts.render_nb(outdir, clear_output, dry_run, inputs)


@cli.command()
@options.outdir(default='..')
@options.git_mode()
@options.dry_run()
@options.package_file()
def clone_source(outdir, git_mode, dry_run, package_file, **kwargs):
    """Install packages from source"""
    scripts.clone_source(outdir, git_mode, dry_run, package_file)


@cli.command()
@options.outdir(default='..')
@options.dry_run()
@options.from_source()
@options.package_file()
def install(outdir, dry_run, from_source, package_file, **kwargs):
    """Install packages from source"""
    scripts.install(outdir, from_source, dry_run, package_file)
