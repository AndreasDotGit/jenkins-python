from os import listdir
from os.path import isdir
import argparse

parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-a", "--AppName", help = "Name of the application")
parser.add_argument("-g", "--GroupId", help = "Group Id of the application")
args = parser.parse_args()
if args._get_args:
        print("Displaying Output as: % s" % args.AppName)
        if args.AppName:
            print('APPNAME: ' + args.AppName)
        else:
            raise Exception("arg AppName must me defined")
        if args.GroupId:
            print('GROUPID: ' + args.AppName)
        else:
            raise Exception("arg GroupId must me defined")
        
muleGroupId = {"key": "{GROUPID}", "value": args.GroupId}
muleAppName = {"key": "{APP_NAME}", "value": args.AppName}

def search_and_replace(file_path):
   with open(file_path, 'r') as file:
      file_contents = file.read()
      if not file_contents.find(muleAppName.get('key')) == -1 or not file_contents.find(muleGroupId.get('key')) == -1:
        updated_contents = file_contents.replace(muleAppName.get('key'), muleAppName.get('value'))
        updated_contents = updated_contents.replace(muleGroupId.get('key'), muleGroupId.get('value'))
        with open(file_path, 'w') as file:
            file.write(updated_contents)


def checkFile(path):
    #print(path)
    files = listdir(path)
    #print(files)
    for file in files:
        print(file)
        if (not file.startswith('.')) and file != 'hello.py':
            if isdir(path + file):
                #print(path + file + ' is a dir')
                checkFile(path= path + file +'/')
            else:
                search_and_replace(path + file)

checkFile('./')    

