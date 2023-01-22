import subprocess

from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://docs.google.com/uc?export=download&id=1Fs-nbS80U-RJESe6huLmyGpdzoj8kAZY', 'colab.ipynb', quiet=False)
    process = subprocess.Popen(['ipython', '-c','"%run colab.ipynb"'], stdout=subprocess.PIPE)
    output, error = process.communicate()
    return jsonify(message=output.decode())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)