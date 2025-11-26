# {{ site.title }}

__Author:__ {{ site.author }}  
__Version:__ {{ site.version }}  

## Overview
{{ site.description }}  

***

## Command Examples:
### 🔧 cc-utils (add_docs, extract, run, list)
#### Add Docs  
__Description:__ Add GitHub docs to an existing project using the github-docs-cookiecutter template.  
1.  
``` shell
$ cc-utils add-docs --help
```

#### Extract  
__Description:__ Clone a repo, extract cookiecutter.json, remove Jinja placeholders, save locally.  
1.  
``` shell
$ cc-utils extract ./python3-cookiecutter  
```
2. Modify extracted json to meet you new projects requirements.  

3. Run ccutils extract command:  
``` shell
$ cc-utils extract \
    --repo git@github.com:jcook3701/python3-cookiecutter.git \
    --branch develop \
    --output clean_cookiecutter.json  
```

#### Run  
__Description:__ Run a cookiecutter template using a pre-supplied JSON configuration file.  
```shell
$ cc-utils run --help
```

#### List
__Description:__ List available cookiecutter templates under a namespace.  
```shell
$ cc-utils list --help
```

***

### ⚙️ Config (cc-config)
__Description:__ cc-utils configuration tools.

#### Sub-commands: (show)

#### Show
__Description:__
```shell
$ cc-config show
```

***

### 🔨 Build (cc-build)
__Description:__ Cookiecutter build automation utilities.

#### Sub-commands: (readme, add-yaml-front-matter)

#### Readme
__Note__: Replace with real values.  
```shell
$ cc-build readme $(JEKYLL_DIR) ./README.md \
		--tmp-dir $(README_GEN_DIR) --jekyll-cmd '$(JEKYLL_BUILD_CMD)'
```

***

## 🍪 Template (cc-templates)
__Description:__ cc-templates tools.

#### Sub-commands: (readme, add-yaml-front-matter)

#### Generate: 
```shell
$ cc-templates generate
```

***

## Development
### 🐍️ Build environment (.venv)
``` shell
$ make install  
```
### 🔍 Linting (ruff & yaml-lint)
2.
``` shell
$ make lint-check  
```
``` shell
$ make lint-fix  
```
### 🎨 Formating (black)
```shell
$ make format-check
```
```shell
$ make format-fix
```
### 🧠 Typechecking (mypy)
``` shell
$ make typecheck  
```
### 🧪 Testing (pytest)
``` shell
$ make test  
```
### 📦 Building (build)
```shell
$ make build
```
### 🚀 Publishing (Twine)
```shell
$ make pubish
```
### Build Help
``` shell
$ make help  
```


### Authors Notes:  


### Future Ideas (TODOs):
1. cc-templates/ccindex.toml
  * create/update this file using the individual ccmeta.toml files in cc-templates

## Packages
### PyPi (stabale)

### TestPyPi (development)
https://test.pypi.org/project/cc-utils/