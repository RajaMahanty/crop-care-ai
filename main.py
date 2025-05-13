import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_plant_disease_model.keras")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Disease Recognition"])

#Main Page
if app_mode == "Home":
    # st.set_page_config(layout="wide")
    
    # Header with custom styling
    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>PLANT DISEASE RECOGNITION SYSTEM</h1>", unsafe_allow_html=True)
    
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        image_path = "home_page.jpg"
        st.image(image_path, use_column_width=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #2E7D32;'>Welcome to the Plant Disease Recognition System</h2>
        <p style = 'color : black; '>Our advanced platform efficiently identifies plant diseases through image analysis, assisting agricultural professionals and enthusiasts in maintaining crop health and optimizing yields.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # System Workflow
    st.markdown("""
    <h3 style='color: #2E8B57;'>System Workflow</h3>
    <ol>
    <li><strong>Image Upload:</strong> Navigate to the <em>Disease Recognition</em> section to submit a high-resolution plant image.</li>
    <li><strong>Automated Analysis:</strong> Our algorithms process the image to detect potential disease indicators.</li>
    <li><strong>Comprehensive Results:</strong> Receive a detailed report with identified issues and recommended actions.</li>
    </ol>
    """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown("""
    <h3 style='color: #2E8B57;'>Key Features</h3>
    <ul>
    <li><strong>Precision:</strong> State-of-the-art machine learning models ensure high accuracy in disease detection.</li>
    <li><strong>Intuitive Interface:</strong> Streamlined design for effortless navigation and operation.</li>
    <li><strong>Rapid Processing:</strong> Obtain results within seconds for prompt decision-making.</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Call to Action
    st.markdown("""
    <div style='background-color: #30475E; padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 0 10px rgba(0,0,0,0.1);'>
    <h3 style='color: #4682B4;'>Ready to Start?</h3>
    <p>Select the <strong>Disease Recognition</strong> option in the sidebar to begin the analysis process and experience our advanced system capabilities.</p>
     </div>
    """, unsafe_allow_html=True)
    
    # Additional Information
    st.info("For more details about our project, team composition, and long-term objectives, please refer to the **About** section.")

#About Project
elif(app_mode=="About"):
    st.header("About")
    st.markdown("""
    ## About Our Project

    ### Dataset Overview
    - **Source**: Recreated using offline augmentation from the original dataset
    - **Original Repository**: Available on GitHub 
    - **Composition**: Approximately 87,000 RGB images of healthy and diseased crop leaves
    - **Categories**: 38 different classes
    - **Distribution**: 
        - Training set: 80% (70,295 images)
        - Validation set: 20% (17,572 images)
    - **Additional**: Test set of 33 images for prediction purposes

    ### Key Features
    - High-quality images for accurate disease recognition
    - Diverse range of plant species and disease types
    - Balanced dataset for robust model training

    ### Project Goals
    1. Develop an efficient plant disease recognition system
    2. Assist farmers and gardeners in early disease detection
    3. Contribute to sustainable agriculture practices

    ### Future Developments
    - Expand the dataset with more plant species
    - Implement real-time disease detection capabilities
    - Integrate with mobile applications for wider accessibility
    """)

#Prediction Page
elif app_mode == "Disease Recognition":
    st.header("Disease Recognition")
    test_image = st.file_uploader("Choose an Image:")
    if st.button("Show Image"):
        st.image(test_image, width=4, use_column_width=True)
    
    # Predict button
    if st.button("Predict"):
        if test_image is not None:
            st.snow()
            st.write("Our Prediction")
            result_index = model_prediction(test_image)
            
            # Reading Labels
            class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                        'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                        'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                        'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                        'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                        'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                        'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                        'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                        'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                        'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                        'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                        'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                        'Tomato___Target_Spot', 'Tomato___Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                        'Tomato___healthy']
            
            prediction = class_name[result_index]
            st.success(f"Model predicts: {prediction}")
            
            # Display additional information about the predicted disease
            st.subheader("Disease Information")
            disease_info = {
                'Apple___Apple_scab': 'Apple scab is a fungal disease that causes dark, scaly lesions on leaves and fruit.',
                'Apple___Black_rot': 'Black rot is a fungal disease causing dark circular lesions on leaves and rotting fruit.',
                'Apple___Cedar_apple_rust': 'Cedar apple rust creates orange spots on leaves and deformed fruit.',
                'Apple___healthy': 'This plant appears healthy with no visible disease symptoms.',
                # Add more disease descriptions as needed
            }.get(prediction, 'No information available for this disease.')
            st.write(disease_info)
            
            # Suggest treatment options
            st.subheader("Recommended Treatment")
            treatment_options = {
                'Apple___Apple_scab': 'Treatment options include: \n- Apply fungicides early in the growing season\n- Prune infected branches\n- Remove fallen leaves\n- Improve air circulation',
                'Apple___Black_rot': 'Treatment options include: \n- Remove infected fruit and cankers\n- Prune during dry weather\n- Apply fungicides\n- Maintain good sanitation',
                'Apple___Cedar_apple_rust': 'Treatment options include: \n- Remove nearby cedar trees if possible\n- Apply preventative fungicides\n- Plant resistant varieties\n- Prune affected areas',
                'Apple___healthy': 'No treatment needed. Continue good agricultural practices.',
                # Add more treatment options for other diseases
            }.get(prediction, 'No specific treatment information available for this disease.')
            st.write(treatment_options)
        else:
            st.warning("Please upload an image before predicting.")