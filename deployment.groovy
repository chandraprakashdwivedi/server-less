node('master'){
      checkout scm
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "$JENKINS_HOME/ci/jenkins/script/deploy-stack.groovy"
          DeployCloudFormation.Deploy()
      }
    }
