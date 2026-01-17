# num2words2

[![PyPI version](https://badge.fury.io/py/num2words2.svg)](https://badge.fury.io/py/num2words2)
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](https://www.gnu.org/licenses/lgpl-2.1)
[![Python Versions](https://img.shields.io/pypi/pyversions/num2words2.svg)](https://pypi.org/project/num2words2/)

`num2words2` is an enhanced fork of the original `num2words` library that converts numbers like `42` to words like `forty-two`. It supports multiple languages and provides various improvements and bug fixes over the original package.

## Features

- Convert numbers to words in 50+ languages
- Support for cardinal, ordinal, currency, and year conversion
- Enhanced language support including recent additions
- Bug fixes for decimal handling, negative numbers, and float conversions
- Actively maintained with regular updates
- Drop-in replacement for the original num2words

## Installation

```bash
pip install num2words2
```

## Usage

### Basic Usage

```python
from num2words2 import num2words

# Cardinal numbers
print(num2words(42))  # forty-two
print(num2words(42, lang='es'))  # cuarenta y dos
print(num2words(42, lang='fr'))  # quarante-deux

# Ordinal numbers
print(num2words(42, to='ordinal'))  # forty-second
print(num2words(42, to='ordinal', lang='es'))  # cuadragésimo segundo

# Currency
print(num2words(42.50, to='currency'))  # forty-two euro, fifty cents
print(num2words(42.50, to='currency', lang='es'))  # cuarenta y dos euros con cincuenta céntimos

# Year
print(num2words(2024, to='year'))  # two thousand and twenty-four
```

### Command Line Interface

```bash
$ num2words2 10001
ten thousand and one

$ num2words2 24120.10
twenty-four thousand, one hundred and twenty point one

$ num2words2 24120.10 -l es
veinticuatro mil ciento veinte punto uno

$ num2words2 2.14 -l es --to currency
dos euros con catorce céntimos

# List all supported languages
$ num2words2 --list-languages

# List all converters
$ num2words2 --list-converters
```

## Supported Languages

`num2words2` supports over 50 languages:

- ar (Arabic)
- az (Azerbaijani)
- be (Belarusian)
- bn (Bengali)
- ca (Catalan)
- ce (Chechen)
- cs (Czech)
- cy (Welsh)
- da (Danish)
- de (German)
- el (Greek)
- en (English)
- eo (Esperanto)
- es (Spanish)
- fa (Persian)
- fi (Finnish)
- fr (French)
- he (Hebrew)
- hi (Hindi)
- hu (Hungarian)
- hy (Armenian)
- id (Indonesian)
- is (Icelandic)
- it (Italian)
- ja (Japanese)
- kn (Kannada)
- ko (Korean)
- kz (Kazakh)
- lt (Lithuanian)
- lv (Latvian)
- mn (Mongolian)
- nl (Dutch)
- no (Norwegian)
- pl (Polish)
- pt (Portuguese)
- ro (Romanian)
- ru (Russian)
- sk (Slovak)
- sl (Slovenian)
- sn (Shona)
- sr (Serbian)
- sv (Swedish)
- te (Telugu)
- tet (Tetum)
- th (Thai)
- tr (Turkish)
- uk (Ukrainian)
- vi (Vietnamese)
- yo (Yoruba)
- zh (Chinese)

And many regional variations like es_CO (Colombian Spanish), pt_BR (Brazilian Portuguese), etc.

## Improvements over Original num2words

- **Bug Fixes**: Fixed issues with negative decimal handling, float comparisons, and type conversions
- **Enhanced Language Support**: Added support for Armenian (hy), Mongolian (mn), Shona (sn), and other languages
- **Better Maintenance**: Regular updates and active issue resolution
- **Improved CI/CD**: Comprehensive testing across multiple Python versions
- **Type Safety**: Better type handling and error messages

## Migration from num2words

`num2words2` is designed as a drop-in replacement for `num2words`. Simply update your imports:

```python
# Before
from num2words import num2words

# After
from num2words2 import num2words
```

Or if you want to maintain compatibility:

```python
try:
    from num2words2 import num2words
except ImportError:
    from num2words import num2words
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-test.txt

# Run tests
python -m pytest tests/

# Run tests with coverage
python -m pytest tests/ --cov=num2words2
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GNU Lesser General Public License v2.1 - see the LICENSE file for details.

## Credits

`num2words2` is based on the original [num2words](https://github.com/savoirfairelinux/num2words) project by Savoir-faire Linux inc.

## Author

Maintained by Jean-Louis Queguiner

## Links

- [PyPI Package](https://pypi.org/project/num2words2/)
- [GitHub Repository](https://github.com/jqueguiner/num2words)
- [Issue Tracker](https://github.com/jqueguiner/num2words/issues)