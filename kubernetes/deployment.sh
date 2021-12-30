cd ~/nginx/
sh lb-deployment.sh
cd ~/kubernetes/

kubectl apply -f configMap.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
kubectl apply -f nodePort.yaml