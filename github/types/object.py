import typing
from datetime import datetime
from json import dumps


class Meta(type, metaclass=type("", (type,), {"__str__": lambda _: ""})):
    def __str__(self):
        return f"<class 'github.types.{self.__name__}'>"


class Object(metaclass=Meta):
    @staticmethod
    def default(obj: "Object"):
        if isinstance(obj, bytes):
            return repr(obj)

        if isinstance(obj, typing.Match):
            return repr(obj)

        return {
            "_": obj.__class__.__name__,
            **{
                attr: (
                    str(datetime.fromtimestamp(getattr(obj, attr)))
                    if attr.endswith("_at") else
                    getattr(obj, attr)
                )
                for attr in filter(lambda x: not x.startswith("_"), obj.__dict__)
                if getattr(obj, attr) is not None
            }
        }

    def __str__(self) -> str:
        return dumps(self, indent=4, default=Object.default, ensure_ascii=False)

    def __repr__(self) -> str:
        return "github.types.{}({})".format(
            self.__class__.__name__,
            ", ".join(
                f"{attr}={repr(getattr(self, attr))}"
                for attr in filter(lambda x: not x.startswith("_"), self.__dict__)
                if getattr(self, attr) is not None
            )
        )

    def __eq__(self, other: "Object") -> bool:
        for attr in self.__dict__:
            try:
                if getattr(self, attr) != getattr(other, attr):
                    return False
            except AttributeError:
                return False

        return True

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


if __name__ == '__main__':
    class A(Object):

        def __init__(self):
            self.a = 3
            self.b = "b"

    print(A())
