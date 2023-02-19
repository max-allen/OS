# Code Review

> A code review is often the first test of whether a given change is understandable to a broader audience.

Code will be read many more times than it is written. Vital to prioritize comprehension.

Focus Areas:

- Correct
- Clear
- Consistent
- Collective Ownership
- Knowledge Sharing
- Historical Record

"Request Changes" is used to request explicit resolution prior to merge. Relevant items should be detailed in review summary.

Benefits for Reviewer:

Reviewing code earnestly and regularly will improve your ability to think critically about code and provide constructive feedback.

Code Review can be a high leverage if done correctly. Reviewer can preempt costly mistakes and improve changes without time spent authoring

Good Practices:

Leave a review summary when you've completed the review. That way the reviewer knows they can safely return to working on it.

Write good change descriptions: they can serve as historical record of any change introduced. The first line should indicate the type of change. Remainder of description should detail what is being changed and _why_. A common argument is that JIRA tickets can serve as the record. What this approach misses is that the merging of changes is often one of final point at which changes can be documented. Tickets on the other hand tend to be authored much much earlier prior to iteration / thrashing. Change descriptions also detail decisions made along the way for other developers