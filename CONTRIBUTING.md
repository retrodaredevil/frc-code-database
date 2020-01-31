# Contributing
Contributions are welcome! Feel free to submit pull requests to add your team's repositories other other team's repositories.

Make sure you have an understanding of how git submodules work and put the submodules in the correct directory locations.

When creating pull requests, please state if you are from the team you are submitting code for.

### Adding repositories
If you are unfamiliar with submodules, [read here](https://git-scm.com/book/en/v2/Git-Tools-Submodules).

To add a repository, first cd to the correct directory
```shell script
mkdir -p frc/<team number>/<year>
# For example:
mkdir -p frc/1444/2020
```
Now change your directory to it
```shell script
cd frc/<team number>/<year>
# For example:
cd frc/1444/2020
```
Now you can add it using submodules:
```shell script
git submodule add <link to git repository>
# For example:
git submodule add https://github.com/frc1444/robot2020
```

### Updating repositories
Constantly updating your repository is frowned upon as this is a database of repositories and not necessarily something to update every time you push.
However, every once in a while, you are welcome to update your submodule. In the future, we may automate this.

### Removing repositories
If you would like to completely remove your repository, you can submit a pull request, an issue, or PM [retrodaredevil](https://github.com/retrodaredevil) directly (by email) (if you are from the team that owns the repository).

### .gitignore
Did we miss something in [.gitignore](.gitignore)? Feel free to add it if you make a pull request for something else.
