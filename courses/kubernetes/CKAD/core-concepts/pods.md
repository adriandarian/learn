# PODs

1. How many pods exist on the system? In the current(default) namespace.

```shell
$ kubectl get pods
No resources found in default namespace.
```

2. Create a new pod using the nginx image.

```shell
$ kubectl run nginx --image=nginx
pod/nginx created
```

3. How many pods are created now?

```shell
$ kubectl get pods
NAME            READY   STATUS    RESTARTS   AGE
newpods-kkbgc   1/1     Running   0          2m16s
newpods-pnpb9   1/1     Running   0          2m16s
newpods-tvblg   1/1     Running   0          2m16s
nginx           1/1     Running   0          50s
```

4. Which image is specified for the pods whose names begin with the newpods- prefix?

```shell
$ kubectl describe pod newpod-kkbgc
Name:             newpods-kkbgc
Namespace:        default
Priority:         0
Service Account:  default
Node:             controlplane/192.168.142.242
Start Time:       Thu, 17 Jul 2025 02:45:50 +0000
Labels:           tier=busybox
Annotations:      <none>
Status:           Running
IP:               10.22.0.10
IPs:
  IP:           10.22.0.10
Controlled By:  ReplicaSet/newpods
Containers:
  busybox:
    Container ID:  containerd://54215f6af8afedad5cc622ccb3d166d5e2555374b6c6aff743e9386faadbbbff
    Image:         busybox
    Image ID:      docker.io/library/busybox@sha256:f85340bf132ae937d2c2a763b8335c9bab35d6e8293f70f606b9c6178d84f42b
    Port:          <none>
    Host Port:     <none>
    Command:
      sleep
      1000
    State:          Running
      Started:      Thu, 17 Jul 2025 02:45:51 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6nhz6 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-6nhz6:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  3m48s  default-scheduler  Successfully assigned default/newpods-kkbgc to controlplane
  Normal  Pulling    3m48s  kubelet            Pulling image "busybox"
  Normal  Pulled     3m47s  kubelet            Successfully pulled image "busybox" in 255ms (255ms including waiting). Image size: 2156518 bytes.
  Normal  Created    3m47s  kubelet            Created container: busybox
  Normal  Started    3m47s  kubelet            Started container busybox
```

5. Which nodes are these pods placed on?

```shell
$ kubectl get pods -o wide
NAME            READY   STATUS    RESTARTS   AGE     IP           NODE           NOMINATED NODE   READINESS GATES
newpods-4cr65   1/1     Running   0          2m34s   10.22.0.9    controlplane   <none>           <none>
newpods-dsmsf   1/1     Running   0          2m34s   10.22.0.10   controlplane   <none>           <none>
newpods-qvqgt   1/1     Running   0          2m34s   10.22.0.11   controlplane   <none>           <none>
nginx           1/1     Running   0          2m17s   10.22.0.12   controlplane   <none>           <none>
```

6. We just created a new pod named webapp. How many containers are part of the webapp pod?

```shell
$ kubectl describe pod webapp
Name:             webapp
Namespace:        default
Priority:         0
Service Account:  default
Node:             controlplane/192.168.142.221
Start Time:       Thu, 17 Jul 2025 02:57:29 +0000
Labels:           <none>
Annotations:      <none>
Status:           Pending
IP:               10.22.0.13
IPs:
  IP:  10.22.0.13
Containers:
  nginx:
    Container ID:   containerd://51e8a7b26bb4f245f5ed592424acab812f268fce8b6a4c5b6660191e140ee4cc
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:f5c017fb33c6db484545793ffb67db51cdd7daebee472104612f73a85063f889
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Thu, 17 Jul 2025 02:57:30 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jtk2j (ro)
  agentx:
    Container ID:   
    Image:          agentx
    Image ID:       
    Port:           <none>
    Host Port:      <none>
    State:          Waiting
      Reason:       ErrImagePull
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jtk2j (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-jtk2j:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  55s                default-scheduler  Successfully assigned default/webapp to controlplane
  Normal   Pulling    55s                kubelet            Pulling image "nginx"
  Normal   Pulled     55s                kubelet            Successfully pulled image "nginx" in 151ms (151ms including waiting). Image size: 72223778 bytes.
  Normal   Created    55s                kubelet            Created container: nginx
  Normal   Started    55s                kubelet            Started container nginx
  Normal   Pulling    14s (x3 over 55s)  kubelet            Pulling image "agentx"
  Warning  Failed     14s (x3 over 54s)  kubelet            Failed to pull image "agentx": failed to pull and unpack image "docker.io/library/agentx:latest": failed to resolve reference "docker.io/library/agentx:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  Warning  Failed     14s (x3 over 54s)  kubelet            Error: ErrImagePull
  Normal   BackOff    3s (x3 over 53s)   kubelet            Back-off pulling image "agentx"
  Warning  Failed     3s (x3 over 53s)   kubelet            Error: ImagePullBackOff
```

