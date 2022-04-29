import  json
from context_manager  import File
class  Converter:
   def csv_to_json(self):
    temp_storage=[]
    with File('input.csv', 'r') as opened_file:
        for item  in  opened_file:
            item=item.strip()
            temp_storage.append(item)
    fields=temp_storage[0]
    fields=fields.split(";")
    temp_storage.remove(temp_storage[0])
    data=[]
    for item  in temp_storage:
      new_object={}
      item=item.split(";")
      for i  in  range(0,len(fields)-1):
          if item[i]!=None:
              if item[i].find(",")==-1:
                 new_object[fields[i]]=item[i]
              else:
                  new_object[fields[i]]=item[i].split(",")
          else:
               new_object[fields[i]]=''
      data.append(new_object)
    final_object={}
    final_object["data"]=data
    with File("output.json","w") as  opened_file:
        opened_file.write(json.dumps(final_object))
  
     
   def json_to_csv(self):
        with  File("input.json","r")  as  opened_file:
            data=opened_file.read()
        parsed_object=json.loads(data)
        self.write_fields(parsed_object["data"][0])
        for  item in parsed_object["data"]:
            self.writer(item)

   def  write_fields(self,field_object):
        columns=""
        for keys  in field_object.keys():
            columns=columns+keys+";"
        with  File("output.csv","w") as  opened_file:
            opened_file.write(columns)
            opened_file.write("\n")
   def  writer(self,csv_item):
        data=""
        for item in  csv_item.values():
            if type(item)==list:
               temp_storage=""
               for  inner_item  in  item:
                   temp_storage=temp_storage+str(inner_item)+","
               data=data+temp_storage[:-1]+";"
            else:
                data=data+str(item)+";"
        with File("output.csv","a")  as  opened_file:
            opened_file.write(data)
            opened_file.write("\n")

   


converter=Converter()
converter.json_to_csv()
converter.csv_to_json()
