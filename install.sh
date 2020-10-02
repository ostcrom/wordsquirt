#!/usr/bin/env bash

python3 -m venv setup_env
source ./setup_env/bin/activate

python -m pip install -r requirements.txt
python setup.py py2app
if [ $? -ne 0 ]; then
  echo "**********************************************"
  echo "Build failed, please review output for error!"
  echo "**********************************************"
fi;

mv dist/wordsquirt.app /Applications/wordsquirt.app
if [ $? -eq 0 ]; then
      echo "**********************************************"
      echo "Install successful, deleting set up files."
      echo "**********************************************"
      rm -rf ./build/ ./dist/ ./setup_env/
else
  echo "**********************************************"
  echo "Install failed, please review output for error!"
  echo "**********************************************"
fi
