Important! You need to update your upstream ref in git! Please run the following commands if you pulled BEFORE we changed to RocketMap. These steps will ensure you are using our repository.
```
git remote set-url origin https://github.com/RocketMap/RocketMap.git
git remote set-url origin --push https://github.com/RocketMap/RocketMap.git
git pull
```
This will set your remotes to pull from our repository. It is very important that you do this, otherwise you will have issues with git pulling in the future!
