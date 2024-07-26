def annotated(enforced: bool = True):
    def typed(func):
        annotations = func.__annotations__

        if len(annotations) < func.__code__.co_argcount + 1:
            raise TypeError(f"{func.__name__} is not fully annotated")

        def inner(*args, **kwargs):
            to_name = lambda ann: ann.__name__ if isinstance(ann, type) else ann

            for i, (arg, ann) in enumerate(zip(args, annotations.values())):
                if ann and not isinstance(arg, ann):
                    raise TypeError(f"arg[{i}] must be {to_name(ann)}")

            for k, v in kwargs.items():
                if (ann := annotations.get(k)) and not isinstance(v, ann):
                    raise TypeError(f"argument '{k}' must be {to_name(ann)}")

            if (result := func(*args, **kwargs) is None) and (ann := annotations.get('return') is None):
                return result

            if not isinstance(result, ann):
                raise TypeError(f"return type must be {to_name(ann)}")

            return result

        return inner if enforced else lambda *args, **kwargs: func(*args, **kwargs)

    return typed
