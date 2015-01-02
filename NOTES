
Working through the book. These are my notes.
The book: http://git-scm.com/book/en/v2/

So far, the commands I've learned are:
git config --global user.name $value
git config --global user.email $value
git config --global core.editor $value

git init - to create a repository in a given directory

git clone https://path/to/repo
e.g.  git clone https://github.com/libgit2/libgit2

git add
git status [-s]
git commit [-a to include un-staged or un-cached files]
git rm $file
git mv $file

git log
git log -p -2
    -p : show diffs
    -2 : only the last two commits
    --oneline : like --pretty=oneline, but uses short versions of the hashes
    --stat : show stats about each change
    --pretty=[oneline|short|full|fuller] : Output format changes
    --pretty=format:....
	e.g. git log --pretty=format:"%h - %an, %ar : %s"
    --since=2.weeks : or with relative dates, or specific times.
    --author
    --grep : works on commit messages
    -Sfunctionname : show the last commit to touch the string functionname
    -- $path - only show details about files in $path
  --decorate - Include branch information in the commits

git commit --amend to modify a previous commit. You can also add files to the
staging area (cached area) and run --amend to add new files to the previous
commit.

git reset HEAD $file - to move a file from staging back to tracked and modified.

To revert all changes to a modified and tracked file, 'git checkout -- <file>'

Remote repositories:
    git remote - list your remote repositories
    git remote add $shortname $url - Add remote $url to your current dir
    git remote rename $shortname $anothername - Rename
    git fetch $shortname - Pull down changes from $shortname to current dir.
    git fetch origin - Fetch latest from origin, if you've cloned a repo this
	pulls the latest changes down. THIS DOES NOT MERGE
    git pull - Fetch latest from origin and merge.
    git push [remote-name] [branch-name] - Push changes from your branch up to
	[remote-name]
      e.g. git push origin master
    git remote show [remote-name] - Details on the remote repo

Tagging
  git tag - list the tags
  git tag -l $glob - list tags matching the glob
  git tag [tag] - Tag the current branch with a lightweight tag.
  git tag -a [tag] [-m 'commit message'] - Annoated tag at the current release.
  git tag -a [tag] [-m 'commit message'] [hash] - Annotated tag at commit
    [hash]

  Tags aren't pushed to remote servers by default. Push them with:
  git push [remotename] [tag] - e.g. git push origin v0.1
  git push [remotename] --tags - to push all local tags to the server.

  To checkout a specific tag, you create a new branch at the given tag
    git checkout -b version2 v2.0.0

Aliases
  To not have to type in the whole command every time, you can set up basic
aliases. For example:
  git config --global alias.co checkout
    Then you only need to type 'git co' instead of 'git checkout'
  Also use this to fix oddities in the CLI. For instance, to fix the risky
reset command:
  git config --global alias.unstage 'reset HEAD --'
    Then
  git reset HEAD fileA == git unstage fileA
  git config --global alias.last 'log -1 HEAD'
  'Also prepend the command with ! to run an external command. e.g.
    git config --global alias.visual '!gitk'

Branches
  git branch testing - Create branch 'testing'. DOES NOT SWITCH TO IT
  git checkout testing - Switch to branch 'testing'
    Note that this moves HEAD to point to the testing branch.
  git branch -d - delete branch
  git checkout -b foo - create branch foo and switch there.
  git brnach -v - To see branches and their commit hash

  To merge back into branch 'master', do:
    git checkout master
    git merge otherbranch
  resolve conflicts through editing files, or using 'git mergetool'
  Always look at 'git status' to see the current state.

For seeing a good list of commits, use:
  git log --oneline --decorate --graph --all
