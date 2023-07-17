# Wipe Reddit History
A simple AWS Lambda function to wipe Reddit history. Currently, it only delete 95% of the comments that are older than 72 hours have less 1 karma. This is a very specific use case for my personal preference which you should modify to your liking. The function is triggered every 12 hours by AWS EventBridge. Deployed by AWS CloudFormation through GitHub Actions by dispatching manually. 

### ENVIRONMENT VARIABLE TO RUN GITHUB ACTIONS
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
Get the Reddit app ID and secret from [here](https://www.reddit.com/prefs/apps). Create a new app if you don't have one. Add your username as the developer. The app type is script. The redirect URL can be anything.

### IAM POLICY NEEDED
Add the following IAM policy to the IAM user or role that will be used to run the GitHub Actions.
```bash
AmazonEventBridgeFullAccess	
AmazonS3FullAccess	
AWSCloudFormationFullAccess	
AWSLambda_FullAccess	
IAMFullAccess
```

## TODO
- [ ] Allow passing username and password as parameter to the Lambda function.
- [ ] More granular control over the deletion process.
- [ ] Delete posts.
- [ ] Create a simple web frontend to trigger the Lambda function.
- [ ] Add tests
- [ ] Update the dependencies in `requirements.txt`
