'''5.	Access the value of key “history”
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}
Expected output: 80
'''
d={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(d['class']['student']['marks']['history'])

