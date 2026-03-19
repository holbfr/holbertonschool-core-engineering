#!/usr/bin/env python3

common_elements = __import__('common_elements').common_elements

set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
print(sorted(list(common_elements(set_1, set_2))))
