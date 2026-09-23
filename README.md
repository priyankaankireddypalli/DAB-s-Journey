# DAB-s-Journey 

CI/CD workflow it is, dev, git - combination of everything

Note: asset bundles are generally used with cloud services.

Backbone of DAB's through 
1. DB's CLI
2. Also, DB's git folder can also
3. VS CODE

Databricks CLI - a rest api call to databricks

Install databricks CLI - https://learn.microsoft.com/en-us/azure/databricks/dev-tools/cli/install#homebrew-install

lets start our development in VS code editor

Quick check: 
make sure vs code editor is able to read databricks cli

# databricks -v

two types of authentication
1. user to machine (easy to set up)
2. machine to machine - service principles

i wanna talk to databricks from vs code cli are authenticate?

U2M authentication we will 
# databricks auth login host_connection_detail_of_Sql_warehouse

profile name - dev

It actually creates a .cfg (configuration file) for databricks authentication

# databricks --profiles list

# databricks -h 

# databricks auth profiles

# databricks schemas create bronze assetbundles --profile dev


What are databricks assets bundle?
Before understanding dab's, lets understand devops ci/cd

1. Planning phase 
2. define the code base
3. build
4. test
5. release
6. deploy it to different env - prod
7. make it live
8. monitor it and enhance required (again do it)


Dev (continuous integration) - Ops (continuous deployment)

asset bundles fit into right part of deployment

Asset Bundles are new way to deploy the changes into diferent env.
Makes CI/CD easy, more efficient and configure and change at any moment.


# databricks bundle init - initiaize the bundle
default_python template
unique name for project - dabtutorial (recognize it has bundled project)


1. .databricks folder is a transactional log for this bundle
2. fixtures -
3. resources - 
4. src - source code
5. tests - 
6. scratch - exploration (you dont want to deploy that changes)
7. .gitignore
8. databricks.yml
9. pyproject.toml
10. README.md


In databricks lets create an env - PROD


In vs code you want to develop something

In real world, you work in agile methodology 

you need to deploy that one notebook
> open databricks.yml (YAML) Human readable format of json.

# databricks bundle -h

# databricks bundle deploy --target dev
the moment it will add that bundle in databricks workspace


deploys notebooks


Lets say we have source folder - deploy notebooks 

Lets say you have a job - databricks job (how can you deploy it)
recommended - create jobs using databricks ui and later copy the code 
To deploy it - edit as yaml (copy the code and paste it in vs code editor > databricks.yml file (resources: )

when we have many jobs it is good to separate it (in resources > job folder > create file  demojob.yml 
and paste code 
and include that files in databricks.yml file) change notebook_path: since it contains email and it is not correct when deploying it to multiple environments

notebook_path: relative url and configure jobs must include 
notebook_path: ../../src/notebooks/notebook1.ipynb

when deployed : it creates a job with [dev name] jobname
It is cutom presets will be present 
in databricks.yml file - 

presets: (databricks will add by default)
name_prefix: dev_${workspace.current_user.short_name}
source_linked_deployment: false # always false everytime (we used notebook directly from .bundle folder but if we do not make it false if we have some notebooks which are not used from src folder (overriding the value)

# ideally you should not do this

# databricks bundle deploy --target dev

deleting .databricks folder (and then deploy) deploys everythung fresh

Importance of .databricks folder and how asset bundles track the changes within this .databricks 
transactional log (version control system) > sync-snapshots (.json(timestamp of every folder or file is present) - snapshot of when was last deployed
before deploying it will check this file 

it keeps separate environments for .databricks.

Deployment to Prod Environment

since we have only one workspace, we can use the same host

permissions:
  - user_name:
  - level: CAN_MANAGE

  - group_name: databricks identity and accesss

It was mentioned that profiles will be used but in bundles we are not specifying profiles.
So, whenever we specify target it looks for host and it searches that host in our profiles and already authenticated, it will automatically auth all the requests.

always validate before deploying to other environments

# databricks bundle summary --target prod 

Validate it
# databricks bundle validate --target prod

Deploy it to prod

# databricks bundle deploy --target prod

How to deploy bundles using databricks repo's or git folders as well using web terminal
create, use web terminal and deploy everything (also deploy DLT with using UI) 
code editor (difficult)



Databricks UI part 

1. Github account and repo should be ready

Databricks repo's or databricks git folder - is a way to work with differnt branches  so you dont overlap with other changes.

Similar to git

You need to have a git hub rep - attach local repo with remote repo (git hub is a remote repo)


















