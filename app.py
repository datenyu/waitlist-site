from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    
    # Load or create the Excel file
    file_name = 'waitlist.xlsx'
    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Email'])
    
    # Append the new email to the DataFrame
    df = df.append({'Email': email}, ignore_index=True)
    
    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_name, index=False)
    
    return "Thank you for joining the waitlist!"

if __name__ == '__main__':
    app.run(debug=True)