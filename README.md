# Roll of the Dice


## building instructions
```
pyinstaller --add-data "./assets/*:./assets" --onefile --windowed src/main.py --clean -n Dice --osx-bundle-identifier com.mustafahaddara.dice --noconfirm -i assets/dice.icns
```

TODO: `--target-arch universal2` requires universal install of python