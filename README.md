# Evaluating Drone Detection Performance in Vision-Language Models

With the recent surge in Large Language Models (LLMs) over the past few years, it has become increasingly important to evaluate and understand what these models excel at and where they fall short. Their capabilities have expanded beyond traditional language tasks, extending into vision models and large multimodal models that combine both vision and language understanding.

There is still much room to explore the boundaries of where these models perform best, especially in more specific and complex tasks like drone detection. Likewise, it's crucial to identify the areas where they struggle, as understanding these limitations will be key to improving their performance and designing better models in the future.

In this project, we will use open-source Vision-Language Models (VLMs) to evaluate their performance in drone detection tasks, primarily using Qwen-VL, a Chinese model developed by Alibaba Cloud.

## Qwen-VL Models

Qwen-VL offers three main models:
- **Qwen-VL-2B (OS)**
- **Qwen-VL-7B (OS)**
- **Qwen-VL-72B (CS)**

## The Importance of Evaluating Multimodal Models in Drone Detection

Vision-Language Models represent a new frontier for applications requiring both image processing and language understanding. In the context of drone detection, these models could prove useful in scenarios where it is necessary not only to detect and classify drones from visual input but also to generate meaningful language-based descriptions or reports based on the detected objects.

Evaluating how well these models handle drone detection tasks is crucial for several reasons:
- **Security and Surveillance:** Drones are increasingly used for both legal and illegal activities. Detection of drones in restricted airspaces or high-security zones could help in preventing unauthorized surveillance or malicious activity.
- **Disaster Management:** Drones play a significant role in disaster relief and environmental monitoring. Accurate detection helps improve the efficiency of managing drone fleets and analyzing the data they collect.
- **Civilian Applications:** Drones are widely used in commercial sectors such as agriculture, film production, and package delivery. Accurate detection optimizes their safe use in civilian airspace.

## Challenges in Evaluating Drone Detection

Vision-Language Models, while powerful, face several challenges in the context of drone detection:
- **Small Object Detection:** Drones are typically small and can appear as tiny objects in wide-angle images or videos. Many vision models struggle with small object detection, which may impact their performance in drone surveillance tasks.

## Conclusion

After evaluating the performance of these models on a 400-image dataset, we can conclude the following:

Qwen-VL-7B results are impressive in classification tasks, achieving an accuracy of 81.5%, detecting 326 drones in 400 images. For detection tasks, the results vary depending on the IoU (Intersection over Union) threshold used. At the normal threshold of 0.5, the precision is low, at 0.23. However, using a 0.4 or 0.3 threshold shows some interesting results. Here are the full results:

| Threshold | TP  | FN  | LE  | Avg IoU | Precision | Recall  |
|-----------|-----|-----|-----|---------|-----------|---------|
| 0.1       | 261 | 74  | 65  | 0.3246  | 0.8006    | 0.7791  |
| 0.2       | 218 | 74  | 108 | 0.3246  | 0.6687    | 0.7466  |
| 0.3       | 167 | 74  | 159 | 0.3246  | 0.5123    | 0.6929  |
| 0.4       | 127 | 74  | 199 | 0.3246  | 0.3896    | 0.6318  |
| 0.5       | 77  | 74  | 249 | 0.3246  | 0.2362    | 0.5099  |
| 0.6       | 46  | 74  | 280 | 0.3246  | 0.1411    | 0.3833  |
| 0.7       | 19  | 74  | 307 | 0.3246  | 0.0583    | 0.2043  |
| 0.8       | 3   | 74  | 323 | 0.3246  | 0.0092    | 0.0390  |
| 0.9       | 0   | 74  | 326 | 0.3246  | 0.0000    | 0.0000  |