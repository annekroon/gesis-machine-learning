# GESIS Fall Seminar in Computational Social Science 2025
## Introduction to Machine Learning for Text Analysis with Python

### Setup Guide

Welcome! In this guide, we will walk you through setting up a programming environment on your computer. The following steps will help you to configure the same environment that we will be working with during the course. However, you are free to deviate from this, if for example you already have a setup that works for you, or you simply prefer to experiment. Just make sure that, before the course begins, you can run python code, inside of a jupyter notebook. Reach out to us if you encounter issues!

> **⚠️ Important:** If you are using a work-managed laptop, you might run into permissions issues when performing this setup (as you, as the user, may not have the necessary administrative rights). Therefore, make sure that you attempt this setup with enough time to contact your ICT administrator should their assistance be needed.

## Prerequisites

You will need to access your system terminal to enter commands:

| Operating System | Instructions |
|------------------|--------------|
| **MacOS** | Press `⌘ + space` and enter: `terminal` |
| **Windows** | Press `ctrl + r` and enter: `cmd` |

## Step 1: Install Python

We recommend installing **miniconda**: https://docs.anaconda.com/miniconda/#quick-command-line-install

Miniconda is a free, lightweight tool for managing python environments and packages. It allows you to create isolated environments for different projects, each with its own set of packages and dependencies. This helps avoid conflicts between projects and keeps your system organized.

### MacOS Installation (arm64)

Copy/paste the following commands into your terminal:

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

> **Note:** If you have an older (Intel) Mac, substitute the 'arm64' in the second line for 'x86_64'.

### Windows Installation (x86)

Copy/paste the following commands into your terminal:

```cmd
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```

### Create a Conda Environment

With miniconda installed, let's try creating an environment. In your terminal, run:

```bash
conda create -n gesis_iml python=3.10 ipykernel
```

> **⚠️ Windows Users:** You might get an error saying that 'conda' is not recognized. If so, you will need to use **Anaconda Prompt** from here on to create/manage environments (search for it via the start menu). This is essentially the same thing as the Windows terminal (cmd), but it will recognize the 'conda' command above.

With this command, we're asking conda to create a new environment called 'gesis_iml' (or whatever you want to call it) and we're setting the python version to 3.10. By default, this will also install a list of commonly used packages. In addition, we also ask it to install the `ipykernel` package, which we need for working with jupyter notebooks.

### Activate Your Environment

Now that we have created an environment, activate it by running:

```bash
conda activate gesis_iml
```

That's it! Remember that you must check that your desired environment is currently active before running python code or installing packages. The name of the currently active environment will always be shown in parentheses next to the current cursor position.

**Additional Resources:** You can find more about creating and managing your environments here: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

## Step 2: Install GitHub Desktop and Clone the Course Repository

We recommend installing **GitHub Desktop**: https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop

This is the easiest way (for now) to access git-versioned repositories. Think of these as project folders that keep track of changes to files over time, including who made each change and when.

In this course, we only need to know how to 'clone' (take a copy of) a repository.

### Clone the Repository

1. From within the GitHub Desktop app, select **Add** → **Clone Repository** → **URL**
2. Clone the repository at: `https://github.com/annekroon/gesis-machine-learning.git`
3. Choose a local folder of your choosing

That's it! This folder will contain your copy of the course materials – lecture slides and exercises.

## Step 3: Install an Integrated Development Environment (IDE)

Your IDE will be where you spend many long and hopefully enjoyable hours working on your code… so it is important to pick a good one! We recommend installing **VSCode**: https://code.visualstudio.com/download

> **Note:** If you are prompted to choose between a 'user' and a 'system' level setup, choose **user**. Downstream tasks (like updates) will require less permission elevations, so there is less chance of encountering issues.

We recommend VSCode primarily as it is quite easy to get running ('out of the box'), but at the same time, provides plenty of room to grow. Many of its advanced features (which we will not need) can be hidden from view. You can also expand its functionality by installing 'extensions' as you need them.

### Install Required Extensions

Click on the **Extensions** tab on the left-hand side of the interface, search for, and install:

