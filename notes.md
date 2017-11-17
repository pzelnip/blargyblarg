# Gittin good at git

- stash
- showing squashing
- dangers of squashing
- git bisect
	- working example of finding a bug
	- example of test runner suddenly breaking & finding bad test from months ago
- showing gitconfig & aliases
- git extras
- cherry picking for fun and profit

---------------

## Stash

A way to temporarily save uncommitted changes to allow you to switch to other branches.

```
git stash
```

To restore previously stashed changes:

```
git stash pop
```

To see what's previously been stashed:

```
git stash list
```

To discard the top-most stashed item:

```
git stash drop
```

_pro-tip_: if you want to turf all uncommitted changes you can do a ```git stash ; git stash drop``` (obviously do with care)

## Squashing

Take a series of commits and turn them into a smaller series of commits

```
git rebase -i <targetBranch>
```

Drops you into interactive mode where you can pick which commits to "squash"

Useful for turning a series of micro commits into a single logical commit.

-----------------

## Dangers of Squashing

*You're rewriting history!*

Rebase interactive mode is extremely dangerous as accidentially entering the wrong thing can result in losing work.

_pro-tip_: before rebasing, create new branch from old branch: ```git checkout -b squashed_feature_branch```

-----------------

## Git Bisect

Quite possibly one of the coolest (though rarely used) git commands I've ever seen.

Allows you to search through a series of commits to find the first commit where a fault condition was introduced.

Basic commands:
```
git bisect start

git bisect bad
git bisect good <sha>
git bisect run <command>
git bisect log

git bisect reset
```

## .gitconfig And Aliases

A .gitconfig file in your home directory controls various user-specific settings for git such as your name, email, etc.

It also allows you to define alises, which are effectively new git commands.

Mine can be found at: https://github.com/pzelnip/dotfiles/blob/master/dotfiles/.gitconfig

Common use cases:

- shorten commands ("git b" vs "git branch")
- commands for common switches ("git graph" vs "git log --oneline --decorate --graph")
- make git do things that are cray-cray via shell scripting

_pro-tip_: on *nix systems if you create an executable command (shell script, etc) called "git-foo" then doing "git foo" will execute that script

## Git Extras

Project originally started by TJ Holowaychuk (local Victoria guy who's done some crazy stuff in the JS space -- mocha, express, etc).

Bunch of common new commands, aliases, scripts, etc to make git life easy.  Check them out at:

https://github.com/tj/git-extras
and
https://github.com/tj/git-extras/blob/master/Commands.

If on OSX can install via homebrew:

```
brew install git-extras
```
If not on OSX, well, you should be (or just go to https://github.com/tj/git-extras/blob/master/Installation.md to find instructions for your platform).