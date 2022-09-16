# -*- coding:utf-8 -*-
from optparse import OptionParser
import os
import re


def reorder(targetPath, fileName, flag, labelFile):
    if not os.path.exists(targetPath):
        return

    # Get lines we're interested in (vulnerabilities)
    linenum = list()
    with open(labelFile,'r') as fr:
        for line in fr:
            line = line.strip('\n')
            _,l = line.split(' ')
            linenum.append(int(l))

    flawLineDict = {}
    focusLineDict = {}

    targetfile = targetPath.split('/')[-2]
    targetfile = targetfile.split('.')[0]
    targetfile += '.ll'
    targetFN = os.path.join(targetPath,targetfile)

    sliceName = targetfile[:-3] + '.new.ll' # change to new.ll
    sliceFN = os.path.join(targetPath,sliceName)

    # If '.new.ll' already exists, we've already parsed this folder
    if os.path.exists(sliceFN):
        return

    focusLineDict[sliceName] = linenum
    if len(linenum) == 0:
        flawLineDict[sliceName] = [0]
    else:
        flawLineDict[sliceName] = linenum
    os.system('cp -f \"' + targetFN + '\" \"' + sliceFN + '\"') 

    lineCounter = 0
    sliceStr = ''
    sourcelinedbg = []

    # For each vulnerable line
    for number in linenum:
        with open(sliceFN,'r') as f:
            for line in f:
                if(line.startswith('!')):
                    pattern = '(.*) = !DILocation\(line: '+str(number)
                    dbg = re.findall(pattern,line)
                    if(len(dbg)):
                        sourcelinedbg.append(dbg[0])

        with open(sliceFN,'r') as f:
            for line in f:
                lineCounter += 1
                noteFlag = re.findall('\A +; x',line)
                if noteFlag:
                    continue
                for dbgline in sourcelinedbg:
                   if line.endswith(dbgline+'\n'):
                       line = line.replace('\n','')
#                      line += ' #_%$$FOCUS_TAG$$%_#\n'
                       line += ' #_%$$FOCUS_TAG$$%_# #_%$$FLAW_TAG$$%_#\n'
#               if lineCounter in flawLineDict[sliceName]:
#                   line = line.replace('\n','')
#                   line += ' #_%$$FLAW_TAG$$%_#\n'
                sliceStr += line

#   if 'FOCUS_TAG' in sliceStr:
#       print('YAY focus')
#   if 'FLAW_TAG' in sliceStr:
#       print('YAY flaw')

    flawFN = os.path.join(targetPath,targetfile[:-3] + '.flawtag.ll')
    with open(flawFN,'w') as f:
        f.write(sliceStr)

    dirList = os.listdir(targetPath)
    for targetfile in dirList:
        if fileName == 'multiFinal':
            flagMulti = 0
        elif targetfile.find(fileName) == -1: 
            flagMulti = 1
        else:
            flagMulti = 0

        if not targetfile.endswith('.flawtag.ll') or flagMulti == 1:
            continue

#       # Note if we've found the lines with the flaws on them
#       found = False
#       for l in linenum:
#           if '{0}:'.format(l) in targetfile:
#               found = True
#               break
#       # If no flaw was found
#       if found is False:
#           print('No Flaw: ',fileName,targetPath,targetfile)
#       # If flaw was found
#       else:
#           print('Flaw: ',fileName,targetPath,targetfile,linenum)

        # Create '.final.ll' file
        # Reorder slices for .c or .cpp file
        if flag == 0:
            cmd = 'python2 reorderSlice.py ' + fileName + '.c "' + os.path.join(targetPath, targetfile) + '"'
            os.system(cmd)
        else:
            cmd = 'python2 reorderSlice.py ' + fileName + '.cpp "' + os.path.join(targetPath, targetfile) + '"'
            os.system(cmd)

        # If *.final.ll has nothing in it (e.g., if there is no calling function), just copy over contents
        finalName = targetfile.replace('.flawtag.','.final.')
        finalFN = os.path.join(targetPath,finalName)
        targetFN = os.path.join(targetPath,targetfile)
        if (os.path.exists(finalFN)) and (os.path.getsize(finalFN) == 0):
            cmd = 'cp {0} {1}'.format(targetFN,finalFN)
            os.system(cmd)


def codeCompile(curpath, fileName, labelFile):
    filePath = os.path.join(curpath, fileName)
    if filePath.find('/testcases/shared/') != -1:
        return
    flag = 0
    if filePath.find('/api/') == -1 and filePath.find('/arr/') == -1 and filePath.find(
            '/point/') == -1 and filePath.find('/bds/') == -1:
        flag = 1 
    if filePath.endswith('.bc') and fileName != 'multiFinal.bc' and flag == 1:
        cmd = 'opt -dot-callgraph "' + filePath + '" -o /dev/null'
        os.system(cmd)
        cmd = 'cp {0}.callgraph.dot callgraph.dot'.format(filePath)
        os.system(cmd)
        if os.path.isfile(os.path.join(curpath, fileName[:-3] + '.c')):
            flag = 0
        else:
            flag = 1
        reorder(os.path.join(curpath, 'api'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'arr'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'point'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'bds'), fileName[:-3], flag, labelFile);
        cmd = 'rm callgraph.dot'
        os.system(cmd)


def autoDetectorCodeFile(curPath,labelFile):
    if not os.path.isdir(curPath):
        print curPath
        return
    dirList = os.listdir(curPath)
    for selectedDir in dirList:
        if os.path.isdir(os.path.join(curPath, selectedDir)):
            if os.path.exists(os.path.join(os.path.join(curPath, selectedDir),'multiFinal.bc')):
                codeCompile(os.path.join(curPath, selectedDir),'multiFinal.bc',labelFile)
            else:
                autoDetectorCodeFile(os.path.join(curPath, selectedDir), labelFile)
        else:
            codeCompile(curPath, selectedDir, labelFile)


if __name__ == '__main__':
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args) > 2:
        print 'Usage error, you need to declare original path.'
    elif len(args) == 2:
        rawPath = args[0] 
        autoDetectorCodeFile(rawPath,args[1])
