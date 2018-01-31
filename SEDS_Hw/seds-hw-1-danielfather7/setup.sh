#!/bin/bash

echo "making dir"
mkdir HCEPDB

echo "changing dir"
cd HCEPDB

echo "This is the README" > README.txt

echo "downloading file"
curl http://faculty.washington.edu/dacb/HCEPDB_moldata.zip -o HCEPDB_moldata.zip

echo "unzipping file"
unzip HCEPDB_moldata.zip

echo “finish!”