7. What images are used in the new webapp pod?

```shell
$ kubectl describe pod webapp | grep "Image:"
    Image:          nginx
    Image:          agentx
```

8. What is the state of the container agentx in the pod webapp? Wait for it to finish the ContainerCreating state

```shell
$ kubectl describe pod webapp
Name:             webapp
Namespace:        default
Priority:         0
Service Account:  default
Node:             controlplane/192.168.142.221
Start Time:       Thu, 17 Jul 2025 02:57:29 +0000
Labels:           <none>
Annotations:      <none>
Status:           Pending
IP:               10.22.0.13
IPs:
  IP:  10.22.0.13
Containers:
  nginx:
    Container ID:   containerd://51e8a7b26bb4f245f5ed592424acab812f268fce8b6a4c5b6660191e140ee4cc
    Image:          nginx
    Image ID:       docker.io/library/nginx@sha256:f5c017fb33c6db484545793ffb67db51cdd7daebee472104612f73a85063f889
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Thu, 17 Jul 2025 02:57:30 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jtk2j (ro)
  agentx:
    Container ID:   
    Image:          agentx
    Image ID:       
    Port:           <none>
    Host Port:      <none>
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-jtk2j (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-jtk2j:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                  From               Message
  ----     ------     ----                 ----               -------
  Normal   Scheduled  3m51s                default-scheduler  Successfully assigned default/webapp to controlplane
  Normal   Pulling    3m51s                kubelet            Pulling image "nginx"
  Normal   Pulled     3m51s                kubelet            Successfully pulled image "nginx" in 151ms (151ms including waiting). Image size: 72223778 bytes.
  Normal   Created    3m51s                kubelet            Created container: nginx
  Normal   Started    3m51s                kubelet            Started container nginx
  Normal   Pulling    56s (x5 over 3m51s)  kubelet            Pulling image "agentx"
  Warning  Failed     56s (x5 over 3m50s)  kubelet            Failed to pull image "agentx": failed to pull and unpack image "docker.io/library/agentx:latest": failed to resolve reference "docker.io/library/agentx:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  Warning  Failed     56s (x5 over 3m50s)  kubelet            Error: ErrImagePull
  Normal   BackOff    1s (x14 over 3m49s)  kubelet            Back-off pulling image "agentx"
  Warning  Failed     1s (x14 over 3m49s)  kubelet            Error: ImagePullBackOff
```

9. Why do you think the container agentx in pod webapp is in error?

```shell
Events:
  Type     Reason     Age                 From               Message
  ----     ------     ----                ----               -------
  Normal   Scheduled  16m                 default-scheduler  Successfully assigned default/webapp to controlplane
  Normal   Pulling    16m                 kubelet            Pulling image "nginx"
  Normal   Pulled     16m                 kubelet            Successfully pulled image "nginx" in 151ms (151ms including waiting). Image size: 72223778 bytes.
  Normal   Created    16m                 kubelet            Created container: nginx
  Normal   Started    16m                 kubelet            Started container nginx
  Normal   Pulling    13m (x5 over 16m)   kubelet            Pulling image "agentx"
  Warning  Failed     13m (x5 over 16m)   kubelet            Failed to pull image "agentx": failed to pull and unpack image "docker.io/library/agentx:latest": failed to resolve reference "docker.io/library/agentx:latest": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  Warning  Failed     13m (x5 over 16m)   kubelet            Error: ErrImagePull
  Normal   BackOff    71s (x63 over 16m)  kubelet            Back-off pulling image "agentx"
  Warning  Failed     71s (x63 over 16m)  kubelet            Error: ImagePullBackOff
```

10. What does the READY column in the output of the kubectl get pods command indicate?

```shell
$ kubectl get pods
NAME            READY   STATUS             RESTARTS       AGE
newpods-4cr65   1/1     Running            1 (8m3s ago)   24m
newpods-dsmsf   1/1     Running            1 (8m3s ago)   24m
newpods-qvqgt   1/1     Running            1 (8m3s ago)   24m
nginx           1/1     Running            0              24m
webapp          1/2     ImagePullBackOff   0              20m
```

11. Delete the webapp Pod.

```shell
$ kubectl delete pod webapp
pod "webapp" deleted
```

12. Create a new pod with the name redis and the image redis123.

```shell
$ kubectl run redis --image=redis123
pod/redis created
```

13. Now change the image on this pod to redis.

```shell
$ kubectl edit pod redis
pod/redis edited
```
