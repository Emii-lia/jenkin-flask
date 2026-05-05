pipeline {
	agent {
		kubernetes {
			label "jenkins-agent-app"
			yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    component: ci
spec:
  containers:
    - name: python
      image: python:latest
      command:
        - cat
      tty: true
    - name: docker
      image: docker
      command:
        - cat
      tty: true
      securityContext:
        privileged: true
      volumeMounts:
        - mountPath: /var/run/docker.sock
          name: docker-sock
  volumes:
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
"""
		}
	}
	triggers {
		pollSCM('* * * * *')
	}
	stages {
		stage("Test python") {
			steps {
				container("python") {
					sh "pip install -r requirements.txt"
					sh "python test.py"
				}
			}
		}
		stage('Build docker image') {
			steps {
			  container("docker") {
          sh "docker build -t localhost:4000/pythontest:latest ."
          sh "docker push localhost:4000/pythontest:latest"
			  }
			}
		}
	}
}
