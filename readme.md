# Bert-based Information Summarizer

## How it works
It first uses BERT-pretrained model to do the embedding for the sentences, then running a clustering algorithm (DBSCAN). 
After that, we use BERTSUM (https://github.com/ptarau/sumbert) to further generate a summary based on the output from the DBSCAN.

## Previous work
Derek Miller's has proposed a paper using BERT and some clustering algorithm (KMean) in the paper (https://arxiv.org/pdf/1906.04165.pdf). But there are some limitations in his work. Our approach has overcomed some weakness. This tool utilizes the HuggingFace Pytorch transformers library to run extractive summarizations. 
This library also uses coreference techniques, utilizing the 
(https://github.com/huggingface/neuralcoref) neuralcoref library to resolve words in summaries that need more context. The greedyness of 
the neuralcoref library can be tweaked in the CoreferenceHandler class.
Paper (https://arxiv.org/abs/1906.04165)

## Features ##

- [Django compressor](http://django-compressor.readthedocs.org/en/latest/) to compress JS and CSS and compile LESS/SASS files.
- [Pipenv](https://docs.pipenv.org) To manage dependences and virtualenvs.
- [Django debug toolbar](http://django-debug-toolbar.readthedocs.org/) enabled for superusers.
- [Argon2](https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#using-argon2-with-django) to hash the passwords

## Quickstart ##

### Install packages ###
pip install pandas
pip install gensim
pip install scipy
pip install sklearn
pip install matplotlib

pip install torch
pip install matplotlib
pip install seaborn
pip install django
pip install django-compressor 
pip install django-debug-toolbar

pip install sumbert
pip install summarizer-yshi0914


Make sure you have [pipenv installed](https://docs.pipenv.org/install.html). Then install Django 2.0 in your virtualenv:

    pip install django

To create a new Django project (make sure to change `project_name`)

    django-admin.py startproject --template=https://github.com/fasouto/django-starter-template/archive/master.zip --extension=py,md,html,txt project_name

cd to your project and install the development dependences

    pipenv install --dev

If you need a database, edit the settings and create one with
   
    pipenv run python manage.py migrate

Once everything it's setup you can run the development server: [http://localhost:8000/](http://localhost:8000/)

    pipenv run python manage.py runserver

## How to use it ##

### Settings ###

Settings are divided by environments: production.py, development.py and testing.py. By default it uses development.py, if you want to change the environment set a environment variable:

    export DJANGO_SETTINGS_MODULE="my_project.settings.production"

or you can use the `settings` param with runserver:

    pipenv run python manage.py runserver --settings=my_project.settings.production

If you need to add some settings that are specific for your machine, rename the file `local_example.py` to `local_settings.py`. This file it's in .gitignore so the changes won't be tracked.



