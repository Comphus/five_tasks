#!/bin/bash
file="gender_submission.csv"
f1=$1
f2=$2
script="import pandas as pd
f = pd.read_csv('$file', header=None)
f.to_csv('$f1', header=False, index=False)
f.T.to_csv('$f2', header=False, index=False)
"
python -c "$script"