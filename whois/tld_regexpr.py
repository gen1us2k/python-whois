com = {
    'extend': None,

    'domain_name': r'Domain Name:\s?(.+)',
    'registrar': r'Registrar:\s?(.+)',
    'registrant': r'Registrant:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Name(?:[^:]{0,}):\s?(.+)',
    'registrant_cc': r'Registrant:?\s{0,}(?:[^\n][\n]?){0,}?\s{0,}Country(?:[^:]{0,}):\s?(.+)',

    'creation_date': r'Creation Date:\s?(.+)',
    'expiration_date': r'Expiration Date:\s?(.+)',
    'updated_date': r'Updated Date:\s?(.+)',

    'name_servers': r'Name Server:\s*(.+)\s*',
    'status': r'Status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

net = {
    'extend': 'com',
}

org = {
    'extend': 'com',

    'creation_date': r'\nCreated On:\s?(.+)',
    'updated_date': r'\nLast Updated On:\s?(.+)',

    'name_servers': r'Name Server:\s?(.+)\s*',
}

uk = {
    'extend': 'com',

    'registrant': r'Registrant:\n\s*(.+)',
    'registrant_cc': r'Registrant\'s address:\s+(?:[^\n][\n]?)+\n(.+)\n\n',

    'creation_date': r'Registered on:\s*(?:before )(.+)',
    'expiration_date': r'Renewal date:\s*(.+)',
    'updated_date': r'Last updated:\s*(.+)',

    'name_servers': r'Name Servers:\s*(.+)\s*',
    'status': r'Registration status:\n\s*(.+)',
}

pl = {
    'extend': 'uk',

    'registrant_cc' : r'location:\s?(.+)',
    'creation_date': r'\ncreated:\s*(.+)\n',
    'updated_date': r'\nlast modified:\s*(.+)\n',

    'name_servers': r'\nnameservers:\s*(.+)\n\s*(.+)\n',
    'status': r'\nStatus:\n\s*(.+)',
}

ru = {
    'extend': 'com',

    'domain_name': r'\ndomain:\s*(.+)',

    'creation_date': r'\ncreated:\s*(.+)',
    'expiration_date': r'\npaid-till:\s*(.+)',

    'name_servers': r'\nnserver:\s*(.+)',
    'status': r'\nstate:\s*(.+)',
}

su = {
    'extend': 'ru',
}

lv = {
    'extend': 'ru',

    'creation_date': r'Registered:\s*(.+)\n',
    'updated_date': r'Changed:\s*(.+)\n',

    'status': r'Status:\s?(.+)',
}

jp = {
    'domain_name': r'\[Domain Name\]\s?(.+)',
    'registrar': None,
    'registrant': r'\[Registrant\]\s?(.+)',
    'registrant_cc' : None,

    'creation_date': r'\[Created on\]\s?(.+)',
    'expiration_date': r'\[Expires on\]\s?(.+)',
    'updated_date': r'\[Last Updated\]\s?(.+)',

    'name_servers': r'\[Name Server\]\s*(.+)',
    'status': r'\[Status\]\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

co_jp = {
    'extend': 'jp',

    'creation_date': r'\[Registered Date\]\s?(.+)',
    'expiration_date': r'\[State\].+\((.+)\)',
    'updated_date': r'\[Last Update\]\s?(.+)',
}

de = {
    'extend': 'com',
    'domain_name': r'\ndomain:\s*(.+)',
    'updated_date': r'\nChanged:\s?(.+)',
    'name_servers': r'Nserver:\s*(.+)',
}

at = {
    'extend': 'com',
    'domain_name': r'domain:\s?(.+)',
    'updated_date': r'changed:\s?(.+)',
    'name_servers': r'nserver:\s*(.+)',
}

eu = {
    'extend': 'com',

    'domain_name': r'\ndomain:\s*(.+)',
    'registrar': r'Name:\s?(.+)',
}

cc = {
    'extend': 'com',

    'registrar': r'(?:Sponsoring\s)?Registrar:\s?(.+)',
    'registrant_cc': None,
    'expiration_date': r'Registry Expiry Date:\s?(.+)',
}

biz = {
    'extend': 'com',

    'registrar': r'Sponsoring Registrar:\s?(.+)',
    'registrant': r'Registrant Organization:\s?(.+)',

    'creation_date': r'Domain Registration Date:\s?(.+)',
    'expiration_date': r'Domain Expiration Date:\s?(.+)',
    'updated_date': r'Domain Last Updated Date:\s?(.+)',

    'status': None,
}

info = {
    'extend': 'biz',

    'creation_date': r'Creat(?:ed On|ion Date):\s?(.+)',
    'expiration_date': r'(?:Registry\s)?Expir(?:y|ation) Date:\s?(.+)',
    'updated_date': r'(?:Last\s)?Updated (?:On|Date):\s?(.+)',

    'status': r'Status:\s?(.+)',
}

name = {
    'extend': 'com',

    'status': r'Domain Status:\s?(.+)',
}

us = {
    'extend': 'name',
}

co = {
    'extend': 'biz',

    'status': r'Status:\s?(.+)',
}

me = {
    'extend': 'biz',

    'creation_date': r'Domain Create Date:\s?(.+)',
    'expiration_date': r'Domain Expiration Date:\s?(.+)',
    'updated_date': r'Domain Last Updated Date:\s?(.+)',

    'name_servers': r'Nameservers:\s?(.+)',
    'status': r'Domain Status:\s?(.+)',
}

be = {
    'extend': 'pl',

    'domain_name': r'\nDomain:\s*(.+)',
    'registrar': r'(?:Company\s)?Name:\n?(.+)',

    'creation_date': r'Registered:\s*(.+)\n',

    'status': r'Status:\s?(.+)',
}

nz = {
    'extend': None,

    'domain_name': r'domain_name:\s?(.+)',
    'registrar': r'registrar_name:\s?(.+)',
    'registrant': r'registrant_contact_name:\s?(.+)',
    'registrant_cc': r'registrant_contact_country:\s?([^\(]+).+',

    'creation_date': r'domain_dateregistered:\s?(.+)',
    'expiration_date': r'domain_datebilleduntil:\s?(.+)',
    'updated_date': r'domain_datelastmodified:\s?(.+)',

    'name_servers': r'ns_name_[0-9]{2}:\s?(.+)',
    'status': r'query_status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

cz = {
    'extend': 'com',

    'domain_name': r'Domain:\s?(.+)',
    'registrar': r'registrar:\s?(.+)',
    'registrant': r'registrant:\s?(.+)',

    'creation_date': r'registered:\s?(.+)',
    'expiration_date': r'expire:\s?(.+)',
    'updated_date': r'changed:\s?(.+)',

    'name_servers': r'nserver:\s*(.+) ',
}

it = {
    'extend': 'com',

    'domain_name': r'Domain:\s?(.+)',
    'registrar': r'Registrar:\s*Organization:\s*(.+)',
    'registrant': r'Registrant:\s?Name:\s?(.+)',

    'creation_date': r'Created:\s?(.+)',
    'expiration_date': r'Expire Date:\s?(.+)',
    'updated_date': r'Last Update:\s?(.+)',

    'name_servers': r'Nameservers:\s?(.+)\s?(.+)\s?(.+)\s?(.+)',
    'status': r'Status:\s?(.+)',
}

fr = {
    'extend': 'com',

    'domain_name': r'domain:\s?(.+)',
    'registrar': r'registrar:\s*(.+)',
    'registrant': r'contact:\s?(.+)',

    'creation_date': r'created:\s?(.+)',
    'expiration_date': None,
    'updated_date': r'last-update:\s?(.+)',

    'name_servers': r'nserver:\s*(.+)',
    'status': r'status:\s?(.+)',
}

kg = {
    'extend': 'com',

    'domain_name': r'Domain \s?(.+)',
    'creation_date': r'Record created:\s?(.+)',
    'expiration_date': r'Record expires on \s?(.+)',
}

vc = {
    'extend': 'com',
}

fm = {
    'extend': 'com',

    'domain_name': r'Query: \s?(.+)',
    'creation_date': r'Created: \s?(.+)',
    'expiration_date': r'Expires: \s?(.+)'
}

tv = {
    'extend': 'com',
    'domain_name': r'Domain Name: \s?(.+)',

    'creation_date': r'Creation Date: \s?(.+)',
    'expiration_date': r'Registry Expiry Date: \s?(.+)'
}

edu = {
    'extend': 'com',
    'domain_name': r'Domain Name: \s?(.+)',

    'creation_date': r'Domain record activated: \s?(.+)',
    'expiration_date': r'Domain expires: \s?(.+)',
    'updated_date': r'Domain record last updated: \s?(.+)',
}

ca = {
    'extend': 'com',

    'domain_name': r'Domain name: \s?(.+)',
    'creation_date': r'Creation date: \s?(.+)',
    'expiration_date': r'Expiry date: \s?(.+)',
    'updated_date': r'Updated date: \s?(.+)',
}

cn = {
    'extend': 'com',

    'registrant': r'Registrant:\s?(.+)',
    'registrant_cc': None,

    'creation_date': r'Registration Date:\s?(.+)',
    'updated_date': None,

    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

hk = {
    'extend': None,

    'domain_name': r'Domain Name:\s?(.+)',
    'registrar': r'Registrar Name:\s?(.+)',
    'registrant': r'Company English Name\(?.+\)?:\s?(.+)',
    'registrant_cc': r'Country:\s?(.+)',

    'creation_date': r'Domain Name Commencement Date:\s?(.+)',
    'expiration_date': r'Expiry Date:\s?(.+)',
    'updated_date': None,

    'name_servers': r'Name Servers Information:\s*(.+)\s*',
    'status': r'Domain Status:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

kr = {
    'extend': None,

    'domain_name': r'Domain Name\s+:\s?(.+)',
    'registrar': None,
    'registrant': r'Registrant\s+:\s?(.+)',
    'registrant_cc': None,

    'creation_date': r'Registered Date\s+:\s?(.+)',
    'expiration_date': r'Expiration Date\s+:\s?(.+)',
    'updated_date': r'Last Updated Date\s+:\s?(.+)',

    'name_servers': r'Host Name\s+:\s?(.+)',
    'emails': r'[\w.-]+@[\w.-]+\.[\w]{2,4}',
}

