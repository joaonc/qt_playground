More info in [Managing releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).

Using GH CLI (TODO: More info here.)

Authenticating:
```
gh auth login
```

Sample output from logging in with the `HTTPS` protocol and via web browser.
```
gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations on this host? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 9999-9999
Press Enter to open github.com in your browser... 
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as <GH username>
```

## Creating a release

1. Update (increase) the app version in `assets/app.yaml`.
2. Create and merge a new PR called "Preparing for v1.2.3" release.  
   This merges the new version, which will be used to create the release and set it to the right
   commit hash.
3. Run `inv build.release`
   Use the `--notes` or `--notes-file` to add more details to the release.  
   See sections below for beta and draft releases.

### Beta

### Draft
