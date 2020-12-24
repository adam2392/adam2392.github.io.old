# Pelican Website for Adam Li

To add additional content, add to the `content/` folder.

To re-deploy changes to github pages run the following command:

Before doing anything, check locally if files look right:

    make html && make serve

First just push all your stuff to your path.

    git add -A && git commit -a -m 'first commit' && git push --all

Then:

    make github