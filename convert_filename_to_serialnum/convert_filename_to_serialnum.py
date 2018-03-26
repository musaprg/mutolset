import argparse
import os,sys

def main(filedir):
    if not os.path.isdir(filedir):
        print("Please select directory path.")
        sys.exit(1)
    files = os.listdir(filedir)
    maxdigit = len(str(len(files)))
    for i, path in enumerate(files):
        _, ext = os.path.splitext(path)
        os.rename(
            os.path.join(filedir, path),
            os.path.join(filedir, (("%0"+str(maxdigit)+"d") % i)+ext)
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filedir", help="Path to file directory.")
    args = parser.parse_args()
    main(args.filedir)