---
layout: page
title: Kubectl Command Reference
permalink: /infrastructure/kubectl-command-reference/
---
# Kubectl Command Reference

## Configuration

### Context
```bash
# sets current context to monitoring namespace for subsequent commands
$ kubectl config set-context --current --namespace=monitoring

# lists pods in the monitoring namespace without -n flag
$ kubectl get pods
```

### Logs

```bash
#  prints fluent-bit-jc2gn logs to stdout
$  kubectl logs fluent-bit-jc2gn -- /bin/sh

#  streams logs from pod fluent-bit-jc2gn to stdout
$  kubectl logs -f fluent-bit-jc2gn -- /bin/sh
```

## Resources

### List

```bash
# list cluster resources
$  kubectl get pods -A # get pods in all namespaces
$  kubectl get configmap -n logging # get configmaps in logging namespace
$  kubectl get daemonset -o yaml # get daemonsets and render to stdout as yaml
$  kubectl get deployment redis -o json # get redis daemonset and render as json
$  kubectl get deployment redis -o json # get redis daemonset and render as json

# list with short aliases
$  kubectl get po -A # get pods in all namespaces
$  kubectl get cm -n logging # get configmaps in logging namespace
$  kubectl get ds -o yaml # get daemonsets and render to stdout as yaml

# list pods belonging to node across all namespaces
$  kubectl get po --field-selector spec.nodeName=ip-10-1-9-313.ec2.internal -A
```

### Detail

```bash
$  kubectl describe po -n monitoring # details pods in the monitoring namespace
```

### Editing

```bash
# opens fluent configmap in editor
$  kubectl edit cm fluent-bit

# copies to local file and updates with changes
$  kubectl edit cm fluent-bit -o > fb-cm.yaml
$  kubectl apply -f fb-cm.yaml # -f specifies filename
```

### Deleting
```bash
# deletes pods with in logging namespace with label fluent-bit
$ kubectl delete po -n logging -l app.kubernetes.io/name=fluent-bit
```

## Pods

### Shell Access

```bash
#  executes agent status command on datadog container
$  kubectl exec datadog-j2n1f -- /bin/sh -c "agent status"

#  raw terminal mode; sends stdin to sh
$  kubectl exec -it datadog-j2n1f -- /bin/sh

#  specifies container integration-install for shell access
$  kubectl exec -it datadog-x1ch8 -c integration-install  -- /bin/sh
```

### Full Resource Alias List

| Short name |	Full name |
| ---------- | ---------- |
| csr | certificatesigningrequests |
| cs | componentstatuses |
| cm | configmaps |
| ds | daemonsets |
| deploy | deployments |
| ep | endpoints |
| ev | events |
| hpa | horizontalpodautoscalers |
| ing | ingresses |
| limits | limitranges |
| ns | namespaces |
| no | nodes |
| pvc | persistentvolumeclaims |
| pv | persistentvolumes |
| po | pods |
| pdb | poddisruptionbudgets |
| psp | podsecuritypolicies |
| rs | replicasets |
| rc | replicationcontrollers |
| quota | resourcequotas |
| sa | serviceaccounts |
| sc | storageclass |
| svc | services |

### References 📚
- [Kubectl Quick Reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/)
- [Kubectl Commands](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)
