def _allow_title_descr_posargs(error_cls):
    class error_cls_with_posargs(error_cls):
        def __init__(self, title=None, description=None, **kwargs):
            super().__init__(title=title, description=description, **kwargs)

    error_cls_with_posargs.__name__ = error_cls.__name__
    error_cls_with_posargs.__qualname__ = error_cls.__name__
    error_cls_with_posargs.__doc__ = error_cls.__doc__

    return error_cls_with_posargs
