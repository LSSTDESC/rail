
if [[ -z "${RAILDIR}" ]] then;
   \rm -rf output_*.pq
   \rm -rf output_*.fits
   \rm -rf output_*.hdf5
   \rm -rf *.pkl
   \rm -rf *.out
else
   \rm -rf ${RAILDIR}/output_*.pq
   \rm -rf ${RAILDIR}/output_*.fits
   \rm -rf ${RAILDIR}/output_*.hdf5
   \rm -rf ${RAILDIR}/*.pkl
   \rm -rf ${RAILDIR}/*.out
fi

