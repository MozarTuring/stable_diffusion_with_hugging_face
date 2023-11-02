from diffusers import DiffusionPipeline
import os
from flask import Flask, request, jsonify, render_template
import json
#import Queue
import threading


lock = threading.Lock()


pipeline = DiffusionPipeline.from_pretrained("/home/maojingwei/project/pretrained_models/runwayml/stable-diffusion-v1-5")
pipeline.to("cuda")
#text = "a black dog"
#image = pipeline(text).images[0]
#print(type(image))
#image.save(os.path.join("static", text+".jpg"), quality=95)


app = Flask(__name__)
#q = Queue.Queue()
tmp_list = list()
@app.route("/index", methods=["GET", "POST"])
def main():
    met = request.method
    if met == "GET":
        return render_template('index.html')
    else:
        text = request.form.get("username")
        with lock:
            print("processing {}".format(text))
#            while len(q) > 0:
#                time.sleep(0.05)
            image = pipeline(text).images[0]
            print(type(image))
            image.save(os.path.join("static", text+".jpg"), quality=95)
            return render_template('index.html', data=json.dumps({"file_path":"static/"+text+".jpg"}, ensure_ascii=False))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=52746,
        debug=False,
    )


"""shell_start_mjw
set -e

source /home/maojingwei/project/stable_diffusion_with_hugging_face/myRequirements.sh run

python /home/maojingwei/project/stable_diffusion_with_hugging_face/flask_service.py
shell_end_mjw"""
