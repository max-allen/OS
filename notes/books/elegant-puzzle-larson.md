# Text Notes: An Elegant Puzzle

#management

## Ch. 2: Organization Design

- **Small teams (< 4) aren't teams**: An important property of teams is that they abstract the complexities of individuals that compose them.

- State changes for teams are reached through applying the correct system solution, not tactics alone
  - system solutions should be applied prior to tactical approaches

- Don't optimize globally (shifting eng. resources as priorities change), resist changes to high performing teams.
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

## Ch. 4: Approaches
&nbsp;
### Philosophy of Management

&nbsp;
#### Foundational management principles:[^1]

- **Golden Rule**: Treat others as you'd like to be treated).
- **Explicit Ownership**: Give each team member an explicit area of ownership.
- Rewards should be given only when work is _finished_ (see
[[finishing-projects]]).
- **Lead from the front**: Assuming an active, hands on role. Willingness to take on IC tasks, incident management / on call rotations, etc. as necessary. Never ask anyone to do something you wouldn't.

#### Principals forged from trial and error:

- **Management should be an ethical profession**: Recognize the huge impact your actions (or inaction) have on the people that work "for" you and assume responsibility for it.
  - **Compensation philosophy/practices**, how roles are pitched to candidates, promotions, growth opportunities, PTO requests, working hours.

- **Great relationships trump problems**: Almost any internal problem can be traced back to a missing or poor relationship. With great relationships, any problem can be solved. Prioritize addressing relationship trouble before attempting to fix a problem through other means.

- **People over process**: "With the right people, any process works, and with the wrong people, no process works." Process should improve collaboration. The process the team enjoys is usually the correct one. Before modifying process, investigate why the process is failing and consider whether its a people problem instead.

- **Do the hard thing now**: Postponement is rarely the answer. A poor relationship with an EM / teammate should be addressed by spending more time together. Have engineers at odds spend additional time together sharing perspectives before separating them.

- **Company -> Team -> Yourself**: When decision making, prioritize doing the right thing in this order.
  - **Company first**: What you do shouldn't create negative externalities for the company. Ex: Choosing to use a technology you're interested in, despite the maintenance cost it imposes on the company.
  - **Team over self**: What's best for the team should take precedence over self. Ex: Failing to push back on a timeline because it'd require uncomfortable conversations with your PM.

**Think for yourself**:
  - **The worst theory of management is to not have a management philosophy, but the second worst is one that doesn't change**: Things should be done with intention. It's okay to adopt practices of others, but never blindly. Review your practices regularly for correctness make adjustments as necessary instead of leaving on autopilot.
  - Common management challenges: interviewing, performance management, promotions, raises


### Ways EMs Get Stuck


[^1]: These were principles of Larson's at the start of his management career.