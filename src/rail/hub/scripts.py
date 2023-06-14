import sys
import os
import glob
import yaml

from rail.hub.options import GitMode


def render_nb(outdir, clear_output, dry_run, inputs, **kwargs):

    command = "jupyter nbconvert"
    options = "--to html"

    status = {}

    for nb_file in inputs:
        subdir = os.path.dirname(nb_file).split('/')[-1]
        basename = os.path.splitext(os.path.basename(nb_file))[0]
        outfile = os.path.join('..', '..', outdir, f"{subdir}/{basename}.html")
        relpath = os.path.join(outdir, f'{subdir}')

        try:
            print(relpath)
            os.makedirs(relpath)
        except FileExistsError:
            pass

        if clear_output:
            comline = f"{command} --clear-output {nb_file}"
        else:
            comline = f"{command} {options} --output {outfile} --execute {nb_file}"

        if dry_run:
            render = 0
            print(comline)
        else:
            render = os.system(comline)
        status[nb_file] = render

    for key, val in status.items():
        print(f"{key} {val}")


def clone_source(outdir, git_mode, dry_run, package_file):

    with open(package_file) as pfile:
        package_dict = yaml.safe_load(pfile)

    for key, val in package_dict.items():
        if os.path.exists(f"{outdir}/{key}"):
            print(f"Skipping existing {outdir}/{key}")
            continue
            
        if git_mode == GitMode.ssh:
            com_line = f"git clone https://github.com/LSSTDESC/{key}.git {outdir}/{key}"
        elif git_mode == GitMode.https:
            com_line = f"git clone git@github.com:LSSTDESC/{key}.git {outdir}/{key}"
        elif git_mode == GitMode.cli:
            com_line = f"gh repo clone LSSTDESC/{key} {outdir}/{key}"

        if dry_run:
            print(com_line)
        else:
            os.system(com_line)


def install(outdir, from_source, dry_run, package_file):

    with open(package_file) as pfile:
        package_dict = yaml.safe_load(pfile)

    for key, val in package_dict.items():

        if not from_source:
            com_line = f"pip install {val}"
        else:            
            if not os.path.exists(f"{outdir}/{key}"):
                print(f"Skipping missing {outdir}/{key}")
                continue
            com_line = f"pip install -e {outdir}/{key}"
        
        if dry_run:
            print(com_line)
        else:
            os.system(com_line)

