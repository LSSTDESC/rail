
import sys
import os
import glob
import argparse



def main(args):

    nb_files = glob.glob('examples/*_examples/*.ipynb')

    command = "jupyter nbconvert"
    options = "--to html"
    
    status = {}
    
    for nb_file in nb_files:        
        subdir = os.path.dirname(nb_file).split('/')[-1]
        basename = os.path.splitext(os.path.basename(nb_file))[0]
        outfile = os.path.join('..', '..', args.outdir, f'{subdir}/{basename}.html')
        relpath = os.path.join(args.outdir, f'{subdir}')

        try:
            print(relpath)
            os.makedirs(relpath)
        except FileExistsError:
            pass
    
        if args.clear:
            comline = f"{command} --clear-output {nb_file}"
        else:
            comline = f"{command} {options} --output {outfile} --execute {nb_file}"

        print(comline)

        if args.dry_run:
            render = 0
        else:
            render = os.system(comline)
        status[nb_file] = render

    for key, val in status.items():
        print(f"{key} {val}")
            


if __name__ == '__main__':
        
    parser = argparse.ArgumentParser(description=f"Render all the jupyter notebooks in this package")

    parser.add_argument("--dry_run", action="store_true", help="Dry run only")
    parser.add_argument("--outdir", action="store", help="Output directory", default="docs")
    parser.add_argument("--clear", action="store_true", help="Clear NB outputs")
    
    ret_args = parser.parse_args()
    main(ret_args)
