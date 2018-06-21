%module simple_ns

%{
#define SWIG_FILE_WITH_INIT
#include <stdio.h>
#include "c_source/noise_suppression_x.h"
#include "c_source/simple_nsx.h"
#include "c_source/noise_suppression_x.h"
#include <stdlib.h>
#include "c_source/real_fft.h"
#include "c_source/nsx_core.h"
#include "c_source/nsx_defines.h"
#include "c_source/complex_fft_tables.h"
#include "c_source/digital_agc.h"
#include "c_source/ring_buffer.h"
#include "c_source/simple_nsx.h"
#include "c_source/noise_suppression.h"
#include "c_source/spl_inl.h"
#include "c_source/gain_control.h"
#include "c_source/nsx_core.h"
#include "c_source/cpu_features_wrapper.h"
#include "c_source/typedefs.h"
#include "c_source/windows_private.h"
#include "c_source/analog_agc.h"
#include "c_source/fft4g.h"
#include "c_source/resample_by_2_internal.h"
#include "c_source/signal_processing_library.h"
#include "c_source/real_fft.h"
#include "c_source/ns_core.h"
#include "c_source/noise_suppression_x.h"
#include "c_source/defines.h"
#include "c_source/nsx_defines.h"
%}

extern void *webrtc_nsx_create(int mode);
extern void webrtc_nsx_process(void *inst, int16_t *dataL, int16_t *dataout);
