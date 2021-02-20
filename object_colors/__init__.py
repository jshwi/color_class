"""
object-colors
=============

Object-oriented library for stylizing terminal output.
"""
import builtins

import colorama

__version__ = "1.0.8"


class Color:
    """Color object. Args passed to constructor call may be strings or
    integers. There are a defined set of options for each. The list
    of options referenced below are the string form. The integer that
    can be called is the index of the list item beginning with 0.

    @DynamicAttrs

    :param effect:  Effect applied to text output. Select from the
                    following :py:attr:`Color.effects`.
    :param fore:    Foreground color applied to text output. Select from
                    the following :py:attr:`Color.colors`.
    :param back:    Background color applied to text output. Select from
                    the following :py:attr:`Color.colors`.
    """

    effects = (
        "none",
        "bold",
        "dim",
        "italic",
        "underline",
        "blink",
        "blinking",
        "negative",
        "empty",
        "strikethrough",
    )
    colors = (
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    )
    _opts = dict(effect=effects, fore=colors, back=colors)
    colorama.init()

    def __init__(self, effect=0, fore=7, back=None):
        self.effect = effect
        self.fore = fore
        self.back = back
        object.__setattr__(self, "_objects", dict())

    def __setattr__(self, key, value):
        """The two types of attributes to set are the object's instance
        attributes, and the dynamic object attributes. Standard
        attributes can be either ``int``, ``str``, or ``NoneType``.
        Object values can only be a ``dict`` i.e. ``**kwargs`` to create
        a new object. All ``int`` values correspond to the index of the
        color or effect and their respective ANSI code. All ``str``
        values will be converted to their index integer. If a key does
        not match ``effect``, ``fore``, or ``back`` it must be a
        ``dict`` which can be instantiated to create a new named object.

        :param key:         The attribute to set.
        :param value:       The value of the attribute to set.
        :raises ValueError: If ``str`` does not a match a ``str`` in the
                            corresponding tuple.
        :raises TypeError:  If an unknown keyword is provided and the
                            value is not a ``dict``.
        """
        if key in self._opts:
            if isinstance(value, str):
                value = self._opts[key].index(value)

            object.__setattr__(self, key, value)
        else:
            if not isinstance(value, dict):
                raise TypeError(
                    "got an unexpected keyword argument '{}'".format(key)
                )

            self._objects[key] = self.__class__(**value)

    def __getattribute__(self, key):
        """Attempt to return the attribute matching the key. If no
        attribute can be found search ``_objects`` for objects. If
        neither of the above can yield a result then raise
        ``AttributeError`` error.

        :param key:             The attribute to get.
        :raises AttributeError: Raise if no instance attribute or
                                objects can be returned with the given
                                key.
        :return:                The retrieved attribute.
        """
        try:
            return object.__getattribute__(self, key)

        except AttributeError as err:
            try:
                return self._objects[key]

            except KeyError:
                raise AttributeError(err) from err

    def __repr__(self):
        """View the containing attributes within the ``str``
        representation.

        :return:  ``str`` representation of this class.
        """
        return "{}({})".format(
            type(self).__name__,
            ", ".join(
                "{}={}".format(k, v)
                if not isinstance(v, dict)
                else "objects({})".format(", ".join(v))
                for k, v in vars(self).items()
            ),
        )

    def _get_colored_str(self, _str):
        """Compile and return ANSI escaped string.

        :param _str:    Regular ``str`` object.
        :return:        ``str`` with escape codes added.
        """
        return "\u001b[{};3{}{}m{}\u001b[0;0m".format(
            self.effect,
            self.fore,
            f";4{self.back}" if self.back is not None else "",
            _str,
        )

    def populate(self, elem):
        """Create an object for every available selection.

        :param elem:            Attribute to fill with available
                                options.
        :raises AttributeError: If element does not exist.
        """
        kwargs = {k: v for k, v in vars(self).items() if not k.startswith("_")}
        try:
            for item in self._opts[elem]:
                kwargs[elem] = item
                setattr(self, item, kwargs)

        except KeyError as err:
            raise AttributeError(
                "'{}' has no attribute '{}'".format(type(self).__name__, elem)
            ) from err

    def populate_colors(self):
        """Create an object for every available foreground color.
        Deprecated.
        """
        self.populate("fore")
        for color in self.colors:
            getattr(self, color).populate("effect")

    def set(self, **kwargs):
        """Call to set new instance values. If not making a subclass
        then process args and kwargs and add compiled dict to
        masterclass.

        :key effect:    Text effect to use.
        :key fore:      Color of text foreground.
        :key back:      Color of text background.
        :key ``dict``:  If ``**kwargs`` are provided then any keyword
                        can be provided.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, *args, **kwargs):
        """Return colored ``str`` or ``tuple`` depending on the arg
        passed to method.

        :param args:    Manipulate string(s).
        :key format:    Return a string instead of a tuple if strings
                        are passed as tuple.
        :return:        Colored string.
        """
        if len(args) > 1:
            if kwargs.get("format", False):
                return self._get_colored_str(" ".join(args))

            return tuple(self._get_colored_str(i) for i in list(args))

        return self._get_colored_str(args[0])

    def print(self, *args, **kwargs):
        """Print colored strings using the builtin ``print`` function.

        :param args:    String(s) to print.
        :key file:      A file-like object (stream); defaults to the
                        current sys.stdout.
        :key sep:       String inserted between values, default a space.
        :key end:       String appended after the last value, default a
                        newline.
        :key flush:     Whether to forcibly flush the stream.
        """
        builtins.print(self.get(*args, format=True), **kwargs)
