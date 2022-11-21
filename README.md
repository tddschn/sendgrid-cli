# sendgrid-cli

A very simple SendGrid CLI written in Python with only basic functionalities (at this moment).

The official [sendgrid-cli](https://github.com/sendgrid/sendgrid-cli) hasn't been updated in years and I couldn't get it to work,  
so I wrote this with only the features I need.

If you need more features, feel free to contribute by submitting pull requests.

- [sendgrid-cli](#sendgrid-cli)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage](#usage)
    - [On the command line](#on-the-command-line)
    - [On GitHub Actions](#on-github-actions)
  - [Develop](#develop)


## Installation

### pipx

This is the recommended installation method.

```
$ pipx install sendgrid-cli
```

### [pip](https://pypi.org/project/sendgrid-cli/)

```
$ pip install sendgrid-cli
```

## Usage

### On the command line

```
usage: sendgrid [-h] [-V] [-t str [str ...]] [-f str] [-n str] [-s str]

sendgrid CLI

options:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -t str [str ...], --to-emails str [str ...]
                        To emails (default: None)
  -f str, --from-email str
                        From email EMAIL (default: None)
  -n str, --from-name str
                        From name NAME (default: None)
  -s str, --subject str
                        Subject (default: None)

Email body (HTML) is read from stdin, supply your API key with SENDGRID_API_KEY environment variable

```

### On GitHub Actions

Below is a working job configuration

```yaml
  send-mail:
    runs-on: ubuntu-latest
    steps:
      - name: setup python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: install CLI tools
        run: pipx install sendgrid-cli
      - name: Send email
        env:
          SENDGRID_API_KEY: ${{ secrets.SENDGRID_API_KEY }}
        run: |
          cat email-body.html | sendgrid -f 'from@example.com' -n 'from-name' -t 'to@example.com' -s 'sendgrid-cli test'
```

## Develop

```
$ git clone https://github.com/tddschn/sendgrid-cli.git
$ cd 
$ poetry install
```