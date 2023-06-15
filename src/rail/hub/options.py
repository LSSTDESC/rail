import enum
from functools import partial, wraps
from typing import Any, Callable, Type, TypeVar, cast

import click

__all__ = [
    "clear_output",
    "dry_run",
    "outdir",
    "from_source",
    "git_mode",
    "print_all",
    "print_packages",
    "print_namespaces",
    "print_modules",
    "print_tree",
    "print_stages",
    "package_file",
    "inputs",
]


class GitMode(enum.Enum):
    """Choose git clone mode"""
    ssh = 0
    https = 1
    cli = 2


EnumType_co = TypeVar("EnumType_co", bound=Type[enum.Enum], covariant=True)


class EnumChoice(click.Choice):
    """A version of click.Choice specialized for enum types"""

    def __init__(self, enum: EnumType_co, case_sensitive: bool = True) -> None:
        self._enum = enum
        super().__init__(list(enum.__members__.keys()), case_sensitive=case_sensitive)

    def convert(self, value: Any, param, ctx) -> EnumType_co:
        converted_str = super().convert(value, param, ctx)
        return self._enum.__members__[converted_str]


class PartialOption:
    """Wraps click.option with partial arguments for convenient reuse"""

    def __init__(self, *param_decls: Any, **kwargs: Any) -> None:
        self._partial = partial(click.option, *param_decls, cls=partial(click.Option), **kwargs)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._partial(*args, **kwargs)

    
class PartialArgument:
    """Wraps click.argument with partial arguments for convenient reuse"""

    def __init__(self, *param_decls: Any, **kwargs: Any) -> None:
        self._partial = partial(click.argument, *param_decls, cls=partial(click.Argument), **kwargs)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._partial(*args, **kwargs)


clear_output = PartialOption(
    "--clear-output",
    help="Clear Notebook output",
    is_flag=True,
)

dry_run = PartialOption(
    "--dry-run",
    help="Dry run only",
    is_flag=True,
)

from_source = PartialOption(
    "--from-source",
    help="Install from source",
    is_flag=True,
)

outdir = PartialOption(
    "--outdir",
    type=click.Path(),
    default=None,
    help="Output directory.",
)

git_mode = PartialOption(
    "--git-mode",
    type=EnumChoice(GitMode),
    default='ssh',
    help="Git Clone mode",
)

print_all = PartialOption(
    "--print-all",
    help="Print all RAIL information",
    is_flag=True,
)

print_packages = PartialOption(
    "--print-packages",
    help="Print RAIL packages",
    is_flag=True,
)

print_namespaces = PartialOption(
    "--print-namespaces",
    help="Print RAIL namespaces",
    is_flag=True,
)

print_modules = PartialOption(
    "--print-modules",
    help="Print RAIL modules",
    is_flag=True,
)

print_tree = PartialOption(
    "--print-tree",
    help="Print RAIL namespace tree",
    is_flag=True,
)

print_stages = PartialOption(
    "--print-stages",
    help="Print RAIL stages",
    is_flag=True,
)





package_file = PartialOption(
    "--package-file",
    type=click.Path(),
    default=None,
    help="File with package",
)

inputs = PartialArgument(
    "inputs",
    nargs=-1
)

