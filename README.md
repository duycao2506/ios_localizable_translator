# iOS Localizable Translator
## Prerequisites
- Python3
## Installations & Usage
- Clone this repo 
```sh
git clone https://github.com/duycao2506/ios_localizable_translator.git
``` 
- Run 
```sh
python3 ios_localizable_strings.py <your-swift-file-containing-folder> --output <output-name-without-extension> --no-comments --locale-origin <src-lang-code> --locale-target <target-lang-code>
```
- If the translated terms remain the same as the source language, please check if this python lib needs any upgrades: 
    https://github.com/ssut/py-googletrans
- For further editing:
    You can convert .strings file to .po file with translate-toolkit
    https://github.com/translate/translate
    and edit with poeditor free version
    https://poedit.net

## Credits and reference
Thanks for the base from konalexiou: 
https://github.com/konalexiou/ios_localizable_strings_finder
