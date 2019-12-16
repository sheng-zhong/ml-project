import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

print('你好')
