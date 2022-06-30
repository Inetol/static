#!/bin/bash

# EXEC EVERY 10 MIN
# SETUP
mkdir "/srv/dns/"
cd "/srv/dns/" || exit
cp raw-records .output

# EXCLUDE
sed -i "/aarif.coi5sbo7qhrd6j96gk4c9ub6y0.php/d" .output

# CONVERT UNBOUND & RELOAD
cat .output | grep '^0\.0\.0\.0' | awk '{printf "local-data: \"%s A 0.0.0.0\"\n", $2}' > "/srv/dns/records.conf"
unbound-control -c "/etc/unbound/unbound.conf" reload
