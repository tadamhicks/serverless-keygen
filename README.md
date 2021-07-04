# morpheus-bundler-keygen

## Intro

This project uses the serverless node module framework.

## Getting started with developing

Life is easier with virtualenvs.  Use them.  This project is based on Python 3.

This project also uses serverless framework for wrapping CloudFormation Templating with AWS for resource stack creation.  Find more at https://serverless.com

```bash
npm init -f
npm install --save-dev serverless-wsgi serverless-python-requirements
export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
serverless deploy
```

This will result in command results like this:

```bash
Serverless: Generated requirements from /Users/adamhicks/gomorpheus/morpheus-bundler-keygen/requirements.txt in /Users/adamhicks/gomorpheus/morpheus-bundler-keygen/.serverless/requirements.txt...
Serverless: Using static cache of requirements found at /Users/adamhicks/Library/Caches/serverless-python-requirements/dad6737b2ea36ddd9e60031649d33e4656007814b26b1e16685af1f3801faf91_slspyc ...
Serverless: Warning: Please change "wsgi.handler" to "wsgi_handler.handler" in serverless.yml
Serverless: Warning: Using "wsgi.handler" still works but has been deprecated and will be removed
Serverless: Warning: More information at https://github.com/logandk/serverless-wsgi/issues/84
Serverless: Python executable not found for "runtime": python3.6
Serverless: Using default Python executable: python
Serverless: Packaging Python WSGI handler...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Creating Stack...
Serverless: Checking Stack create progress...
........
Serverless: Stack create finished...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service serverless-flask.zip file to S3 (12.24 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
....................................
Serverless: Stack update finished...
Service Information
service: serverless-flask
stage: dev
region: us-east-1
stack: serverless-flask-dev
resources: 13
api keys:
  None
endpoints:
  ANY - https://fiqozn0ia5.execute-api.us-east-1.amazonaws.com/dev
  ANY - https://fiqozn0ia5.execute-api.us-east-1.amazonaws.com/dev/{proxy+}
functions:
  app: serverless-flask-dev-app
layers:
  None
Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.
```

The endpoints can then be used to test.  Example:

```bash
export BASE_DOMAIN=https://fiqozn0ia5.execute-api.us-east-1.amazonaws.com/dev
curl -H "Content-Type: application/json" -X POST ${BASE_DOMAIN}/client_keys -d '{"client_id": "1234"}'

curl -H "Content-Type: application/json" -X GET ${BASE_DOMAIN}/client_keys/1234
```
