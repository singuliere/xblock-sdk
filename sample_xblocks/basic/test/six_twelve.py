# fs-s3fs==0.1.5 requires six 1.10.0 and ensure_str is not available there, we need 1.12.0
def six_ensure_str(s, encoding='utf-8', errors='strict'):
    """Coerce *s* to `str`.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> `str`
      - `bytes` -> decoded to `str`
    """
    if not isinstance(s, (six.text_type, six.binary_type)):
        raise TypeError("not expecting type '%s'" % type(s))
    if six.PY2 and isinstance(s, six.text_type):
        s = s.encode(encoding, errors)
    elif six.PY3 and isinstance(s, six.binary_type):
        s = s.decode(encoding, errors)
    return s

def six_ensure_binary(s, encoding='utf-8', errors='strict'):
    """Coerce **s** to six.binary_type.

    For Python 2:
      - `unicode` -> encoded to `str`
      - `str` -> `str`

    For Python 3:
      - `str` -> encoded to `bytes`
      - `bytes` -> `bytes`
    """
    if isinstance(s, six.text_type):
        return s.encode(encoding, errors)
    elif isinstance(s, six.binary_type):
        return s
    else:
        raise TypeError("not expecting type '%s'" % type(s))
