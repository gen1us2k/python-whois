#!/bin/bash
FILE=whois.conf
curl https://gist.githubusercontent.com/thde/3890aa48e03a2b551374/raw/138589bfcae4d24b31ddd61ac7886ab568a8fc28/whois.conf > $FILE
[[ -f $FILE ]] || { printf "$FILE doesn't exist!\n" && exit 1; }

# Strip characters to get TLD name only e.g. com
TLDs=$(cut -d " " -f1 whois.conf | sed -e 's/\\//' -e 's/\.//' -e 's/\$//' | egrep -v '^$|^#')

# Skip existing supported TLDs
SKIP=$(grep = ./whois/tld_regexpr.py | cut -d " " -f1)

config(){
tld="$1"

cat <<EOF
$tld = {
  'extend': 'com',
}
EOF
}

for tld in $TLDs; do
    [[ $SKIP =~ .*$tld.* ]] && continue
    config $tld
done
