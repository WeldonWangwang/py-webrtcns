#ifndef _SIMPLE_NSX_H_
#define _SIMPLE_NSX_H_
#include "noise_suppression_x.h"
typedef NsxHandle simple_nsx;

void *webrtc_nsx_create(int mode);

void webrtc_nsx_process(void *inst, int16_t *dataL, int16_t *dataout);

#endif