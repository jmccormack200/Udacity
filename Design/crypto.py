# -------------
# User Instructions
#
# Write a function, solve(formula) that solves cryptarithmetic puzzles.
# The input should be a formula like 'ODD + ODD == EVEN', and the 
# output should be a string with the digits filled in, or None if the
# problem is not solvable.
#
# Note that you will not be able to run your code yet since the 
# program is incomplete. Please SUBMIT to see if you are correct.

from __future__ import division
import string, re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
		if valid(f):
			print f
def fill_in(formula):
	letters = ''.join(set(re.findall('[A-Z]', formula)))
	for digits in itertools.permutations('1234567890', len(letters)):
		table = string.maketrans(letters, ''.join(digits))
		yield formula.translate(table)
    
def compile_word(word):
	if word.isupper():
		terms = [('%s*%s' % (10**i, d))
			for (i,d) in enumerate(word[::-1])]
		return '(' + '+'.join(terms)+ ')'
	else:
		return word
    
def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
		
if __name__ == '__main__':
	print solve("ODD + ODD == EVEN")