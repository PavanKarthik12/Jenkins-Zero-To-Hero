steps to install argo CD in a EC2 instance :

1) login to ec2 instance as ubuntu user and then switch to root user by giving below command

      sudo su -
2) Install docker as root user by following any documentation :

   sudo apt update
   sudo apt install docker.io

3) Grant acccess to ubuntu user for docker

     usermod -aG docker ubuntu

4) Switch again to root user for installing minikube and kubectl :

     curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
     sudo install minikube-linux-amd64 /usr/local/bin/minikube
     sudo snap install kubectl

5) switch to ubuntu user again and start minikube server
      minikube start --driver=docker

6) Now that docker kubectl minikube got installed now you can download argo cd from official documentation .4

     https://operatorhub.io/operator/argocd-operator


port forward - kubectl port-forward service/example-argocd-server --address 0.0.0.0 5000:80
