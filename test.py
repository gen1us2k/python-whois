#!/usr/bin/env python
# -*- coding: utf-8 -*-

import whois

domains = '''
google.com
www.fsdfsdfsdfsd.google.com
google.org
google.net
google.pl
google.co
google.co.uk
google.jp
google.co.jp
google.de
google.cc
google.ru
google.us
google.eu,whois.markmonitor.com
google.me
google.be
google.biz
google.info
google.it
google.cz
google.fr
google.lv
e2e4.online,whois.nic.ru
napaster.name,whois.nic.ru
XN--C1AAY4A.XN--P1AI
гугл.рф
nic.pw
nic.bid,whois.nic.bid
nic.host,whois.nic.host
nic.party,whois.nic.party
nic.pro,whois.nic.pro
nic.review,whois.nic.review
nic.site,whois.nic.site
nic.space,whois.nic.space
nic.top,whois.nic.top
nic.website,whois.nic.website
nic.win,whois.nic.win
nic.man,whois.nic.man
nic.men,whois.nic.men
'''

def parse(data):
    if "," in data:
        data = data.split(',')

        if len(data) == 1:
            query(data[0])

        elif len(data) == 2:
            query(data[0], data[1])
    else:
        query(data)

def query(domain, host=None):
    print('-' * 80)
    print("Domain: {0}, host: {1}".format(domain, host))
    w = whois.query(domain, host, ignore_returncode=1)
    if w:
        wd = w.__dict__
        for k, v in wd.items():
            print('%20s\t"%s"' % (k, v))

def main():
    for data in domains.split('\n'):
        if data: parse(data)

if __name__ == "__main__":
  main()
