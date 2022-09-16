import sys
import os
import argparse
import shutil

def _main():
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', help='base folder of dataset', required=True)

    args = parser.parse_args()

    # Store arguments
    baseFolder = args.base

    s2l = dict()

    # Get source file locations & vulnerable lines
    for root,dirs,files in os.walk('wildcve_positives'):
        for fn in files:
            path = os.path.join(root,fn)

            with open(path,'r') as fr:
                for e,line in enumerate(fr):
                    if e == 0:
                        continue

                    _,orig_path,linenum,_,_,_,_ = line.split(',')

                    #TODO - debugging/testing
                    if 'jasper-version' not in orig_path:
                        continue

                    orig_path = orig_path.replace('/mnt/sdb/gmacon3/labeled-dataset',baseFolder)
                    orig_path = orig_path.replace('samples-from-wild','wild_compile')
                    orig_path = orig_path.replace('hector_build/../','')

                    if orig_path not in s2l:
                        s2l[orig_path] = set()
                    s2l[orig_path].add(linenum)

    with open('SARD-hole_line_wild.txt','w') as fw_sard:

        # For each source file
        for e,t in enumerate(s2l.items()):
            k,v = t

            print('=================================')
            print(k,v)

            # Find compiled bitcode (will be named .o)
            srcFN = k.split('/')[-1]
            targetFN = srcFN.split('.')[0] + '.o'
            targetFN2 = srcFN + '.o'
            targets = [targetFN,targetFN2]

            folder = '/'.join(k.split('/')[:6])

            found = None
            for root,dirs,files in os.walk(folder):
                for fn in files:
                    qpath = os.path.join(root,fn)
                    for target in targets:
                        if target in qpath:
                            if found is None:
                                found = qpath

            if found is None:
                print('Error, bitcode file not found')
                continue

            # Copy it to where the source file is as a .bc file
            bcFolder = '/'.join(k.split('/')[:-1])
            bcPath = os.path.join(bcFolder,targetFN.replace('.o','.bc'))

            print('Copied {0} -> {1}'.format(found,bcPath))

            shutil.copy2(found,bcPath)

            # Output xml file
            xmlPath = os.path.join(bcFolder,targetFN.replace('.o','.xml'))
            # Output txt file
            txtPath = os.path.join(bcFolder,targetFN.replace('.o','.txt'))

            with open(xmlPath,'w') as fw, open(txtPath,'w') as fw_txt:
                fw.write('<file path="{0}" language="">\n'.format(k))
                fw.write('<testcase id="{0}" ></testcase>\n'.format(e))

                # If there's a vulnerability
                if len(v) > 0:
                    for d in v:
                        fw.write('<flaw line="{0}" name="">\n'.format(d))
                        fw_sard.write('{0} {1}\n'.format(k,d))
                        fw_txt.write('{0} {1}\n'.format(k,d))
                # Else
                else:
                    fw.write('<flaw line="0" name="">\n')
                    fw_sard.write('{0} 0\n'.format(k))
                    fw_txt.write('{0} 0\n'.format(k))

                fw.write('</file>')

            print('Output xml file {0}'.format(xmlPath))

            print('')

if __name__ == '__main__':
    _main()
