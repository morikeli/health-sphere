# Health-sphere

## Overview

![Screenshot from 2024-01-29 15-28-51](https://github.com/morikeli/health-sphere/assets/78599959/0670de40-9b80-4407-b1bd-89b4afb1f8bc)

Health-sphere is a web app that allows a user (medical staff, e.g. doctors, nurse) to enter diagnostic data that can diagnose whether a patient has the following diseases:
- Breast cancer
- Heart disease
- Diabetes
- Parkinson's disease

The models used have an accuracy of 100% ± 2.

### User instructions
1. You can access the website by clicking this [link](https://health-sphere.streamlit.app/).
2. Select the tab you want to input data.
3. Enter numerical data in the input fields provided and submit form.
4. Wait for response as the models diagnose the data input.
5. Once diagnosis is through, a message will be displayed of the current diagnosis.

### Developer instructions
```bash
   $ cd Desktop
   $ git clone https:github.com/morikeli/health-sphere/
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install -r requirements.txt
```
- Once installtion is complete, open type the following command to open the folder on your default browser.

   ```bash
      $ streamlit run app.py
   ```

### Bug reports
Incase of an error or bug create an issue using the `Issues` tab or create a new branch using Git and make a pull request.

- Don't forget to star the repo. 😉
