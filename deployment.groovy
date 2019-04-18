if(env.JOB_BASE_NAME == "master") {
    env.ROLE_NAME="jenkins/appslave-jenkins-cpdelivery"
    env.ENVIRONMENT="master"
    env.MASTER_REGION="us-east-1"
    env.ACCOUNT_NUMBER="815275185692"
    env.VPC_NAME = "aws-ghns-sharedservices-prod-useast1-vpn"
} else {
    env.ROLE_NAME="jenkins/appslave-jenkins-cpdelivery"
    env.ENVIRONMENT="development"
    env.MASTER_REGION="us-east-1"
    env.ACCOUNT_NUMBER="049723741716"
    env.VPC_NAME = "aws-ghns-sharedservices-devl-useast1-cp"
}

withAWS(role:"${ROLE_NAME}", roleAccount: "${ACCOUNT_NUMBER}"){
      stage('Deploy using serverless framework'){
          def DeployCloudFormation = load "ci/jenkins/scripts/deploy-stack.groovy"
          DeployCloudFormation.Deploy()
      }
    }
