# form8-example-joker
A simple example service configured to use form8, _joker_ consists of a single stateless component that serves jokes 
as text strings and a functional test that ensures the service is working as expected. Please see the form8.yaml file 
for details on how the service is tied together.

Doing a build/deploy(or update)/test of this service (as well as any service configured with a form8.yaml file) 
    is as easy as:
```bash
form8 build -t mytag --env myenv && \
form8 deploy -t mytag --env myenv && \
form8 test -t mytag --env myenv
```
or even simpler:
```bash
export FORM8_TAG=mytag
export FORM8_ENVIRONMENT=myenv
form8 build && form8 deploy && form8 test
```
Note that each form8 action exists with status 0 if it completes successfully.
