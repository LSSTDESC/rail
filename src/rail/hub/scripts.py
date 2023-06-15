import sys
import os
import glob
import yaml

import rail.stages
from rail.core import RailEnv
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

    ret_val = 0
    for key, val in status.items():
        print(f"{key} {val}")
        if val != 0:
            ret_val = val

    return ret_val
        

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


def info(**kwargs):
    
    rail.stages.import_and_attach_all()

    print_all = kwargs.get('print_all', False)
    if kwargs.get('print_packages') or print_all:
        print("======= Printing RAIL packages ==============")
        RailEnv.print_rail_packages()
        print("\n\n")
    if kwargs.get('print_namespaces') or print_all:
        print("======= Printing RAIL namespaces ==============")
        RailEnv.print_rail_namespaces()
        print("\n\n")
    if kwargs.get('print_modules') or print_all:
        print("======= Printing RAIL modules ==============")
        RailEnv.print_rail_modules()
        print("\n\n")
    if kwargs.get('print_tree') or print_all:
        print("======= Printing RAIL source tree ==============")
        RailEnv.print_rail_namespace_tree()
        print("\n\n")
    if kwargs.get('print_stages') or print_all:
        print("======= Printing RAIL stages ==============")
        RailEnv.print_rail_stage_dict()
        print("\n\n")
    


    
