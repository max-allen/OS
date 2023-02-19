# Dependency Management

How do we properly address problems attributable to changes made outside of the organization, without complete access or visibility?

Questions to Answer:
 - How / When should we take on external dependencies?
 - How we should we address breaking changes between releases?
 - When should we update?

This problem increases in complexity with scale.

> All else being equal, prefer source control problems over dependency-management problems.

SC problems can be dealt with more simply and cheaply than DM problems.

As OSS grows, dependency graphs continue to expand.

Difficulty

Managing a network of dependencies and their changes over time. A subset of the network is required for first-party code, some is required by transitive dependencies.

Over a long enough period of time, each of the nodes will have new versions, and some of the updates will be significant. How is the resulting cascade of changes managed?

- How do we find mutually compatible versions for all deps  given we don't control them?
- How do we analyze the dependency network?
- How is the network managed as the graph grows?

> Even if we import a dependency with no intent of upgrading it, security vulnerabilities, changing platforms, and evolving dependency networks can force the upgrade

Dependency provider should have compatibility promises documented. What are the expectations for ongoing support of previous releases?

Diamond Dependency Problem

This diamond can form at any scale: in the entire network of your dependencies, if there is ever a low-level node that is required to be in two incompatible versions at the same time (by virtue of there being two paths from some higher level node to those two versions), there will be a problem.

Embedding Multiple Versions

This can be made to work by tweaking the names of functions, but if there are types that are passed around between dependencies, all bets are off.

What's the growth in the transitive usage of the package?

Perhaps a dependency is well written, has no security bugs, and isn’t depended upon by other OSS projects. It might be possible for it to go quite a few years without being updated.

It’s not necessarily wise for that to happen: changes externally might have optimized it or added important new functionality, or cleaned up security holes before CVEs were discovered. The longer that the package exists, the more dependencies (direct and indirect) are likely to accrue. The more that the package remains stable, the more that we are likely to accrete Hyrum’s Law reliance on the particulars of the version that is checked into third_party.

Cost of Exporting a Package

Providing a dependency isn’t free: “throw it over the wall and forget” can cost you reputation and become a challenge for compatibility. Supporting it with stability can limit your choices and pessimize internal usage. Supporting without stability can cost goodwill or expose you to risk of important external groups depending on something via Hyrum’s Law and messing up your “no stability” plan.
