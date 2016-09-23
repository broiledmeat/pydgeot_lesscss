import os
from lesscpy.lessc import parser, formatter
from pydgeot.processors import register, Processor


@register(name='lesscss')
class LessCSSProcessor(Processor):
    """
    Compile a Less (http://lesscss.org) source file in to the build directory.
    """
    def __init__(self, app):
        super().__init__(app)
        self._parser = parser.LessParser()

    def can_process(self, path):
        """
        :type path: str
        :rtype: bool
        """
        from .dirconfig import DirConfig
        config = DirConfig.get(self.app, path)
        return path.endswith(config.source_ext)

    def prepare(self, path):
        """
        :type path: str
        """
        self.app.sources.set_targets(path, [self.target_path(path)])

    def generate(self, path):
        """
        :type path: str
        """
        from .dirconfig import DirConfig

        config = DirConfig.get(self.app, path)
        target_path = self.target_path(path)
        formatter_ = formatter.Formatter(self._LessOpts(xminify=config.minify))

        self._parser.parse(filename=path)

        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, 'w') as fh:
            fh.write(formatter_.format(self._parser))

    def target_path(self, path):
        """
        :type path: str
        :rtype: str
        """
        from .dirconfig import DirConfig
        config = DirConfig.get(self.app, path)
        path = path[:-len(config.source_ext)] + config.build_ext
        return self.app.target_path(path)

    class _LessOpts:
        def __init__(self, minify=False, xminify=False, tabs=False, spaces=True):
            self.minify = minify
            self.xminify = xminify
            self.tabs = tabs
            self.spaces = spaces
