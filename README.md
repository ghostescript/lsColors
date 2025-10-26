# lsColors
Changes the color of a file type using the 'ls' command for fast and easy identification.

<br>

# Installation 
```bash
git clone https://github.com/ghostescript/lsColors
cd lsColors
python set_ls_color.py
```

<br>

* Copy, rename and move the script to home directory or any path of your choice for easy configuration.

<br>

```bash
# cd lsColors
cp set_ls_color.py set-lsColors.py
mv set-lsColors.py /home/kali/
mv /home/kali/set-lsColors.py /home/kali/set_ls_color.py
```

<br>

# Quick Usage
![alt text](https://raw.githubusercontent.com/ghostescript/lsColors/refs/heads/main/files/Screenshot_20251025-211453_Termux.jpg)

<br>

# Examples

<br>

* Show the help message and exit.
```bash
python set_ls_color.py
```

<br>

* List available file types, colors, and attributes.
```bash
python set_ls_color.py -l
```

<br>

 * List all 256 color codes.
```bash
python set_ls_color.py list-colors
```

<br>

* Change your directories to color 178 (orange)
```bash
python set_ls_color.py DIR 256 178 bold
```

<br>

* Change .txt files magenta in color.
```bash
python set_ls_color.py .txt magenta normal
```

<br>

* Change .py scripts cyan in color.
```bash
python set_ls_color.py .py cyan bold
```

<br>

# Execute Changes

```bash
eval "$(dircolors -b .dir_colors)"
```

<br>

> ⚠️ NOTE: This command will execute the ``.dir_colors`` file, your current and last saved configuration. When logging out of a session colors reset by default and you will need to execute the command again by itself to view your saved configuration.

<br>

# Updated On
``Oct 25, 2025``

<br>
