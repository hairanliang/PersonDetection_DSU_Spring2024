
# Person Detection with YOLOv8









## Overview

Ever wanted to build a model that could detect you or your friends within an image, video, or real-time camera input? I led a team of 5 within the Data Science Union at UCLA in building out such a model that uniquely detects each of us, as well as a [Streamlit app](https://dsu-object-detection.streamlit.app/app). 

![Screenshot 2024-05-22 at 9 20 03 AM](https://github.com/user-attachments/assets/901759b1-4893-4e28-8d4b-ae30f38e21ea)

*Above: Some fails and successes of our model on a portion of our testing set. It sometimes fails to recognize someone is in the picture or misidentifies them——more on this later*

This repository will serve as a description of our project but also a demo/guide if you want to build a similar project, whether it is detecting your friends or anything else. Let's get started!

## Dataset and Labels

We used [CVAT](https://www.cvat.ai/) to upload photos of ourselves and label them. After manually labelling our bounding boxes, CVAT also provided us with the box coordinates and labels, that we could later use as input to the model we used for training, YOLOv8 from [UltraLytics](https://github.com/ultralytics/ultralytics). 

## Model 

We used the YOLOv8 architecture, which is state-of-the-art for many computer vision tasks, including object detection. However, in the past, YOLOv8 has not been used for unique person detection, so we decided to see if we could reasonably train a YOLO model using lots of labeled data of each of us.

We experimented with Ultralytic's various pretrained models, and we found the YOLOv8s to be the best when considering accuracy and ability for real-time detection. 

## Training

Our training dataset comprised roughly 75 images of 7 people, along with 25 images of the same 7 people for validation/test. This amounted to a training set of roughly 700 images. Our final model was trained on all 700 images.

We trained on Google Colab, making use of the T4 GPU to speed up training. Ultralytics handled plotting of loss curves and some other cool plots that helped us understand how our model was training. 

The following confusion matrix showed us who the model struggled with and succeeded with. For instance, I was routinely confused with my friend Justin, whereas the model was confidently correct for detecting Parth.

![confusion_matrix_normalized](https://github.com/user-attachments/assets/cce932e7-f05f-49c8-9627-6f6226087bab)

In the figure below, the top right diagram was fascinating: it showed the distribution of bounding boxes for each of us. As can be seen, Parth, the bright green boxes, are generally the biggest ones, which confirms that Parth had many selfies within the dataset. We found that when testing the model, whenever we stood too close to the webcam, it would likely predict us to be Parth.

![labels](https://github.com/user-attachments/assets/a75607fc-0234-451a-b477-eefb40d48895)

Lastly, here are some training/validation loss graphs along with mean average precision, in which the model ends up getting 0.51. YOLOv8 is trained with multiple loss terms, including the classification loss (is the person in the box actually predicted correctly?) and the box loss (how well does the box bound the person?). We can see that during training, the model's training loss is still decreasing at the end of training, but the validation loss is plateauing, so we felt it was a good place to stop training.

![results](https://github.com/user-attachments/assets/3a68da6d-2b9b-4a20-8053-be78930599c1)








## Conclusion and Future Direction

This was one of my first times using external libraries like UltraLytics, and it was fun seeing how I could build an end-to-end project within 10 weeks by making use of amazing machine learning resources. 

My team and I found that while YOLOv8 did a decent job of detecting us sometimes, it struggled a lot in various cases, like when there were large groups of people in the picture or if it was a back or side-profile of us instead of front-on. In the end, we realized it all comes back down to the model's data——data quality is so important! So often we focus on searching for ideal hyperparameters or choosing the perfect model, but we neglect our data, which is the backbone of the entire process. 

For object detection in particular, it's important that there is enough data, and it's likely that our 700 photos was not enough for the model to confidently detect us. In the future, if we had unlimited time, we would have used 10,000 photos or more.

Lastly, YOLOv8 may not be the best architecture for differentating complex features like human faces and bodies, which can vary wildly from fashion choices and different poses. We hypothesize that a model with YOLOv8 as the backbone to perform the detection, and a specialized model responsible for classifying faces would work even better for our problem, and highly encourage anyone to try such an architecture out and let us know how it goes :) 

## Acknowledgements

Thank you to my amazing team members, Terry, Chelsea, Parth, Isaac, and Emily for helping create such a fun project. Also, thank you to the Data Science Union for providing such an amazing learning environment to learn and grow.

The following were integral resources that helped me learn about YOLO and can help you create an object detection project of your own.

 - [YOLO v3 Explanation Video](https://www.youtube.com/watch?v=vRqSO6RsptU&ab_channel=%D0%92%D0%B0%D0%BB%D0%B5%D0%BD%D1%82%D0%B8%D0%BD%D0%A1%D0%B8%D1%87%D0%BA%D0%B0%D1%80)
 - [Original YOLO paper](https://arxiv.org/abs/1506.02640)
 - [Amazing Resource on End-to-End Object Detection Project](https://www.youtube.com/watch?v=m9fH9OWn8YM&t=2861s&ab_channel=Computervisionengineer)



## Appendix

In case you were interested in seeing the presentation our team gave to the rest of the Data Science Union about this project, here is a [link](https://docs.google.com/presentation/d/1V6c1hgeQ_YZdw_v9RJhdqv4A2rU4jl6nGjs9W0B9lj4/edit?usp=sharing)


