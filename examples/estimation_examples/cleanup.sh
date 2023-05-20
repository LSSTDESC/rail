
if [[ -z "${RAILDIR}" ]] then;
   \rm -rf examples/estimation/TEMPZFILE.out
   \rm -rf examples/estimation/output_*.fits
   \rm -rf examples/estimation/demo_FZB_model.pkl
   \rm -rf examples/estimation/demo_knn.pkl   
else
   \rm -rf ${RAILDIR}/examples/estimation/TEMPZFILE.out
   \rm -rf ${RAILDIR}/examples/estimation/output_*.fits
   \rm -rf ${RAILDIR}/examples/estimation/demo_FZB_model.pkl
   \rm -rf ${RAILDIR}/examples/estimation/demo_knn.pkl   
fi

