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
          image: docker:latest
          command:
            - cat
          tty: true
          env:
            - name: DOCKER_HOST
              value: tcp://localhost:2375

        - name: dind
          image: docker:dind
          securityContext:
            privileged: true
          env:
            - name: DOCKER_TLS_CERTDIR
              value: ""
          volumeMounts:
            - name: docker-storage
              mountPath: /var/lib/docker

  volumes:
    - name: docker-storage
      emptyDir: {}
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