- **Python** – this extension allows VSCode to work seamlessly with your python environment(s)
- **Jupyter** – this allows VSCode to run Jupyter notebooks (where we will perform exercises)

### Test Your Setup

With these extensions installed, let's check that we can run python code inside of a jupyter notebook:

1. **Create a new Jupyter Notebook** via the command palette:
   - **MacOS:** Press `⌘ + Shift + P` and enter: `Create: New Jupyter Notebook`
   - **Windows:** Press `Ctrl + Shift + P` and enter: `Create: New Jupyter Notebook`

2. **In the empty cell, enter the following, and then run the cell** (`Shift + Enter`):
   ```python
   print('hello world!')
   ```

3. **Select your kernel:** The command palette will ask you which python kernel you would like to use to run the code. You should see the python environment you created earlier with miniconda. Select it.

4. **Verify output:** The cell should execute, and underneath it, you should see the output `hello world!`

> **Note:** For each new notebook, you only need to select the kernel once – it will remember and use it in the future.

## Optional: Co-pilot (AI Assisted Coding)

While not required for this course, we recommend learning to work with AI-assisted programming, as it will save you a good deal of time and frustration fixing errors with your code and can be an excellent learning tool.

For this, we recommend **Microsoft Copilot**, since it integrates into VSCode.

### Prerequisites

You will need a **GitHub Pro account**. This can be discounted (academic staff), or free (PhD students):
- Apply here: https://education.github.com/discount_requests/application
- **Note:** Approval can take a couple of days

### Setup

Once you have upgraded your account, follow these instructions to set up Copilot in VSCode: https://code.visualstudio.com/docs/copilot/setup

### Usage

There are two main ways to use Copilot: https://code.visualstudio.com/docs/copilot/getting-started

#### 1. Chat

Chat can be accessed by clicking the chat button to the right-hand side of the command palette (top). You can ask the assistant questions without specific context, or with specific context by highlighting the part of your code that you are asking about, before asking your question.

The latter is extremely useful: for example, you can highlight code from this course and ask it to explain the working of the code to you step-by-step. Or, to troubleshoot code that isn't behaving as expected.

> **⚠️ Important:** When using Chat, ensure that it is in **'Ask'** mode, and not 'Edit' or 'Agent' (you can change this via the bottom left corner of the chat box). The latter two allow co-pilot to make direct edits to your code and files. This is an advanced functionality that generally doesn't work very well, as you cede control over the composition of your code. It can be fun to experiment with, but for now: we recommend sticking with 'Ask'.

#### 2. Code Completion

Code completion is switched on by default and works in two ways:

##### Coding by Comments

This involves describing what you want in natural language and allowing the assistant to predict the required code for you. For example, you could type:

```python
# print the string: 'hello world!'
```

…and in the next line, the assistant will suggest something like this, which you can accept by pressing `Tab`:

```python
print('hello world!')
```

This is useful for relatively simple operations, but the assistant can become overwhelmed quite easily and produce code that – whilst might run – may not behave the way that you expect or may be needlessly long or complex. Therefore, instead of asking it to perform a more complex operation all at once, try to break the operation into simpler steps, using comments to 'guide' the assistant through each in order. This will ensure the most success.

##### Inline Completion

This involves writing the beginning of your code and allowing the assistant to predict the rest of your code for you. For example, if you type:

```python
print('hell
```

…the assistant will try to predict the remainder of your code, which you can accept by pressing `Tab`:

```python
print('hello world!')
```

Like coding by comments, the more wiggle-room the assistant has, the more likely it will get this prediction wrong, and produce code that does something that you don't want it to do. Therefore, it is best to leave a trail of 'breadcrumbs' by completing as much of the code you can yourself, until the suggestion is what you were after.

### Managing Copilot

**Important:** Copilot is aware of your existing code, so it will often try to predict what you want to write based on previous lines (even before you start typing). This can be useful, but it can also be quite distracting at times.

You can toggle on/off code completions using the command palette:
**GitHub Copilot: Enable/Disable Copilot completions**

### Privacy Disclaimer

⚠️ **Disclaimer:** As with all commercial AI offerings, presume that your interactions with Copilot (and the contents of your code) are retained by Microsoft.
