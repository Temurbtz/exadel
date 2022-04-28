import  json
class  Converter:
   
   def csvtojson(self):
    f=open("input.csv","r")
    li=[]
    for item  in  f:
        item=item.strip()
        li.append(item)
    f.close()
    fields=li[0]
    fields=fields.split(";")
    li.remove(li[0])
    data=[]
    for item  in li:
      x={}
      item=item.split(";")
      for i  in  range(0,len(fields)-1):
          if item[i]!=None:
              if item[i].find(",")==-1:
                 x[fields[i]]=item[i]
              else:
                  x[fields[i]]=item[i].split(",")
          else:
               x[fields[i]]=''
      data.append(x)
    y={}
    y["data"]=data
    f1=open("output.json","w")
    f1.write(json.dumps(y))
    f1.close()
     
   def jsontocsv(self):
    f1=open("input.json","r")
    data=f1.read()
    f1.close()
    obj=json.loads(data)
    self.writefields(obj["data"][0])
    for  item in obj["data"]:
        self.writer(item)

   def  writefields(self,obj):
        columns=""
        for keys  in obj.keys():
            columns=columns+keys+";"
        f=open("output.csv","w")
        f.write(columns)
        f.write("\n")
        f.close()
   def  writer(self,obj):
        data=""
        for item in  obj.values():
            if type(item)==list:
               x=""
               for  it  in  item:
                   x=x+str(it)+","
               data=data+x[:-1]+";"
            else:
                data=data+str(item)+";"
      
        f=open("output.csv","a")
        f.write(data)
        f.write("\n")
        f.close()

   



x=Converter()
x.csvtojson()
x.jsontocsv()


