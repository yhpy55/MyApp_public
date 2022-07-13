#!/bin/bash

cd ../
if [ -d ./MyApp.git ]; then
    rm -rf ./MyApp.git
fi

git clone --bare https://github.com/yhpy55/MyApp.git
cd ./MyApp.git
git push --mirror https://github.com/yhpy55/MyApp_public.git
