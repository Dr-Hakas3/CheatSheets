converting code from Python 2 to Python 3.
```zsh
2to3-2.7 -w 40280.py
```

# Example Truble shuuting

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python3 40280.py internal
  File "/home/kali/CTF/OffSec/Internal/40280.py", line 19
        print '\nUsage: %s <target ip>\n' % sys.argv[0]
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python2 40280.py internal
Traceback (most recent call last):
  File "40280.py", line 12, in <module>
    from smb.SMBConnection import SMBConnection
ImportError: No module named smb.SMBConnection
```

```zsh
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python3 -m venv venv 
                                                                                                                    
┌──(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ source venv/bin/activate
                                                                                                                    
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ pip install pysmb

Collecting pysmb
  Downloading pysmb-1.2.14-py3-none-any.whl.metadata (1.6 kB)
Collecting pyasn1 (from pysmb)
  Downloading pyasn1-0.6.3-py3-none-any.whl.metadata (8.4 kB)
Collecting tqdm (from pysmb)
  Downloading tqdm-4.67.3-py3-none-any.whl.metadata (57 kB)
Downloading pysmb-1.2.14-py3-none-any.whl (85 kB)
Downloading pyasn1-0.6.3-py3-none-any.whl (83 kB)
Downloading tqdm-4.67.3-py3-none-any.whl (78 kB)
Installing collected packages: tqdm, pyasn1, pysmb
Successfully installed pyasn1-0.6.3 pysmb-1.2.14 tqdm-4.67.3
```

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python2 get-pip.py
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
100  1.81M 100  1.81M   0      0 12.48M      0                              0
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.                                                                              
Defaulting to user installation because normal site-packages is not writeable
Collecting pip<21.0
  Downloading pip-20.3.4-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 6.1 MB/s 
Collecting wheel
  Downloading wheel-0.37.1-py2.py3-none-any.whl (35 kB)
Installing collected packages: pip, wheel
Successfully installed pip-20.3.4 wheel-0.37.1
```

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python2 -m pip install "setuptools<45"
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.                                                                              
Defaulting to user installation because normal site-packages is not writeable
Collecting setuptools<45
  Downloading setuptools-44.1.1-py2.py3-none-any.whl (583 kB)
     |████████████████████████████████| 583 kB 4.8 MB/s 
Installing collected packages: setuptools
Successfully installed setuptools-44.1.1
```

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python2 get-pip.py pysmb              
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. pip 21.0 will drop support for Python 2.7 in January 2021. More details about Python 2 support in pip can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support pip 21.0 will remove support for this functionality.                                                                              
Defaulting to user installation because normal site-packages is not writeable
Collecting pysmb
  Using cached pysmb-1.2.14.tar.gz (1.2 MB)
Collecting pip<21.0
  Using cached pip-20.3.4-py2.py3-none-any.whl (1.5 MB)
Collecting pyasn1
  Downloading pyasn1-0.5.1-py2.py3-none-any.whl (84 kB)
     |████████████████████████████████| 84 kB 2.2 MB/s 
Collecting tqdm
  Downloading tqdm-4.64.1-py2.py3-none-any.whl (78 kB)
     |████████████████████████████████| 78 kB 4.0 MB/s 
Collecting importlib-resources; python_version < "3.7"
  Downloading importlib_resources-3.3.1-py2.py3-none-any.whl (26 kB)
Collecting singledispatch; python_version < "3.4"
  Downloading singledispatch-3.7.0-py2.py3-none-any.whl (9.2 kB)
Collecting typing; python_version < "3.5"
  Downloading typing-3.10.0.0-py2-none-any.whl (26 kB)
Collecting zipp>=0.4; python_version < "3.8"
  Downloading zipp-1.2.0-py2.py3-none-any.whl (4.8 kB)
Collecting contextlib2; python_version < "3"
  Downloading contextlib2-0.6.0.post1-py2.py3-none-any.whl (9.8 kB)
Collecting pathlib2; python_version < "3"
  Downloading pathlib2-2.3.7.post1-py2.py3-none-any.whl (18 kB)
Collecting six
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Collecting scandir; python_version < "3.5"
  Downloading scandir-1.10.0.tar.gz (33 kB)
Building wheels for collected packages: pysmb, scandir
  Building wheel for pysmb (setup.py) ... done
  Created wheel for pysmb: filename=pysmb-1.2.14-py2-none-any.whl size=84352 sha256=2b55bb03da82b8a4e2fffcbd63f49bc04286aa837a51ea455b5194640a703f51
  Stored in directory: /home/kali/.cache/pip/wheels/2b/7a/2d/0d4a33fc1b11037e6225a75671a4c4e1cb325323f5da051d1c
  Building wheel for scandir (setup.py) ... done
  Created wheel for scandir: filename=scandir-1.10.0-cp27-cp27mu-linux_x86_64.whl size=11146 sha256=adf4f03bb7ca295b0e881bfc269cbc4a8998b81d6048e71505a56d2da76c9e13
  Stored in directory: /home/kali/.cache/pip/wheels/58/2c/26/52406f7d1f19bcc47a6fbd1037a5f293492f5cf1d58c539edb
Successfully built pysmb scandir
Installing collected packages: pyasn1, six, singledispatch, typing, contextlib2, zipp, scandir, pathlib2, importlib-resources, tqdm, pysmb, pip
  Attempting uninstall: pip
    Found existing installation: pip 20.3.4
    Uninstalling pip-20.3.4:
      Successfully uninstalled pip-20.3.4
Successfully installed contextlib2-0.6.0.post1 importlib-resources-3.3.1 pathlib2-2.3.7.post1 pip-20.3.4 pyasn1-0.5.1 pysmb-1.2.14 scandir-1.10.0 singledispatch-3.7.0 six-1.17.0 tqdm-4.64.1 typing-3.10.0.0 zipp-1.2.0
```

```zsh
┌──(venv)─(kali㉿kali)-[~/CTF/OffSec/Internal]
└─$ python2 40280.py internal
Password for [WORKGROUP\Administrator]:
Cannot connect to server.  Error was NT_STATUS_LOGON_FAILURE
```

...Search other