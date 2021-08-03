# FlyByWire Development Guide Overview

## Development practices

FlyByWire Simulations aims to maintain professional standards as well as industry-wide best practices in order to maximize developer productivity and deliver high-quality, tested products.

This is why we adopt a set of rules and practices that create a strong framework, not only around the usage of `git` but also surrounding code quality.

### Version control

Our version control approach maintains the following guidelines:

- Commit messages should be short and to the point. The [Angular commit message convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format) is often used and recommended but not enforced at the moment
- Merge commits are discouraged in commit histories and disallowed when merging pull requests
- Squash commits are exclusively used for pull request merges
- One approving review from a maintainer is required to merge a pull request
- Positive reports from a number of QA testers (varies depending on the PR scope and size) are required before merging, unless a maintainer judges appropriate to bypass this rule
- Creation of draft pull requests is required when a developer wishes to get working on a project, to avoid duplicate PR situations

### Code quality

Code quality is of an utmost importance as it allows other developers to more easily find bugs and understand logic.

An ESLint configuration is provided and should cover most code style rules.

A few guidelines apply:

- Prefer self-documenting code over having to write tons of comments
- However, do not hesitate to write comments when complex logic is used
- Use language-specific docstring tools (JSDoc, rustdoc)
- Maintain separation of concerns
- Do not be afraid to separate code into logical blocks, even if resulting sub-functions are only used locally (while maintaining a reasonable limit)
- (aircraft development specific) Avoid polling - prefer reactive APIs (but remain sure of not introducing state that cannot be externally read)
- Avoid introducing new technologies/languages without talking with the development team

Additionally, a few practices are straight up forbidden:

- Do not use `async/await` without a good reason (it does not make code run faster unless you are calling threaded APIs like `fetch`)
- Do not use hungarian notation (b, m, g identifier prefixes)
- Do not perform business logic calculations in presentation code
