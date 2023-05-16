
if [[ -z "${RAILDIR}" ]] then;
   \rm -rf examples/evaluation/output_*.hdf5
else
   \rm -rf ${RAILDIR}/examples/evaluation/output_*.hdf5
fi

