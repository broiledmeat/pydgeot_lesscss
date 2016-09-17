# LessCSS support for Pydgeot
Add support for [LessCSS](http://lesscss.org) files to [Pydgeot](http://www.github.com/broiledmeat/pydgeot).

### Requirements
- Python 3.*
- [Pydgeot](http://www.github.com/broiledmeat/pydgeot)
- [lesscpy](https://pypi.python.org/pypi/lesscpy)

### Installation
```bash
git clone https://github.com/broiledmeat/pydgeot_lesscss.git pydgeot_lesscss
cd pydgeot_lesscss
python setup.py install
```

### Configuration
Add `lesscss` to your pydgeot.conf `plugins` list.
```json
{
  "plugins": ["lesscss"]
}
```

### Usage
The LessCSS plugin will process any `.css` file as a LessCSS template.
