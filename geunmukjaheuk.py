# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
input = sys.stdin.readline
from math import ceil

def main():
		N, K = map(int, input().strip().split())
		input()
		print(ceil((N-1)/(K-1)))
main()
