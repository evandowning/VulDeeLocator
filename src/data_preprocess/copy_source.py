import sys
import os
import shutil

def _main():
    if len(sys.argv) != 3:
        sys.stderr.write('error. wrong params\n')
        sys.exit(1)

    srcFolder = sys.argv[1]
    dstFolder = sys.argv[2]

    for root,dirs,files in os.walk(srcFolder):
        for d in dirs:
            path = os.path.join(root,d)

            folders = path.replace(srcFolder,'')
            dstPath = os.path.join(dstFolder,folders)

            # NOTE: Skip libtiff for now
            if 'libtiff' in path:
                continue

            ext='_dir'
            if ext == path[-len(ext):]:
                shutil.copytree(path, dstPath)

if __name__ == '__main__':
    _main()
