
# Elasticsearch

## Password check

```bash
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
```

## SSL check
```bash
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic:$ElasticPW https://localhost:9200
```

---

# Kibana

## Token create

```bash
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTkyLjE2OC4xNTAuMzo5MjAwIl0sImZnciI6ImYxM2Y3ZGU2ZjExNzAxMDIzZWYzYWY3MjRkNmIzNWM2YTA1Mzc3ODlkNjNjNTUzMzhlNDE3YmM1ZmE3YmUwMzEiLCJrZXkiOiJQa29aVWFBQk55MDg2bVNXdHJzaDpJOHZlclphdXRRTHl6UWVQVWpBOWFnIn0=
```

## Setup

```bash
/usr/share/kibana/bin/kibana-setup
```

![[Pasted image 20260830142155.png]]

## Login

elasticのパスワードでログイン
---
# Fleet

```bash
/usr/share/kibana/bin/kibana-encryption-keys generate
```

```
xpack.encryptedSavedObjects.encryptionKey: b69ebb036e371e1870ff2045c852c5286699a8ed6ca065cd3a19bee679ce9656
xpack.reporting.encryptionKey: 9a03cca4f2497d13240b13d14d113546e3a03492776cc0f1e46b004e1b0f7b8c
xpack.security.encryptionKey: 5a412d112ebe01e3e16be6c7d243092ab3e1b630b5397aa8b9b4226847c9cf81
```

![[Pasted image 20260830150454.png]]

上記をkibana.ymlに追記

---

# Fleet

```powershell
PS C:\Program Files\Elastic\Agent> .\elastic-agent.exe enroll `
>>   --url=https://192.168.150.3:8220 `
>>   --enrollment-token=b0VwX1VhQUJOeTA4Nm1TVzJNNjI6bXJRbmxPeTNmay1aSUZoa0RVSnVLZw== --insecure
{"log.level":"warn","@timestamp":"2026-08-30T16:13:22.429+0900","log.logger":"tls","log.origin":{"function":"github.com/elastic/elastic-agent-libs/transport/tlscommon.(*TLSConfig).ToConfig","file.name":"tlscommon/tls_config.go","file.line":185},"message":"SSL/TLS verifications disabled.","ecs.version":"1.6.0"}
{"log.level":"info","@timestamp":"2026-08-30T16:13:22.457+0900","log.origin":{"function":"github.com/elastic/elastic-agent/internal/pkg/agent/application/enroll.EnrollWithBackoff","file.name":"enroll/enroll.go","file.line":87},"message":"Starting enrollment to URL: https://192.168.150.3:8220/","ecs.version":"1.6.0"}
{"log.level":"warn","@timestamp":"2026-08-30T16:13:22.677+0900","log.logger":"tls","log.origin":{"function":"github.com/elastic/elastic-agent-libs/transport/tlscommon.(*TLSConfig).ToConfig","file.name":"tlscommon/tls_config.go","file.line":185},"message":"SSL/TLS verifications disabled.","ecs.version":"1.6.0"}
{"log.level":"info","@timestamp":"2026-08-30T16:13:23.712+0900","log.origin":{"function":"github.com/elastic/elastic-agent/internal/pkg/agent/cmd.(*enrollCmd).daemonReloadWithBackoff","file.name":"cmd/enroll_cmd.go","file.line":417},"message":"Restarting agent daemon, attempt 0","ecs.version":"1.6.0"}
{"log.level":"info","@timestamp":"2026-08-30T16:13:23.728+0900","log.origin":{"function":"github.com/elastic/elastic-agent/internal/pkg/agent/cmd.(*enrollCmd).Execute","file.name":"cmd/enroll_cmd.go","file.line":206},"message":"Successfully triggered restart on running Elastic Agent.","ecs.version":"1.6.0"}
Successfully enrolled the Elastic Agent.
```


