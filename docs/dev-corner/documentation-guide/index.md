---
title: Overview
description: Overview of the FlyByWire Documentation Guide
---

# FlyByWire Documentation Guide

 [:fontawesome-brands-github:{: .github } -  **Documentation Project GitHub**](https://github.com/flybywiresim/docs){target=new .md-button}

## Background

!!! info "Guides"
    If you would like to setup the documentation project locally please continue with this guide.

    If you would like to understand our guidelines on writing and different available features please see the [Writing Documentation](writing-documentation.md) Page instead.

The FlyByWire Documentation Project aims to provide all necessary information and documentation to successfully install and use the FlyByWire A32NX aircraft in Microsoft Flight Simulator.

For this, we provide documentation about the A32NX add-on itself, but also valuable additional documentation on how to fly an airliner on Microsoft Flight Simulator in general and even some specific A320neo documentation for the more involved user.

We apply very high standards to the quality and accuracy of our documentation so that it is easy to read and understand but also as correct as possible. Therefore, we have a strict quality process and everything is reviewed by several users and real pilots from our team.

## How to Contribute

### Contacts for FlyByWire Documentation Team

If you have questions or suggestions, or if you want to contribute to the FlyByWire Documentation project, please contact us on Discord:

[:fontawesome-brands-discord:{: .discord } - **Discord Link**](https://discord.gg/flybywire){target=new}

- valastiri
- cdr_maverick
- slein15

### Required Tools

To participate in the FlyByWire Documentation Project, you need to have the following tools installed:

- GitHub account and Git ([GitHub Quickstart](https://docs.github.com/en/get-started/quickstart){target=new})
- Python ([Python Downloads](https://www.python.org/downloads/){target=new})
- Install the following Python-based tools (see install command below):
    - MkDocs ([MkDocs](https://www.mkdocs.org/){target=new})
    - mkdocs-awesome-pages-plugin
    - mkdocs-git-revision-date-localized-plugin
    - mkdocs-redirects
    - mkdocs-embed-external-markdown
    - mkdocs-video
    - mike
    - pillow
    - cairosvg
- Create and activate a Python Virtual Environment (`virtualenv`) to be used for working on the documentation project:
    ```title="Run In Terminal"
    python -m venv venv
    ```

    Once created, you need to activate it. Use the following command on Windows:
    ```title="Activating virtualenv on Windows"
    .\venv\Scripts\activate.bat
    ```
    Or the following command on Linux and macOS:
    ```title="Activating virtualenv on Linux and macOS"
    source venv/bin/activate
    ```
- Install dependencies with this single line command:
    ```title="Run In Terminal"
    pip install -r requirements.txt
    ```
!!! info "Using `virtualenv`"
    Starting with Python 3.11, the `pip` tool will fail to install dependencies and packages globally, instead it's recommended to use `virtualenv`. If you desire to install packages globally, you must use another tool, such as [`pipx`](https://github.com/pypa/pipx). We recommend using `virtualenv` because it's easier and the recommended way to work on Python projects.
!!! danger "Activating `virtualenv`"
    It's important to note that `virtualenv` activation is not persisted. If you restart your terminal/command prompt and want to preview your work on the documentation project again, you have to reactivate your `virutalenv` using the appropriate activation command that was shown earlier in this guide.
!!! info "Pillow + Cairo Dependency"
    As part of the new social card feature released with `mkdocs-material 8.5.0` [Pillow](https://pillow.readthedocs.io/) and [Cairo Graphics](https://www.cairographics.org/) 
    dependencies were added. We bundle this as part of our `requirements.txt` to ensure the dependencies are installed when attempting to test [social cards locally](#social-cards-feature). If you encounter any issues with these python packages:

    - Install [GTK+](https://www.gtk.org/docs/installations/windows/) for Windows.

    For more information, including other operating systems, refer to the [Social Card Dependencies](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/#dependencies) Section on the `mkdocs-material` documentation.

- Editor / IDE:
    - Recommended: [Microsoft Visual Studio Code](https://code.visualstudio.com/docs#vscode){target=new}
        - recommended plugins to work with Markdown:
            - any markdown helper plugin - e.g., [https://github.com/yzhang-gh/vscode-markdown](https://github.com/yzhang-gh/vscode-markdown){target=new}
            - especially for tables: [https://github.com/darkriszty/MarkdownTablePrettify-VSCodeExt](https://github.com/darkriszty/MarkdownTablePrettify-VSCodeExt){target=new}
            - any plugin to enter Unicode symbols like the narrow non-breakable space for the thousand separator in numbers - e.g., [https://github.com/brunnerh/insert-unicode](https://github.com/brunnerh/insert-unicode){target=new}
    - Or any [JetBrains](https://www.jetbrains.com/) IDE, e.g. IntelliJ IDEA or Clion.
    - Or any text editor (even Notepad.exe will do) in conjunction with [stackedit.io](https://stackedit.io/){target=new} - Create and edit markdown on the web. Useful if you don't have / can't set up MkDocs locally on your machine. Does not support material references. Please note this in your PR, so a maintainer can double-check your references render appropriately.

#### Social Cards Feature

!!! danger "Important Information"
    For general purposes, you do not need to test or utilize this feature locally unless you want to develop or change configurations related to this feature. Please be aware of
    the information below if you intend to test this locally.

We have added the social cards feature to the FBW documentation project. When generating the social cards locally, the directory `.cache` is created where all the assets are generated. See [Complete Local Builds](#complete-local-builds).

You may need to manually clean any files within the `.cache` directory if you encounter any build issues after generating / modifying configuration files related to this 
feature.

### Process

#### Preview your Local Clone

- Fork the [:fontawesome-brands-github:{: .github } -  **Documentation Project GitHub**](https://github.com/flybywiresim/docs){target=new} ([How to fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo){target=new}).
- Create a local clone ([How to clone your forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository){target=new}).
- Checkout the "primary" branch - this is the main branch of the current FlyByWire Documentation Project.
- In a command line terminal, go to the cloned repository folder and start `mkdocs.exe serve` to start the local preview server.

    This should look like this:

    ```
    > mkdocs.exe serve
    INFO     -  Building documentation...
    INFO     -  Cleaning site directory
    INFO     -  Documentation built in 4.03 seconds
    INFO     -  [12:05:30] Serving on http://127.0.0.1:8000/
    ```
  
    !!! danger "Building the Project with No Internet Connection"
        This project utilizes the `external-markdown` plugin, which pulls MarkDown files from other repositories during the build for both production and development. This helps reference other important documentation externally without having to copy and paste it into this project.
        
        When working on a feature branch without an internet connection, your development server may exit and fail to build, resulting in:
        
        ```
        Error! https://[hyperlink here] returned connection error
        ```
        
        ---

        To bypass this issue, you can comment out the `external-markdown` plugin temporarily in `mkdocs.yml` found in the /root of this project. (Please ensure not to commit this change 
        when creating a Pull Request.) See the example below:

        ``` { .yaml .annotate title="mkdocs.yml example configured for offline builds" }
        # Plugins
        plugins:
        search:
          lang: en
        # Comment out the plugin below if building docs without an internet connection.
        # external-markdown: {} (1)
        ```

        1. For production or PR purposes, please ensure that the above plugin reads `external-markdown: {}` (without the preceding `#`) before finalizing your PR.
  
!!! info "Faster Preview Server"
    You can opt to use a faster instance of the developer server by invoking the flag `--dirty`. This just checks for any markdown that has changed since the HTML was rendered and will reconstruct any relevant pages only, rather than rebuilding the entire website.

    ```
    mkdocs.exe serve --dirty
    ```

    !!! danger ""
        Navigation and new internal links may not get updated on other pages while using `--dirty`. Verify links using the standard serve or build command.

- You can now browse the current checked out branch in a browser at this address: [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The site renders every time you save any `filename.md` you are working on.
- Optional: Build a static site locally for testing:

    ```
    mkdocs build --clean --no-directory-urls
    ```

    - The site will be built locally under `/site` on in your local repo for user testing. Open`index.html` in the root of `/site` to preview.
    - Note: `--no-directory-urls` allows usage of reference links when browsing the locally built site. Prevents having to find each index.html related to every `filename.md` to preview the relevant page.

#### Make Changes or Additions to the Documentation

- Create a new branch based on branch "primary" (might differ for certain subprojects) and checkout this new branch. Give a short but meaningful name to the branch.
- Make initial changes to your local branch.
- Create a [Draft Pull Request](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-forkhttps://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork){target=new} (aka PR) early to let people know what you are working on.
    - Explain in the PR Description what you are changing/adding and how people should review your changes.
- Work on your changes locally, preview constantly and push your changes regularly to get a preview deployment for others to provide feedback.
    - Every time you push changes to your PR, a preview is generated with a URL. You can share this link in Discord for the team to provide feedback easily. The URL (by the Vercel bot) is visible as a comment on your PR GitHub page.
- When finished, push your final changes to the PR, update the PR description if required and mark it "[Ready for Review](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/changing-the-stage-of-a-pull-request#marking-a-pull-request-as-ready-for-review){target=new}".
- Someone from the documentation team will review your changes, provide feedback, potentially ask for changes, and eventually approve and merge your changes.

#### Adding Plugins or Markdown Extensions

Please use the alternative "key/value" pairs method when adding plugins or markdown extensions, with special note that an empty value must be provided when no options are defined.

```yaml title="Sample New Config"
plugins:
  search: {}
  awesome-pages: {}
```

```yaml title="Old Config"
plugins:
    - search
    - awesome-pages
```

### Build Pipeline and Config Changes

To facilitate smooth local development, we have made some changes between production builds and local development.

Building for production now uses the `production.yml` file, which deep merges with mkdocs.yml using the `INHERIT` function with MkDocs.

`mkdocs build --config-file production.yml`

#### Complete Local Builds

You can still follow the instructions to [preview your local clone](#preview-your-local-clone) to test and preview your changes locally.

If you would like to fully test a complete build of the production website, you need to run the following:

- `mkdocs.exe serve --config-file production.yml` 
- `mkdocs.exe build --clean --no-directory-urls --config-file production.yml`

!!! info "Additional Plugins in `production.yml`"
    The following plugins are included:
    
    - Social Cards

## Ideas and Issues

Please use GitHub's Issue tracker for any documentation request or issues you might have encountered.

 [:fontawesome-brands-github:{: .github } -  **Documentation Project Issues**](https://github.com/flybywiresim/docs/issues){target=new}

