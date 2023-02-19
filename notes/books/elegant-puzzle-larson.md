# An Elegant Puzzle

**Ch. 2: Organization Design**

- **On small teams (< 4) not being teams**: An important property of teams is that they abstract the complexities of individuals that compose them.

- State changes for teams are reached through applying the correct system solution, not tactics alone
  - system solutions should be applied prior to tactical approaches

- Don't optimize globally (shifting eng. resources as priorities change), resist changes to high perforing teams.
  - [[jelling]] costs
  - Fixed costs: More teams have fixed costs and limited variable costs. Moving one person can take result in multiple teams performing suboptimally.
  - Time to task completion approaches infinity as team utilization approaches 100%, and most teams have deps  on other teams, resources to a team can have the effect of slowing it down by creating upstream constraints.
  - **An alternative to moving people is shifting scope of teams.**
    - avoids jelling costs
    - preserves system behavior

"All real world systems have some degree of self healing properties." An overloaded DB will slow down until someone fixes it, and overwhelmed employees will slow down at finishing work until someone finds a way to help."

"Productively integrating large numbers of engineers is hard."

Concentrate growth by having teams alternate between periods of hiring and consolidation

Cost of new hires:
  - Time spent hiring / interviewing
  - Time trained engineers must spend onboarding new hires
  - Every order of magnitude means a new layer of management is necessary
  - ~10 hires means a new team is required
  - More commits and deployments, which means more incident management / outages
  - More engineers means more specialized teams / systems, which means increasingly small on call rotations.

"Hiring is slowing us down": At high enough rates, the marginal added value of hiring gets very low. Sometimes low means negative.
