# Pelican Website for Adam Li

To add additional content, add to the `content/` folder.

To re-deploy changes to github pages run the following command:

Before doing anything, check locally if files look right:

    make html && make serve

First just push all your stuff to your path.

    git add -A && git commit -a -m 'first commit' && git push --all

Then:

    make github


## Pelican Themes and PlugIns

In order to make the above work, you will need to also have the `pelican-themes` and `pelican-plugins` folder locally as a "sub-module".

You can clone those repos locally from https://github.com/getpelican/pelican-plugins and https://github.com/getpelican/pelican-themes.

# To Setup Virtual Environment

I make use of a `Pipfile` to setup a virtual environment.

# TO ADD
publication list: https://github.com/vene/pelican-bibtex
