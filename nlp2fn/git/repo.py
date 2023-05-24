import subprocess


class Repo:
    def __init__(self, path):
        """
        Initializes a Repo object with the given path to the repository.
        """
        self.path = path

    def run_command(self, command):
        """
        Runs the specified command as a subprocess in the repository's working directory.

        Args:
            command (list): A list containing the command and its arguments.

        Returns:
            str: The output of the command as a string.
        """
        result = subprocess.run(command, cwd=self.path, capture_output=True, text=True)
        return result.stdout.strip()

    def clone(self, url):
        """
        Clones a Git repository from the specified URL into the repository's working directory.

        Args:
            url (str): The URL of the repository to clone.

        Returns:
            str: The output of the clone command.
        """
        return self.run_command(['git', 'clone', url, self.path])

    def commit(self, message):
        """
        Commits the changes in the repository with the specified commit message.

        Args:
            message (str): The commit message.

        Returns:
            str: The output of the commit command.
        """
        return self.run_command(['git', 'commit', '-m', message])

    def push(self):
        """
        Pushes the changes in the repository to the remote repository.

        Returns:
            str: The output of the push command.
        """
        return self.run_command(['git', 'push'])

    def pull(self):
        """
        Pulls the latest changes from the remote repository.

        Returns:
            str: The output of the pull command.
        """
        return self.run_command(['git', 'pull'])

    def add(self, files):
        """
        Adds the specified files to the staging area.

        Args:
            files (list): A list of file paths to add.

        Returns:
            str: The output of the add command.
        """
        return self.run_command(['git', 'add'] + files)

    def status(self):
        """
        Retrieves the current status of the repository.

        Returns:
            str: The output of the status command.
        """
        return self.run_command(['git', 'status'])

    def branch(self):
        """
        Retrieves the name of the currently active branch.

        Returns:
            str: The name of the active branch.
        """
        return self.run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])

    def create_branch(self, branch_name):
        """
        Creates a new branch with the specified name.

        Args:
            branch_name (str): The name of the new branch.

        Returns:
            str: The output of the branch creation command.
        """
        return self.run_command(['git', 'branch', branch_name])

    def checkout_branch(self, branch_name):
        """
        Switches to the specified branch.

        Args:
            branch_name (str): The name of the branch to switch to.

        Returns:
            str: The output of the branch checkout command.
        """
        return self.run_command(['git', 'checkout', branch_name])

    def merge(self, branch_name):
        """
        Merges the specified branch into the current branch.

        Args:
            branch_name (str): The name of the branch to merge.

        Returns:
            str: The output of the merge command.
        """
        return self.run_command(['git', 'merge', branch_name])

    def diff(self):
        """
        Retrieves the differences between the working directory and the index.

        Returns:
            str: The output of the diff command.
        """
        return self.run_command(['git', 'diff'])

    def log(self):
        """
        Retrieves the commit log of the repository.

        Returns:
            str: The output of the log command.
        """
        return self.run_command(['git', 'log'])
