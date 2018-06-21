#include <stdio.h>
#include "noise_suppression_x.h"
#include "simple_nsx.h"

void *webrtc_nsx_create(int mode)
{
    void *nsInst;
    WebRtcNsx_Create(&nsInst);
    if (0 != WebRtcNsx_Init(nsInst, 16000)) {
        printf("WebRtcNsx_Init failed!\n");
        return NULL;
    }
    if (0 != WebRtcNsx_set_policy(nsInst, mode)) {
        printf("WebRtcNsx set policy failed!\n");
        return NULL;
    }
    return nsInst;
}

void webrtc_nsx_process(void *inst, int16_t *dataL, int16_t *dataout)
{
    WebRtcNsx_Process(inst, dataL, NULL, dataout, NULL);
}