# -*- coding:utf-8 -*-
from optparse import OptionParser
import os
import re


def reorder(targetPath, fileName, flag, labelFile):
    if not os.path.exists(targetPath):
        return

    global_linenum = list()
    with open(labelFile,'r') as fr:
        for line in fr:
            line = line.strip('\n')
            _,l = line.split(' ')
            global_linenum.append(int(l))

    flawLineDict = {} #key:xxx_new.ll value:linenum of vulline
    focusLineDict = {} #key:xxx_new.ll value:linenum of focus
    dirList = os.listdir(targetPath) 
    flagZero = 0
    linenum = 0
    for targetfile in dirList:  
        flagZero = 0
        #NOTE: this doesn't apply to our wild dataset
       #if not targetfile.endswith('].ll') or targetfile.endswith('[9999].ll'):
       #    continue
        if targetfile.endswith('_[0].ll'):
            flagZero = 1
        elif targetfile.endswith('.ll'):
            flagZero = 2
        else:
            continue
        if flagZero == 0:
            targetflag = re.findall('_\[(\d+)_(\d+)\].ll', targetfile) 
            sliceName = re.sub('_\[\d+_\d+\].ll', '.new.ll', targetfile) #change [xxx_yy].ll to new.ll
            linenum = re.findall('_(\d+):',targetfile)[0];
        elif flagZero == 1:
            sliceName = targetfile[:-7] + '.new.ll' #change [0].ll to new.ll
            linenum = re.findall('_(\d+):',targetfile)[0];
        #NOTE - need a new.ll file for Juliet dataset
        elif flagZero == 2:
            sliceName = targetfile[:-3] + '.new.ll' #change [0].ll to new.ll
            # Flaw lines are in the file
            linenum = list()
            with open(labelFile,'r') as fr:
                for line in fr:
                    line = line.strip('\n')
                    _,l = line.split(' ')
                    linenum.append(int(l))
#       print(sliceName)
        focusLineDict[sliceName] = linenum
        os.system('cp -f \"' + os.path.join(targetPath, targetfile) + '\" \"' + os.path.join(targetPath, sliceName)+ '\"') 
        if flagZero == 0 and sliceName in flawLineDict:
            for i in range(int(targetflag[0][1])): 
                flawLineDict[sliceName].append(int(targetflag[0][0]) + i)
        elif flagZero == 0:
            flawLineDict[sliceName] = []
            for i in range(int(targetflag[0][1])):
                flawLineDict[sliceName].append(int(targetflag[0][0]) + i)
        elif sliceName in flawLineDict:
            flawLineDict[sliceName].append(0)
        # NOTE: needed for Juliet dataset
        elif flagZero == 2:
            if sliceName not in flawLineDict.keys():
                flawLineDict[sliceName] = list()
            for l in linenum:
                flawLineDict[sliceName].append(l)
        else:
            flawLineDict[sliceName] = [0]

    for slicefile in flawLineDict.keys():
        lineCounter = 0
        sliceStr = ''
        sourcelinedbg = []
        lines = focusLineDict[slicefile]

#       print(flawLineDict[slicefile])

        # For each vulnerable line
        for linenum in lines:
#           print(linenum)

            with open(os.path.join(targetPath,slicefile),'r') as f:
                for line in f:
                    if(line.startswith('!')):
                        pattern = '(.*) = !DILocation\(line: '+str(linenum)
                        dbg = re.findall(pattern,line)
                        if(len(dbg)):
                            sourcelinedbg.append(dbg[0])

#           print(sourcelinedbg)

            with open(os.path.join(targetPath,slicefile),'r') as f:
                for line in f:
                    lineCounter += 1
                    noteFlag = re.findall('\A +; x',line)
                    if noteFlag: 
                        continue
                    for dbgline in sourcelinedbg:
                       if line.endswith(dbgline+'\n'):
                           line = line.replace('\n','')
                           line += ' #_%$$FOCUS_TAG$$%_#\n' 
                    if lineCounter in flawLineDict[slicefile]:
                        line = line.replace('\n','')
                        line += ' #_%$$FLAW_TAG$$%_#\n'
                    sliceStr += line

#       if 'FOCUS_TAG' in sliceStr:
#           print('YAY focus')
#       if 'FLAW_TAG' in sliceStr:
#           print('YAY flaw')

        if(len(slicefile[:-7] + '.flawtag.ll') > 250): 
            return
        with open(os.path.join(targetPath,slicefile[:-7] + '.flawtag.ll'),'w') as f: 
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

        #TODO - only focus on positive lines
        found = False
        for l in global_linenum:
            if '{0}:'.format(l) in targetfile:
                found = True
                break
        if found is False:
            continue
        print(fileName,targetPath,targetfile,global_linenum)

        # Is this a line we're interested in?

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
        #NOTE: need to specify to output dot file locally
        cmd = 'opt -dot-callgraph "' + filePath + '"'
        os.system(cmd)
        #print(cmd)
        cmd = 'cp {0}.callgraph.dot callgraph.dot'.format(filePath)
        os.system(cmd)
        #print(cmd)
        if os.path.isfile(os.path.join(curpath, fileName[:-3] + '.c')):
            flag = 0
        else:
            flag = 1
        reorder(os.path.join(curpath, 'api'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'arr'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'point'), fileName[:-3], flag, labelFile);
        reorder(os.path.join(curpath, 'bds'), fileName[:-3], flag, labelFile);
        #cmd = 'mv callgraph.dot '+curpath+'/'+fileName[:-3]+'_callgraph.dot'
        cmd = 'rm callgraph.dot'
        os.system(cmd)
        #print(cmd)


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
