# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

def main():
		T = int(input())
		testcase = [list(map(int, input().split())) for i in range(T)]
		for i in range(T):
				print(min(testcase[i][0] // 5, (testcase[i][0] + testcase[i][1]) // 12))
				
main()