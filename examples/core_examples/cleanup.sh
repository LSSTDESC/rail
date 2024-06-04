#!/bin/bash

if [[ -z "${RAILDIR}" ]]; then
   \rm -rf examples/core/*.out
   \rm -rf examples/core/output_*
   \rm -rf examples/core/pipe_saved*.yml
else
   \rm -rf "${RAILDIR}"/core/*.out
   \rm -rf "${RAILDIR}"/core/output_*
   \rm -rf "${RAILDIR}"/core/pipe_saved*.yml
fi