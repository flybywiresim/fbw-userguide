---
title: Contribution Guidelines
description: Overview of the FlyByWire Contribution Guidelines
---

# Contribution Guidelines

Welcome to the FlyByWire Aircraft project repository. Thank you for your interest in contributing to the project. Full 
details and guidelines on how to ensure this project is managed well are included below.

As this is an open-source project, anyone is free to contribute as much or as little as they like.

If you're just getting started with GitHub or project contributions, then we suggest you take a look at issues on the 
repository. These issues will vary in complexity depending on the issue itself, but will give you a good insight into 
the different topics you could contribute to.

If you're comfortable contributing to Open-Source projects on GitHub, please ensure you read our expectations for issue 
tracking, feature proposals and pull requests.

If you're looking for tools and tips to help you develop, see [Development Resources](resources.md).

**Please avoid** adding features that are not true to life or features without providing supported documentation.

## Expectations

As contributors and maintainers of this project, we pledge to respect all people who contribute through reporting issues
, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, issues and
other contributions that are not aligned to this Code of Conduct.

Make sure to read our [Code of Conduct](https://github.com/flybywiresim/aircraft/blob/master/CODE_OF_CONDUCT.md)

## Pull Requests

We welcome pull requests with fixes and improvements to the project.

If you wish to add a new feature or you spot a bug that you wish to fix, **please open an issue for it first** on the
[FBW Aircraft issue tracker](https://github.com/flybywiresim/aircraft/issues).

The work-flow for submitting a new pull request is designed to be simple, but also to ensure consistency from **all** 
contributors:

- Fork the project into your personal space on GitHub.com.
- Create a new branch (with a clear name of what is being changed).
- Add changes to CHANGELOG.md with credits to yourself.
- Commit your changes.
- When writing commit messages, make sure they are clear about what has been changed.
- Push the commit(s) to your fork.
- Submit a pull request (PR) to the master branch.
- The PR title should describe the change that has been made.
- Follow the PR template and write as much detail as necessary for your changes, and include documents/screenshots if
  needed.
- Be prepared to answer any questions about your PR when it is reviewed for acceptance.

**Please** keep your changes in a single PR as small as possible (relating to one issue) as this makes it easier to 
review and accept.  Large PRs with a small error will prevent the entire PR from being accepted.

**Ensure** that you include a CHANGELOG with your PR.

## Helping others

Please help other contributors to the project wherever you can, as people all start somewhere. If you require assistance
or wish to provide assistance, you can ask/answer questions on the 
[#dev-support](https://discord.gg/v3jAxJpwZm){target=new} channel on discord.

## Finding tasks

The best place to look for possible things where you could contribute is the FBW Aircraft GitHub repository's 
[Issues List](https://github.com/flybywiresim/aircraft/issues){target=new}. There you can find open bug reports or 
feature requests from users or other developers.

## Issues

If you require **support** with the A32NX, please utilize the channels on our official 
[Discord](https://discord.gg/flybywire). Issues regarding the features or bugs will not be handled on Discord. Please 
use GitHub issues to track new features or bugs.

When submitting an issue, there are a few guidelines we'd ask you to respect to make it easier to manage and for others 
to understand:

- **Search the issue tracker** before you submit your issue - it may already be present.
- When opening an issue, a template is provided for you. Please provide as much information as requested to ensure 
  others are able to act upon the requests or bug reports.
- Please ensure you add screenshots or documentation references for bugs/changes, so we can quickly ascertain if the 
  request is suitable.

**To be 'assigned' an issue**, please comment on the issue itself, letting others know you are working on it.

## Code Quality

Code quality is of an utmost importance, as it allows other developers to more easily find bugs and understand logic.

An ESLint configuration is provided and should cover most code style rules.

A few guidelines apply:

- Prefer self-documenting code over having to write tons of comments
- However, do not hesitate to write comments when complex logic is used
- Use language-specific docstring tools (JSDoc, rustdoc)
- Maintain separation of concerns
- Do not be afraid to separate code into logical blocks, even if resulting sub-functions are only used locally (while 
  maintaining a reasonable limit)
- (aircraft development specific) Avoid polling - prefer reactive APIs (but remain sure of not introducing state that 
  cannot be externally read)
- Avoid introducing new technologies/languages without talking to the development team

Additionally, a few practices are straight up forbidden:

- Do not use `async/await` without a good reason (it does not make code run faster, unless you are calling threaded APIs
  like `fetch`)
- Do not use hungarian notation (b, m, g identifier prefixes)
- Do not perform business logic calculations in presentation code

## Version Control

Our version control approach maintains the following guidelines:

- Commit messages should be short and to the point. The 
  [Angular commit message convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format){target=new} 
  is often used and recommended but not enforced at the moment.
- Merge commits are discouraged in commit histories and disallowed when merging pull requests
- Squash commits are exclusively used for pull request merges
- One approving review from a maintainer is required to merge a pull request
- Positive reports from a number of QA testers (varies depending on the PR scope and size) are required before merging, 
  unless a maintainer judges appropriate to bypass this rule
- Creation of draft pull requests is required when a developer wishes to get working on a project, to avoid duplicate PR
  situations

## Testing

If changes are made, they should always be tested to make sure they work as intended and don't conflict with other 
systems. If you see a pull request open, it's recommended that you test the features that were implemented to check for 
errors, or whether it works as intended.

## References Material (real life aircraft)

Creating a high-fidelity aircraft is a serious task that requires focus and dedication. But more importantly, it's 
striving for accuracy and realism. Therefore, any change that affects the appearance or behavior of a plane needs to 
reference real documentation.

The maintainer team has the role of deciding if references are suitable for a change. It is understandable that new 
developers do not have access to in-depth resource material.

While material like that is generally not in the possession of new contributors, the development team is always 
available to confirm your changes or provide you with necessary info.

Our extensive pool of IRL A320/A380 pilots and aircraft maintenance engineers are also able to answer your questions 
whenever needed.
