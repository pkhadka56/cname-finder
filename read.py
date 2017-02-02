#!/usr/bin/env python

from dns.resolver import dns

with open('subdomains.txt') as lines:
	for line in lines:
		line=line.rstrip('\n')
		try:
			answers = dns.resolver.query(line, 'CNAME')
			for rdata in answers:
				print answers.qname, '-->', rdata.target
		except Exception: 
			#print answers.qname, 'no'
			pass