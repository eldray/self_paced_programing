#!/usr/bin/env bash

whom_variable="World"
#spaces cannot be around the '=' 
#printf is used to safely output the data

printf "Hello, %s\n" "whom_variable"
