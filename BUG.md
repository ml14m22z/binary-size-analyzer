# BUG


### BUG_20231122_1

```bash
$ ./binary_size_analyzer ./DCPS/
Traceback (most recent call last):
  File "main.py", line 39, in <module>
  File "main.py", line 26, in main
  File "main.py", line 34, in analyze_file
  File "analyzer/size_analyzer.py", line 20, in analyze_size
  File "utils/helper.py", line 18, in calculate_file_size
  File "genericpath.py", line 50, in getsize
FileNotFoundError: [Errno 2] No such file or directory: 'not found'
[390855] Failed to execute script 'main' due to unhandled exception!
```

```bash
$ ldd UnionTopic
        linux-vdso.so.1 (0x00007ffdf15f5000)
        libOpenDDS_Dcps.so.3.27.0-dev => not found
        libTAO_Valuetype.so.2.5.20 => not found
        libTAO.so.2.5.20 => not found
        libACE.so.6.5.20 => not found
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fa52d7f5000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fa52d7ce000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007fa52d7ab000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fa52d5b9000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fa52d46a000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fa52dc05000)
```

Conclusion: The LD_LIBRARY_PATH not set!

Open.
