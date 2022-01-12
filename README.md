# LiftPose App - Receive alerts to correct lifting posture
This app uses pose estimation to help users correct their posture while bending over and lifting items. The alert is a printed message with specific suggestions for correcting posture. A **scale** variable is used to adjust the keypoints measurements for different individuals, accounting for greater or smaller natural distances between keypoints used to detect poor posture.

## Requirements
* [alwaysAI account](https://alwaysai.co/auth?register=true)
* [alwaysAI Development Tools](https://alwaysai.co/docs/get_started/development_computer_setup.html)

## Usage
Once the alwaysAI tools are installed on your development machine (or edge device if developing directly on it) you can install and run the app with the following CLI commands:

Create empty directory for app and cd to it
```
mkdir AppDir1
cd AppDir1
```

To perform initial configuration of the app:
```
aai app configure
```

Follow the prompts:
---
Choose: Create new project

Enter Project Name: **LiftPoseApp1**

How would you like to initialize your project? **From Git Repo**

Enter: https://github.com/alwaysai/LiftPose.git

What is the destination: **Your local computer**

Install the app
---
```
aai app install
```

Start the app:
```
aai app start
```

## Disclaimer
This app is not mean to diagnose or treat any disease. The posture recommended by this app is what the creator has found best for him. This app mostly serves as a template that one can modify to suit their needs.

## Support
* [Documentation](https://alwaysai.co/docs/)
* [Community Discord](https://discord.gg/z3t9pea)
* Email: support@alwaysai.co
