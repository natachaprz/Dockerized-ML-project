import requests
import streamlit as st


st.title("Iris prediction")


sepal_length = st.text_input("Sepal Length", "Type Here")
sepal_width = st.text_input("Sepal Width", "Type Here")
petal_length = st.text_input("Petal Length", "Type Here")
petal_width = st.text_input("Petal Width", "Type Here")


if st.button("Predict"):
	url = "http://server:8000"

	data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width" : petal_width
    }
		
	try :
		response = requests.post(f"{url}/predict", json=data)
		if response.status_code == 200:
			hasil = response.json()
			st.success('The output is {}'.format(hasil['iris_type']))
			st.balloons()
		else:
			st.error("Error:", response.status_code, response.json())
	except requests.exceptions.RequestException as e:
    		st.error(f"Error: {e}")