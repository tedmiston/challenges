#!/bin/bash

python3 solution.py < in.txt > solution_out.txt && diff solution_out.txt out.txt && rm solution_out.txt
