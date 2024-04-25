@echo off
cd /d %~dp0

echo Running first Python script...
start cmd /k python "E:\shared folder\manage_VM.py"

echo Running second Python script in another Command Prompt window...
start cmd /k python "E:\shared folder\chrome\chrome.py"

echo Both Python scripts started.
