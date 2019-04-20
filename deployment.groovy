node('master'){
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "ci/jenkins/scripts/deploy-stack.groovy"
          DeployCloudFormation.Deploy()
      }
    }
