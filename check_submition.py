# Do pip install gitpython
# run with python check_submition.py hw-id.txt
import os
import sys
import subprocess
import re
import git
global commit, id, giturl, grade, total


def main():
    print("1 Test(1)\n")
    total = 1
    grade = 0
    try:
        hw = open(sys.argv[1], 'r+').read().splitlines()
        repo_url = hw[0]
        commit_id = hw[1]
        repo_path = hw[2]
        if(os.path.exists(repo_path)):
            return print("Directory  " + repo_path+" is already exists, so please delete it and run the command again")
        print(repo_path)
        repo = git.Repo.clone_from(repo_url, repo_path, no_checkout=True)
        repo.git.checkout(commit_id)
        # base dirs
        os.mkdir(repo_path+'/inputs')
        os.mkdir(repo_path+'/outputs')
        basedir = os.getcwd().replace("\\", "/")+"/"+repo_path+"/"
    except Exception as e:
        print(e)
    try:
# test 1
        print("\nTest 1")
        f = open(basedir+"text.txt", 'w+')
        f.write("first")
        f.write("\n")
        f.write("tsriF sgniht tsrif si a tnellecxe vt wohs")
        f.write("\n")
        f.write("divaD tnew emoh")
        f.write("\n")
        f.write("learsi tog rezifp eniccav tsrif")
        f.write("\n")
        f.write("tsrif desaeler fo nohtyP saw ta seitenin")
        f.write("\n")
        f.write("i annaw eb eht tsriF ot yas yppah yadhtrib")
        f.close()

        f = open(basedir+"test.py", 'w+')
        f.write("import text as txt")
        f.write("\n")
        f.write("print(txt.countword())")
        f.close()

        command = "cd "+repo_path+" && python " + basedir + \
            "test.py" + " > "+basedir+"/outputs/test1.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test1.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if float(x)==6.0:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)

        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest1:"+passed)
        f.close()
    except Exception as e:
        print(e)


    print("Total Grade", (grade/total)*100, "%")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you need write python check_submition.py hw-id.py while id is your id number")
