node('master'){
      checkout scm
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "$JENKINS_HOME/jobs/server-less/workspace/ci/jenkins/script/deploy-stack.groovy"
          DeployCloudFormation.Deploy()
      }
    }
