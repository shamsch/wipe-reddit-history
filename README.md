## ENVIRONMENT VARIABLE TO RUN GITHUB ACTIONS
Set up the following variable in GitHub repository secrets to run the GitHub Actions.
```bash
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
REDDIT_USERNAME
REDDIT_PASSWORD
REDDIT_APP_ID
REDDIT_APP_SECRET
BUCKET_NAME
```
## IAM POLICY NEEDED
```bash
AmazonEventBridgeFullAccess	
AmazonS3FullAccess	
AWSCloudFormationFullAccess	
AWSLambda_FullAccess	
IAMFullAccess
```