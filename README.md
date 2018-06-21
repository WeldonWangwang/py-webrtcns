# py-webrtcns
Python interface to the WebRTC Noise Suppression  

This repertory contains the pre-compiled `.so` files, which can be used directly.  

The pre-compiled '.so' files in `build/lib.linux-x86_64-2.7`, named `_simple_ns.so`.

## How to recompile `so` files  

- Set up swig
- run `swig -python simple_ns.i`
 - This step will generate two new files: `simple_ns_wrap.c` and `simple_ns.py`  
- run `python setup.py build`  
 - This step will generate `.so` files in `build/lib*`  

## How to use the `.so` files  

You can use `test.py` to test the WebRTC Noise Suppression basic functions.