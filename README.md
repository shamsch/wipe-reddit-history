# 🚀 Wipe Reddit History 🗑️

A simple AWS Lambda function to help minimize your footprint on Reddit. Currently, it deletes all comments older than 72 hours with less than 1 karma and deletes comments aged between 3 and 5 days with a score less than 10 karma with 50% probability. 

### 💻 Environment Variables for Github Actions 📝

Set up the following variable in Github repository secrets to run the Github Actions. Make sure to replace 'value' with your actual details.

```bash
AWS_ACCESS_KEY_ID=value 
AWS_SECRET_ACCESS_KEY=value 
REDDIT_USERNAME=value 
REDDIT_PASSWORD=value 
REDDIT_APP_ID=value 
REDDIT_APP_SECRET=value 
BUCKET_NAME=value 
```
Get the Reddit app ID and secret from [here](https://www.reddit.com/prefs/apps). Create a new app if you don't have one. Add your username as the developer. The app type is script. The redirect URL can be anything.

### 🔐 GitHub Action Permissions 🛡️

The following permissions are necessary for the Github Actions to run correctly. Make sure the IAM user or role has these permissions:


> AmazonEventBridgeFullAccess
> 	
> AmazonS3FullAccess
> 
> AWSCloudFormationFullAccess
> 
> AWSLambda_FullAccess
> 
> IAMFullAccess

## 📋 TODO ✔️

- [ ] Send monthly log by email using SNS 📝
- [ ] Allow multi-account 🔐
- [ ] Delete posts. 📝
- [ ] Possibly a front-end of sort. 🖥️
- [ ] Add tests. 🧪
- [ ] Update the dependencies in requirements.txt 📦

This project is under active development. Contributions are welcome! 🤝
