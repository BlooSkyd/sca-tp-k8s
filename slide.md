todo : le faire en marp

python dockerfile :
https://docs.docker.com/guides/python/containerize/#overview


https://blog.stephane-robert.info/docs/conteneurs/orchestrateurs/kubernetes/horizontal-pod-scaling/

kubectl apply -f hpa-deployment.yaml
> deployment.apps/hpa-deployment created
kubectl apply -f .\hpa-service.yaml 
> service/hpa-service created
kubectl apply -f .\hpa.yaml           
> horizontalpodautoscaler.autoscaling/api-hpa created
kubectl get all 


minikube service hpa-service --url

kubectl get hpa
kubectl get pods -w

 curl http://localhost:52103/stress (attention au port)