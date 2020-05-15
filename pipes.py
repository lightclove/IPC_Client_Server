# -*- coding: utf-8 -*-
# /usr/bin/python2
#! https://docs.python.org/2/library/pipes.html

import pipes
t = pipes.Template()
t.append('tr a-z A-Z', '--')
f = t.open('pipefile', 'w')
f.write('hello world')
f.close()
open('pipefile').read()