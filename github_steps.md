# Visit github.com/new to create a new repository on GitHub.
github.com/new

# Clone the newly created repository to your local machine.
# This creates a local copy of the repository that you can edit.
git clone https://github.com/johnmelodev/scrapy.git

# Change to the directory of the cloned repository.
# This command changes the current working directory to the specified directory.
cd /Users/joaomelo/scrapy-com-selenium1

# Check the status of your Git repository.
# This command shows which changes have been made that have not yet been committed.
git status

# Add all current changes to the next commit.
# The '.' means "the current directory", so this command adds all changes in the current directory and its subdirectories.
git add .

# Commit the changes that you added.
# This saves the changes in the Git history with a commit message 'initial'.
git commit -m 'initial'

# Send the changes to the remote repository on GitHub.
# This synchronizes your local repository with the repository on GitHub.
git push

# VPS

https://github.com/johnmelodev/scrapy
https://cloud.linode.com/linodes SSH access 
# paste in the terminal the SSH # ssh root@198.58.xxx.xxx
git clone https://github.com/johnmelodev/scrapy
# username: johnmelodev
# password: your_git_hub_token

venv
python3 -m venv joao
source joao/bin/activate

# install chrome
sudo apt update -y
sudo apt upgrade -y
