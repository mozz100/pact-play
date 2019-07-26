Start server on port 1234 with:

```
python -m http.server 1234 &
```

Verify server with:

```
pact-verifier --provider-base-url=http://localhost:1234 --pact-url=../consumer/myconsumer-myprovider.json
```
