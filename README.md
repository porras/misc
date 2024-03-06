# Misc

This repository contains the specs for a bunch of Fedora packages I maintain on
https://copr.fedorainfracloud.org/coprs/porras/misc/. They are a bit random,
just stuff I use and is not packaged for Fedora. Hence the name "misc". Some of
them are work in progress but if they are here, I am using them. Feel free to
use them too if you find that useful, of course. They are:

* [cliphist](https://github.com/sentriz/cliphist)

The rest of this README is just private notes about housekeeping.

## Adding a new package

Given a spec file is added to this repo, usually the simplest way to build it
for the first time is pushing it manually to copr:

```sh
copr-cli build misc <spec-file>
```

## Updating a package

It is possible to simply do that again, but a more automated way is:

* Go to the [Copr
  GUI](https://copr.fedorainfracloud.org/coprs/porras/misc/packages/), find the
  package and click on "Edit"
* Fill in the part about the source: type is git, clone URL is this repository
  URL (it has to be HTTPS), and spec file is the path to the spec file in the
  repo.
* At the bottom of the form, check "Auto-rebuild" and hit "Save changes"

From now on, package rebuilds will be triggered by pushing a tag
`package-name>-<version>-revision>` to this repository.
