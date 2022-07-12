@echo off
setlocal

cd C:\Users\0502_Python\Downloads\GitHub
git clone --bare https://github.com/yhpy55/MyApp.git
cd MyApp.git
git push --mirror https://github.com/yhpy55/MyApp_public.git
