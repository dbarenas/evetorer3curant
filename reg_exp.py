import sys
import re

print "format 1"
#format 1
def strip_punctuation(input):
    x = 0
    for word in input:
        input[x] = re.sub(r'[^A-Za-z]', "", input[x])
        x += 1
    return input

a=['\xc3', '\x82', '\xc2','difficult', '9concepts', '.', ':', 'flow\x30', 'business', 'entities', 'basis', 'distribution', 'concepts', 'Major', 'error', 'malpractice', 'issues', 'occur', 'CPA', 'fully', 'understand', 'impact', 'rules', 'course', 'designed', 'focus', 'practical', 'applications', 'rules', 'Corporations', 'Determine', 'calculate', 'basis', 'Worksheets', 'included', 'Recognize', 'AAA', 'applies', 'apply', 'certain', 'corporations', 'Discuss', 'loss', 'limitation', 'rules', 'depth', 'Understand', 'distributions', 'cash', 'property', 'LLCs', 'Partnerships', 'Determine', 'calculate', 'basis', '704', 'risk', '465', 'Learn', 'difference', 'basis', 'risk', 'basis', 'means', 'economic', 'effect', 'equivalence', 'test', 'dumb', 'lucky', 'rule', 'Find', 'hot', 'assets', 'change', 'game', 'distributions', 'Understand', 'affects', 'basis', 'treat', 'distributions', 'Designed', 'CPAs', 'prepare', 'individual', 'flow', 'business', 'entity', 'tax', 'returns', 'need', 'thorough', 'grasp', 'significant', 'issues', 'course', 'must', 'practitioners', 'help', 'reduce', 'avoid', 'exposure', 'malpractice', 'CPE', 'Credits', '8', 'Taxes', 'Prerequisite', 'Experience', 'business', 'taxation', 'Advance', 'Preparation', 'None']

#fcontent = [w for w in content if w.lower() not in rmlist]
print str(strip_punctuation(a)).lower()


print "format 2"
#format 2 
fcontent = [w for w in a if re.sub(r'[^A-Za-z]', "", w)]
print fcontent


b="trololo\xe30"
print re.sub(r'[^A-Za-z]', "", b)