# DON'T DELETE THIS FILE!
# Add this file for a bug cause by 'watchdog', when execute: `pecan serve
# config.py --reload`, python will raise a exception as below:
# TypeError: expected str, bytes or os.PathLike object, not NoneType
# while `pecan serve config.py` works well.
# I only found the problem in archlinux system.
