
"""
setup.py
"""
 
from distutils.core import setup, Extension
 
 
simple_ns_module = Extension('_simple_ns',
                           sources=['c_source/simple_nsx.c', 
                                    'c_source/nsx_core_neon_offsets.c', 
                                    'c_source/analog_agc.c', 
                                    'c_source/cross_correlation.c', 
                                    'c_source/noise_suppression.c', 
                                    'c_source/division_operations.c', 
                                    'c_source/fft4g.c', 
                                    'c_source/complex_fft.c', 
                                    'c_source/min_max_operations.c', 
                                    'c_source/complex_bit_reverse.c', 
                                    'c_source/resample.c', 
                                    'c_source/downsample_fast.c', 
                                    'c_source/nsx_core_c.c', 
                                    'c_source/energy.c', 
                                    'c_source/simple_ns_wrap.c', 
                                    'c_source/spl_sqrt.c', 
                                    'c_source/vector_scaling_operations.c', 
                                    'c_source/copy_set_operations.c', 
                                    'c_source/real_fft.c', 
                                    'c_source/ns_core.c', 
                                    'c_source/resample_48khz.c', 
                                    'c_source/resample_fractional.c', 
                                    'c_source/ring_buffer.c', 
                                    'c_source/resample_by_2_internal.c', 
                                    'c_source/spl_init.c', 
                                    'c_source/noise_suppression_x.c', 
                                    'c_source/resample_by_2.c', 
                                    'c_source/get_scaling_square.c', 
                                    'c_source/dot_product_with_scale.c', 
                                    'c_source/splitting_filter.c', 
                                    'c_source/spl_sqrt_floor.c', 
                                    'c_source/digital_agc.c', 
                                    'c_source/nsx_core.c', 
                                    'c_source/resample_by_2_mips.c'],
                           )
 
setup (name = 'simple_ns',
       version = '0.1',
       author      = "Weldon",
       description = """Simple swig simple_ns""",
       ext_modules = [simple_ns_module],
       py_modules = ["simple_ns"],
       )
