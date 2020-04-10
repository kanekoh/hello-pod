# Hello Pod

## Build Application

```
$ git clone <this repo>
$ cd <the repo>
$ oc new-build hello --image-stream=python:3.5 --binary=true
$ oc start-build hello --from-dir=. -w
```

## Deploy Application

```
$ oc new-app hello
$ oc expose svc hello
```

## Access to the applicaiton

```
$ ROUTE=$(oc get route python -o jsonpath={.spec.host})
$ curl $ROUTE; echo ''
```
