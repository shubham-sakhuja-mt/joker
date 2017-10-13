# joker
A simple example service configured to use form8, _joker_ consists of:
- a stateless component that serves jokes over http
- a functional test that ensures it is working as expected
Please see the **form8.yaml** file for more details on how the above pieces are configured.

Doing a build/deploy(or update)/test of this service (as well as any service configured with a form8.yaml file) is as easy as:
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
Note that each form8 action exits with status 0 if it completes successfully.
