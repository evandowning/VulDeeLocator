import sys
import json

def _main():
    if len(sys.argv) != 5:
        sys.stderr.write('error. params\n')
        sys.exit(1)

    jsonFN = sys.argv[1]
    xmlFN = sys.argv[2]
    srcFN = sys.argv[3]
    setid = sys.argv[4]

    with open(jsonFN,'r') as fr:
        content = json.load(fr)

    with open(xmlFN,'w') as fw:
        fw.write('<file path="{0}" language="">\n'.format(srcFN))
        fw.write('<testcase id="{0}" ></testcase>\n'.format(setid))

        # If there's a vulnerability
        if len(content) > 0:
            for d in content:
                line = d['line_number']
                fw.write('<flaw line="{0}" name="">\n'.format(line))
        # Else
        else:
            fw.write('<flaw line="0" name="">\n')

        fw.write('</file>')
if __name__ == '__main__':
    _main()
