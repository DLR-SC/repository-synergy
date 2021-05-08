# Fritz AI Models

A collection of machine and deep learning models designed to run on mobile devices.

Models in this repository contain code and utilities for training models as well as converting them to mobile-friendly formats like Core ML, TensorFlow Mobile, and TensorFlow Lite.

## Fritz AI

Fritz AI helps you teach your applications how to see, hear, feel, think, and sense. Create ML-powered features in your mobile apps for both Android and iOS. Start with our ready-to-use feature APIs or connect and deploy your own custom models.

[Sign up](https://app.fritz.ai/register?utm_source=github&utm_campaign=fritz-models) for an account on Fritz AI in order to get started with machine learning in your apps.

## Models

- [Image Labeling](image_labeling/): Label images based on their content.
- [Object Detection](object_detection/): Localize and label objects in an image with a bounding box.
- [Style Transfer](style_transfer/): Transform images into works of art by transfering the style of one image onto the content of another.
- [Image Segmentation](image_segmentation/): Semantic segmentation of images. Assign a value to each pixel of an image corresponding to the type of object it belongs to.
- [Create ML Playgrounds](create_ml_playgrounds/): A series of playgrounds for training models with Apple's Create ML tool

Don't see the model you're looking for? Open an issue and let us know!

## Add to your app

To see live demonstrations of these models running on-device, the Heartbeat App is available in both the [App Store](https://itunes.apple.com/us/app/heartbeat-by-fritz/id1325206416?mt=8) ([source code](https://github.com/fritzlabs/heartbeat-ios)) and [Play Store](https://play.google.com/store/apps/details?id=ai.fritz.heartbeat) ([source code](https://github.com/fritzlabs/heartbeat-android)).

If you'd like to incorporate any of these models or versions you've trained into your own app, head over to [Fritz](https://fritz.ai/?utm_source=github&utm_campaign=fritz-models). SDKs are available for both iOS and Android.

## Additional resources

Additional, [non-code resources](resources/README.md) for machine learning and AI.

- [Mobile ML GitHub Repositories](resources/mobile_ml_github_repositories.md): A list of repos with machine learning models ready for mobile, organized by feature type.
- [AI and ML Landscape](resources/AI_Landscape.md): Our curated list of helpful products and services for AI and machine learning.
- [AI and ML Newsletters](resources/AI_ML_Newsletters.md): A list of relevant newsletters in AI and machine learning.
- [Mobile Development Newsletters](resources/Mobile_Newsletters.md): A list of relevant newsletters in iOS, Android, React Native, and Cross Platform development.
- [Data Science Newsletters](resources/Data_Science_Newsletters.md): A list of relevant data science and data analytics newsletters.
- [Facebook Groups for AI/ML, Mobile, and Data Science](resources/AI_ML_Mobile_Facebook_Groups.md): A list of AI/ML, mobile dev, and data science Facebook communities.

## A note about large files

Large files like model checkpoints, data, and archives of compiled code are managed via `git lfs`. You need to have Git LFS installed in order to download these files. Installation instructions are available [here](https://github.com/git-lfs/git-lfs#getting-started).

If you have Git LFS installed, large files will download automatically by default. This can take a while and require a good connection. To clone this repository without downloading the model checkpoints, you can run:

```
GIT_LFS_SKIP_SMUDGE=1 git clone ...
```

## Stay in touch with Fritz AI

To keep tabs on what we’re up to, and for an inside look at the opportunities, challenges, and tools for mobile machine learning, subscribe to the [Fritz AI Newsletter](https://www.fritz.ai/newsletter?utm_campaign=fritz-models&utm_source=github).

## Join the community

[Heartbeat](https://heartbeat.fritz.ai/?utm_source=github&utm_campaign=fritz-models) is a community of developers interested in the intersection of mobile and machine learning. [Chat with us in Slack](https://fritz.ai/slack?utm_source=github&utm_campaign=fritz-models), and stay up to date on industry news, trends, and more by subscribing to [Deep Learning Weekly](https://www.deeplearningweekly.com/?utm_campaign=fritz-models&utm_source=github).

## Help

For any questions or issues, you can:

- Submit an issue on this repo
- Go to our [Help Center](https://docs.fritz.ai/help-center/index.html?utm_source=github&utm_campaign=fritz-models)
- Message us directly in [Slack](https://fritz.ai/slack?utm_source=github&utm_campaign=fritz-models)
