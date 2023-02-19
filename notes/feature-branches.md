# Feature Branches

Ideally, feature branches don't spend too much time in any particular state. They otherwise become difficult to manage. Once they've entered code review, care should be taken to move them along as quickly as possible, while maintaining standards of code review / QA.

This is particularly important as the number of contributors to the repository increases; this is doubly the case as the number of changes introduced becomes sufficiently large (number of files changed is a metric to pay attention to here).

Failure to progress the branch in a timely fashion may result in the following:

- A feature branch significantly behind the base
	- rebase hell, large merge commits
		- "ghost changes" introduced by merge commits

- A branch perennially conflicted with the base

## Rebasing

- If changes will be relied on heavily by other tickets to be picked up in current sprint, it increases the burden of reconciling changes across the various feature branches.

- Better to separate what can be done independently from what relies on in progress tickets