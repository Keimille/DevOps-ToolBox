# Deploy Application with Codecommit and AWS CLI

- Create repository
``aws codecommit create-repository --repository-name <name>``

- Create git credentials for your user (I searched to see if there was a way to do this with CLI but it seems as if that is unavailable at the time)

- Clone your repository 
``git clone <url>``

- Add index.html file to repository
``git init``
``git add -A``
``git commit``


