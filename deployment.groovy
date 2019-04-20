node('master'){
      checkout scm
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "$JENKINS_HOME/jobs/${env.JOB_NAME}/workspace/ci/jenkins/script/*"
          //DeployCloudFormation.Deploy()
          DeployCloudFormation.Delete() //to delete stack
      }
    }
