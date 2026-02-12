
if [[ -z "${RAILDIR}" ]] then;
   \rm -rf examples/creation/output_*.pq
   \rm -rf examples/creation/output_*.fits
else
   \rm -rf $RAILDIR/examples/creation/output_*.pq
   \rm -rf $RAILDIR/examples/creation/output_*.fits 
fi
