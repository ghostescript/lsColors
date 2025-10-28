#!/bin/bash

# Ensure the .dir_colors file exists before attempting to use it.
# This prevents errors if the file is not present.
if [ -f "$HOME/.dir_colors" ]; then
    eval "$(dircolors -b "$HOME/.dir_colors")"
else
    # If the custom file does not exist, use dircolors with its default database.
    eval "$(dircolors -b)"
fi

# Now, any subsequent `ls` commands in this script will use the new color scheme.
ls --color=auto




