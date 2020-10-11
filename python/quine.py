def as_data(code):
	s="'"
	l=code[0]
	if ord(l)==9:l='\\n'
	elif ord(l)==10:l='\\t'
	elif l=="'":l="\\'"
	elif l=='"':l='\\"'
	elif l=="\\":l='\\\\'
	s=s+l
	for l in code[1:]:
		if ord(l)==0x0a:l='\\n'
		elif ord(l)==10:l='\\t'
		elif l=="'":l="\\'"
		elif l=='"':l='\\"'
		elif l=="\\":l='\\\\'
		s=s+l
	return s + "'"
def as_code(data):
	s=""
	for l in data:
		if l=="\\":l='\\\\'
		s=s+l
	return s
p = 'def as_data(code):\n	s=\"\'\"\n	l=code[0]\n	if ord(l)==9:l=\'\\n\'\n	elif ord(l)==10:l=\'\\t\'\n	elif l==\"\'\":l=\"\\\'\"\n	elif l==\'\"\':l=\'\\\"\'\n	elif l==\"\\\":l=\'\\\\\'\n	s=s+l\n	for l in code[1:]:\n		if ord(l)==0x0a:l=\'\\n\'\n		elif ord(l)==10:l=\'\\t\'\n		elif l==\"\'\":l=\"\\\'\"\n		elif l==\'\"\':l=\'\\\"\'\n		elif l==\"\\\":l=\'\\\\\'\n		s=s+l\n	return s + \"\'\"\ndef as_code(data):\n	s=\"\"\n	for l in data:\n		if l==\"\\\":l=\'\\\\\'\n		s=s+l\n	return s\np = \nprint(as_code(p[:388]),end=\"\")\nprint(as_data(p),end=\"\")\nprint(as_code(p[388:]),end=\"\")'
print(as_code(p[:388]),end="")
print(as_data(p),end="")
print(as_code(p[388:]),end="")