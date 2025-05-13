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

## 📊 Model Performance

### Accuracy Metrics

```mermaid
pie title Model Accuracy Distribution
    "Training" : 98.5
    "Validation" : 96.2
    "Test" : 95.8
```

### Performance Statistics

```mermaid
graph LR
    subgraph Model Metrics
        A[Training Accuracy<br>98.5%] --> D[Model]
        B[Validation Accuracy<br>96.2%] --> D
        C[Test Accuracy<br>95.8%] --> D
        E[Inference Time<br>0.8s] --> D
        F[Model Size<br>90MB] --> D
        G[Input Size<br>128x128] --> D
    end
```

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
        G[Pandas]
    end
    subgraph Visualization
        H[Matplotlib]
        I[Plotly]
    end
```

## 📚 Dataset Information

### Dataset Distribution

```mermaid
pie title Dataset Split
    "Training" : 70295
    "Validation" : 17572
    "Test" : 33
```

### Dataset Statistics

```mermaid
graph LR
    subgraph Dataset Overview
        A[Training<br>70,295 Images] --> D[Total: 87,900]
        B[Validation<br>17,572 Images] --> D
        C[Test<br>33 Images] --> D
        E[38 Disease Classes] --> D
        F[14 Plant Species] --> D
    end
```

## 🔄 Future Enhancements

```mermaid
gantt
    title Future Development Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1
    Video Analysis    :2024-03-01, 30d
    Mobile App       :2024-04-01, 45d
    section Phase 2
    Weather Integration :2024-05-15, 30d
    Multi-language    :2024-06-15, 30d
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
