from flask import Flask
from flask_restful import Api,Resource,reqparse

app = Flask(__name__)
api = Api(app)
#class HelloWorld(Resource):
 #   def get(self):
 #       return{"data":" Hello World"}
#api.add_resource(HelloWorld,"/helloworld")  
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str,help="name")      
video_put_args.add_argument("views",type=int,help="views")      
video_put_args.add_argument("likes",type=int,help="likes")      
videos={"name":" Hello World"}
class Video(Resource):
    def get(self,video_id):
        return videos[video_id]
    def put(self,video_id):
        args = video_put_args.parse_args()
        return {video_id: args}
api.add_resource(Video,"/video/<int:video_id>")        
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5004,debug=True) 