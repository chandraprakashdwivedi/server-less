node('master'){
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "ci/jenkins/script/deploy-stack.groovy"
          DeployCloudFormation.Deploy()
      }
    }
