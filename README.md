# 🌿 CropCareAI: Plant Disease Recognition System

<div align="center">

![CropCareAI Banner](home_page.jpg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17.0-orange)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

## 📋 Overview

CropCareAI is an advanced plant disease recognition system that leverages deep learning to identify various plant diseases from images. This tool helps farmers, gardeners, and agricultural professionals quickly detect and address plant health issues, contributing to better crop management and yield optimization.

## ✨ Features

<details>
<summary>🔍 Click to expand features</summary>

### Core Features

```mermaid
graph TD
    A[CropCareAI] --> B[Image Analysis]
    A --> C[Disease Detection]
    A --> D[Treatment Recommendations]
    B --> E[Real-time Processing]
    C --> F[38 Disease Classes]
    D --> G[Detailed Reports]
```

### Supported Plants and Diseases

```mermaid
mindmap
  root((CropCareAI))
    Apple
      Apple Scab
      Black Rot
      Cedar Apple Rust
      Healthy
    Blueberry
      Healthy
    Cherry
      Powdery Mildew
      Healthy
    Corn
      Cercospora Leaf Spot
      Common Rust
      Northern Leaf Blight
      Healthy
    Grape
      Black Rot
      Esca
      Leaf Blight
      Healthy
    Orange
      Citrus Greening
    Peach
      Bacterial Spot
      Healthy
    Pepper
      Bacterial Spot
      Healthy
    Potato
      Early Blight
      Late Blight
      Healthy
    Raspberry
      Healthy
    Soybean
      Healthy
    Squash
      Powdery Mildew
    Strawberry
      Leaf Scorch
      Healthy
    Tomato
      Bacterial Spot
      Early Blight
      Late Blight
      Leaf Mold
      Septoria Leaf Spot
      Spider Mites
      Target Spot
      Yellow Leaf Curl Virus
      Mosaic Virus
      Healthy
```

</details>

## 🚀 Getting Started

### Prerequisites

```mermaid
graph LR
    subgraph System Requirements
        A[Python 3.8+] --> D[Application]
        B[pip Latest] --> D
        C[8GB+ RAM] --> D
        E[1GB+ Storage] --> D
    end
```

### Installation

```mermaid
graph LR
    A[Clone Repo] --> B[Install Dependencies]
    B --> C[Run Application]
    C --> D[Start Analysis]
```

1. Clone the repository:

```bash
git clone https://github.com/RajaMahanty/crop-care-ai.git
cd crop-care-ai
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run main.py
```

## 🎯 Usage

```mermaid
sequenceDiagram
    participant U as User
    participant A as App
    participant M as Model

    U->>A: Upload Image
    A->>M: Process Image
    M->>A: Return Prediction
    A->>U: Show Results & Treatment
```

### Application Flow

1. Launch the application
2. Navigate to "Disease Recognition" in the sidebar
3. Upload a plant leaf image
4. Click "Show Image" to preview
5. Click "Predict" to analyze
6. View results including:
   - Disease identification
   - Disease information
   - Recommended treatment options

## 📊 Model Details

### Model Architecture

```mermaid
graph TD
    A[Input Image<br>128x128 pixels] --> B[Preprocessing]
    B --> C[ResNet50V2 Base]
    C --> D[Global Average Pooling]
    D --> E[Dense 512 + ReLU]
    E --> F[Dropout 0.5]
    F --> G[Dense 38 + Softmax]
```

### Model Performance

The model was trained for 6 epochs and achieved excellent performance metrics:

- Overall Accuracy: 96%
- Training Accuracy: 97.06%
- Validation Accuracy: 95.94%

#### Detailed Performance Metrics

The model shows strong performance across all 38 classes with:

- Average Precision: 96%
- Average Recall: 96%
- Average F1-Score: 96%

Notable class-wise performance:

- High accuracy (>98%) for most healthy plant classes
- Strong performance for common diseases like:
  - Apple Scab (96% F1-score)
  - Grape Black Rot (96% F1-score)
  - Tomato Yellow Leaf Curl Virus (98% F1-score)
  - Potato Early Blight (95% F1-score)

### Training Process

- Training Set: 70,295 images
- Validation Set: 17,572 images
- Image Size: 128x128 pixels
- Color Mode: RGB
- Batch Size: 32
- Optimizer: Adam (learning_rate=0.001)
- Loss Function: Categorical Crossentropy
- Early Stopping: Patience=5, monitor='val_loss'
- Model Checkpoint: Save best model based on validation accuracy

The model shows consistent improvement across epochs with minimal overfitting, as evidenced by the close training and validation accuracy curves.

## 📚 Dataset Information

### Dataset Distribution

```mermaid
pie title Dataset Split
    "Training Set<br>70,295 Images<br>80%" : 70295
    "Validation Set<br>17,572 Images<br>20%" : 17572
    "Test Set<br>33 Images" : 33
```

### Dataset Overview

- Total Images: 87,900
- Training Set: 70,295 images (80%)
- Validation Set: 17,572 images (20%)
- Categories: 38 different classes
- Image Type: RGB images of healthy and diseased crop leaves
- Image Size: 128x128 pixels
- Data Augmentation: Random rotation, width/height shifts, shear, zoom, horizontal flip

## 🛠️ Technical Stack

```mermaid
graph TB
    subgraph Frontend
        A[Streamlit]
    end
    subgraph Backend
        B[Python]
    end
    subgraph Deep Learning
        C[TensorFlow/Keras]
    end
    subgraph Processing
        D[OpenCV]
        E[Pillow]
        F[NumPy]
    end
```

## 🔄 Future Enhancements

```mermaid
gantt
    title Future Development Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1
    Expand Dataset    :2024-03-01, 30d
    Real-time Detection :2024-04-01, 45d
    section Phase 2
    Mobile Integration :2024-05-15, 30d
    Additional Features :2024-06-15, 30d
```

## 🤝 Contributing

### Development Workflow

```mermaid
graph LR
    A[Fork Repo] --> B[Create Branch]
    B --> C[Make Changes]
    C --> D[Test Changes]
    D --> E[Create PR]
    E --> F[Review]
    F --> G[Merge]
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

```mermaid
graph LR
    A[CropCareAI] --> B[PlantVillage Dataset]
    A --> C[Streamlit]
    A --> D[TensorFlow]
    A --> E[Open Source Community]
```

## 📧 Contact

- GitHub Issues: Create an issue
- Repository: [crop-care-ai](https://github.com/RajaMahanty/crop-care-ai)

---

<div align="center">
Made with ❤️ for better agriculture
</div>
